import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import os
from pathlib import Path

class LXPDocsCrawler:
    def __init__(self, base_url: str, output_dir: str = "lxp_docs"):
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.base_domain = urlparse(base_url).netloc
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
    async def fetch_page(self, session: aiohttp.ClientSession, url: str) -> str:
        """Fetch a single page with proper headers."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        try:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print(f"Failed to fetch {url}: Status {response.status}")
                    return None
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None

    def is_valid_doc_url(self, url: str, current_page_url: str) -> bool:
        """Check if URL is a valid documentation page."""
        if not url:
            return False
            
        # Handle relative URLs
        full_url = urljoin(current_page_url, url)
        parsed = urlparse(full_url)
        
        # Skip certain URLs
        if (
            '#' in url  # Skip anchor links
            or url.startswith('mailto:')  # Skip mail links
            or parsed.netloc != self.base_domain  # Stay on the same domain
            or any(url.endswith(ext) for ext in ['.png', '.jpg', '.gif', '.pdf', '.zip'])  # Skip binary files
        ):
            return False
            
        return True

    def sanitize_filename(self, url: str) -> str:
        """Convert URL to a valid filename."""
        path = urlparse(url).path
        # Remove trailing slash and handle index
        path = path.rstrip('/')
        if not path or path == '':
            return 'index'
            
        # Convert path to filename
        filename = path.strip('/').replace('/', '_')
        return filename or 'index'

    def clean_content(self, text: str) -> str:
        """Clean and format extracted text content."""
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith(('Skip to', '<<', '>>', '«', '»')):
                cleaned_lines.append(line)
                
        return '\n\n'.join(cleaned_lines)

    def extract_content(self, soup: BeautifulSoup, current_url: str) -> tuple:
        """Extract title and content from the page."""
        content = {}
        
        # Find title
        title = soup.find('h1')
        if not title:
            title = soup.find('title')
        content['title'] = title.get_text().strip() if title else 'Untitled'
        
        # Find main content - Material for MkDocs specific
        main_content = soup.find('article', class_='md-content__inner') or \
                      soup.find('div', class_='md-content__inner') or \
                      soup.find('div', class_='md-typeset')
                      
        if main_content:
            # Extract text content with proper formatting
            content_text = []
            
            # Process headings and content
            for elem in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'pre', 'code', 'div']):
                if 'admonition' in elem.get('class', []):
                    # Handle admonition blocks (info, warning, etc.)
                    title = elem.find(class_='admonition-title')
                    if title:
                        content_text.append(f"\n> **{title.get_text().strip()}**")
                    body = elem.find('p')
                    if body:
                        content_text.append(f"> {body.get_text().strip()}\n")
                else:
                    text = elem.get_text().strip()
                    if text:
                        if elem.name.startswith('h'):
                            level = int(elem.name[1])
                            content_text.append(f"\n{'#' * level} {text}")
                        elif elem.name == 'li':
                            content_text.append(f"- {text}")
                        elif elem.name in ['pre', 'code']:
                            content_text.append(f"```\n{text}\n```")
                        else:
                            content_text.append(text)
            
            content['text'] = self.clean_content('\n'.join(content_text))
            
            # Extract links
            links = []
            for link in main_content.find_all('a', href=True):
                href = link['href']
                if href and self.is_valid_doc_url(href, current_url):
                    full_url = urljoin(current_url, href)
                    links.append(full_url)
            
            return content, links
        
        return content, []

    async def crawl_all(self):
        """Crawl all documentation pages starting from base_url."""
        async with aiohttp.ClientSession() as session:
            to_visit = [self.base_url]
            
            while to_visit:
                url = to_visit.pop(0)
                if url in self.visited_urls:
                    continue
                
                print(f"\nProcessing: {url}")
                self.visited_urls.add(url)
                
                content = await self.fetch_page(session, url)
                if content:
                    soup = BeautifulSoup(content, 'html.parser')
                    page_content, new_links = self.extract_content(soup, url)
                    
                    if page_content:
                        filename = self.sanitize_filename(url)
                        filepath = os.path.join(self.output_dir, f"{filename}.md")
                        
                        # Create markdown content
                        markdown_content = f"# {page_content['title']}\n\n"
                        markdown_content += f"Source: {url}\n\n"
                        markdown_content += page_content.get('text', '')
                        
                        # Save to file
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(markdown_content)
                        print(f"Saved: {filepath}")
                        
                        # Add new links to visit
                        for link in new_links:
                            if link not in self.visited_urls and link not in to_visit:
                                to_visit.append(link)
                                print(f"Found new link: {link}")
                
                # Small delay between requests
                await asyncio.sleep(1)

async def main():
    base_url = "https://docs.lxp.lu/"
    crawler = LXPDocsCrawler(base_url)
    await crawler.crawl_all()

if __name__ == "__main__":
    asyncio.run(main())