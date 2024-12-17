import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode

async def main():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html",process_iframes=True)
        # Soone will be change to result.markdown
        print(result.markdown_v2.raw_markdown) 

if __name__ == "__main__":
    asyncio.run(main())