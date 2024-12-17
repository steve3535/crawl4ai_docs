import asyncio
from crawl4ai import AsyncWebCrawler, CacheMode
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator

async def main():
    async with AsyncWebCrawler(
        headless=True,  
        verbose=True,
    ) as crawler:
        result = await crawler.arun(
            url="https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html",
            cache_mode=CacheMode.ENABLED,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(threshold=0.48, threshold_type="fixed", min_word_threshold=0)
            ),
            # markdown_generator=DefaultMarkdownGenerator(
            #     content_filter=BM25ContentFilter(user_query="WHEN_WE_FOCUS_BASED_ON_A_USER_QUERY", bm25_threshold=1.0)
            # ),
        )
        print(len(result.markdown))
        print(len(result.fit_markdown))
        print(len(result.markdown_v2.fit_markdown))

if __name__ == "__main__":
    asyncio.run(main())