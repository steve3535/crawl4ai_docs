import asyncio
from crawl4ai import AsyncWebCrawler

BASE_URL = "https://docs.gitlab.com/ee/ci/index.html"
OUTPUT_FILE = "gitlab_ci.md"  # Output file name

async def fetch_gitlab_docs():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # Start crawling from the base URL
        result = await crawler.arun(
            url=BASE_URL,
            follow_links=True,  # Follow all related links
            allowed_domains=["docs.gitlab.com"],  # Restrict domain
            allowed_path_patterns=[
                r"^/ee/user/project/merge_requests",  # Merge Requests section
                r"^/ee/ci/",                         # Continuous Integration section
                r"^/ee/user/discussions/",            # Discussions section
                r"^/ee/topics/git/",                 # Git-related topics
            ],
            exclude_path_patterns=[
                r"^/about", r"^/privacy", r"^/terms",  # Exclude unrelated topics
            ],
            max_depth=10,  # Increase depth to ensure we capture all relevant subpages
        )

        # Combine results into a structured Markdown document
        markdown_doc = "# GitLab Documentation\n\n"
        markdown_doc += result.markdown  # Add the Markdown content
        
        # Save the Markdown document to a file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(markdown_doc)

        print(f"Documentation saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(fetch_gitlab_docs())
