import asyncio
from crawl4ai import AsyncWebCrawler

BASE_URL = "https://docs.gitlab.com/ee/user/project/merge_requests/index.html"
OUTPUT_FILE = "gitlab_merge_requests.md"  # Output file name

async def fetch_merge_requests_docs():
    async with AsyncWebCrawler(verbose=True) as crawler:
        # Start crawling from the base URL
        result = await crawler.arun(
            url=BASE_URL,
            follow_links=True,  # Follow related links
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
        )

        # Check if the result has a 'markdown' attribute
        if hasattr(result, "markdown"):
            markdown_doc = "# GitLab Documentation\n\n"
            markdown_doc += result.markdown  # Add the Markdown content
            
            # Save the Markdown document to a file
            with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
                file.write(markdown_doc)

            print(f"Documentation saved to {OUTPUT_FILE}")
        else:
            print("Error: The result does not contain markdown content.")

if __name__ == "__main__":
    asyncio.run(fetch_merge_requests_docs())
