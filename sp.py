import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def crawl_gitlab_page():
    url = "https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html"
    
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url=url,
            cache_mode=CacheMode.BYPASS,
            magic=True,
            extract_text=True,
            preserve_code_blocks=True,
            extract_links=True
        )
        
        if result.success:
            # Try to get content from any available source
            content = result.markdown or result.extracted_content or result.html
            
            if content:
                print("\n=== EXTRACTED CONTENT ===\n")
                print(content)
                return content
            else:
                logger.error("No content found")
                return None
        else:
            logger.error(f"Failed to crawl: {result.error_message}")
            return None

if __name__ == "__main__":
    asyncio.run(crawl_gitlab_page())