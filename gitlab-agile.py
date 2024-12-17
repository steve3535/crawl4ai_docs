import asyncio
import os
from typing import List, Dict, Any
from crawl4ai.async_webcrawler import AsyncWebCrawler
from urllib.parse import urljoin, urlparse

class GitLabUniversityCrawler:
    def __init__(self, base_url: str, output_dir: str = "gitlab_university"):
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.crawler = None
        
    async def setup(self):
        self.crawler = AsyncWebCrawler(verbose=True)
        await self.crawler.awarmup()
        os.makedirs(self.output_dir, exist_ok=True)
        
    async def cleanup(self):
        if self.crawler:
            await self.crawler.aclear_cache()
            
    def is_same_domain(self, url: str) -> bool:
        """Check if URL belongs to the same domain as base_url"""
        base_domain = urlparse(self.base_url).netloc
        url_domain = urlparse(url).netloc
        return base_domain == url_domain
        
    async def extract_links(self, html: str) -> List[str]:
        """Extract all links from the HTML content"""
        result = await self.crawler.arun(
            url=self.base_url,  # dummy url for extraction
            html=html,
            css_selector="a[href]",
            bypass_cache=True
        )
        
        links = []
        if result.success:
            for link in result.links.get('internal', []):
                if link.startswith('/') or self.is_same_domain(link):
                    full_url = urljoin(self.base_url, link)
                    links.append(full_url)
        return links
        
    def save_markdown(self, url: str, markdown: str):
        """Save markdown content to a file"""
        # Create filename from URL
        parsed = urlparse(url)
        filename = parsed.path.strip('/').replace('/', '_') or 'index'
        filepath = os.path.join(self.output_dir, f"{filename}.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {url}\n\n")
            f.write(markdown)
            
    async def crawl_page(self, url: str):
        """Crawl a single page and its subpages recursively"""
        if url in self.visited_urls:
            return
            
        print(f"Crawling: {url}")
        self.visited_urls.add(url)
        
        result = await self.crawler.arun(
            url=url,
            bypass_cache=True,
            crawler_params={
                "headless": True,
                "wait_for": "article, .content, main",  # Wait for main content
                "timeout": 30000
            },
            extra={
                "word_count_threshold": 10  # Filter out small text blocks
            }
        )
        
        if result.success:
            # Save the markdown content
            self.save_markdown(url, result.markdown)
            
            # Extract and crawl links
            links = await self.extract_links(result.html)
            for link in links:
                await self.crawl_page(link)
                
    async def crawl(self):
        """Main crawling method"""
        await self.setup()
        try:
            await self.crawl_page(self.base_url)
        finally:
            await self.cleanup()

async def main():
    base_url = "https://university.gitlab.com/learn/course/gitlab-agile-project-management-s2"
    crawler = GitLabUniversityCrawler(base_url)
    await crawler.crawl()

if __name__ == "__main__":
    asyncio.run(main())