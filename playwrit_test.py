import asyncio
from playwright.async_api import async_playwright
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def extract_gitlab_content():
    url = "https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        try:
            # Navigate to the page
            await page.goto(url, wait_until='networkidle')
            
            # Wait for content to be available
            await page.wait_for_selector('article[data-testid="main-content"]')
            
            # Extract the content using JavaScript
            content = await page.evaluate('''() => {
                function processNode(node) {
                    // Skip certain elements
                    if (node.classList && (
                        node.classList.contains('nav-sidebar') ||
                        node.classList.contains('nav-controls') ||
                        node.classList.contains('footer'))) {
                        return '';
                    }
                    
                    let result = '';
                    
                    // Handle code blocks
                    if (node.tagName === 'PRE') {
                        const code = node.querySelector('code');
                        if (code) {
                            return '```\\n' + code.innerText + '\\n```\\n\\n';
                        }
                    }
                    
                    // Handle headings
                    if (['H1', 'H2', 'H3', 'H4', 'H5', 'H6'].includes(node.tagName)) {
                        const level = node.tagName[1];
                        const prefix = '#'.repeat(parseInt(level));
                        return `${prefix} ${node.textContent.trim()}\\n\\n`;
                    }
                    
                    // Handle lists
                    if (node.tagName === 'LI') {
                        return `* ${node.textContent.trim()}\\n`;
                    }
                    
                    // Handle paragraphs
                    if (node.tagName === 'P') {
                        return node.textContent.trim() + '\\n\\n';
                    }
                    
                    // Recursively process child nodes
                    for (const child of node.childNodes) {
                        if (child.nodeType === 3) { // Text node
                            result += child.textContent.trim() + ' ';
                        } else if (child.nodeType === 1) { // Element node
                            result += processNode(child);
                        }
                    }
                    
                    return result;
                }
                
                const article = document.querySelector('article[data-testid="main-content"]');
                return processNode(article);
            }''')
            
            if content:
                # Clean up the content
                content = re.sub(r'\n{3,}', '\n\n', content)  # Remove excessive newlines
                content = re.sub(r' {2,}', ' ', content)      # Remove excessive spaces
                
                # Add title
                title = await page.title()
                content = f"# {title}\n\n{content}"
                
                print("\n=== EXTRACTED CONTENT ===\n")
                print(content)
                return content
            else:
                logger.error("No content found")
                return None
                
        except Exception as e:
            logger.error(f"Error extracting content: {str(e)}")
            return None
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(extract_gitlab_content())