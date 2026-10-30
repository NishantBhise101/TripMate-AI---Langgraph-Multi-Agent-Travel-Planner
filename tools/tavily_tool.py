import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

# "TRAVILY_API_KEY" is retained as a compatibility fallback for the typo
# used in existing .env files.
_tavily_api_key = os.getenv("TAVILY_API_KEY") or os.getenv("TRAVILY_API_KEY")


def _get_client():
    if not _tavily_api_key:
        raise RuntimeError(
            "Tavily API key is not configured. Set TAVILY_API_KEY in .env."
        )
    return TavilyClient(api_key=_tavily_api_key)


def tavily_search(query):
    response = _get_client().search(
        query= query,
        max_results= 5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title   = r.get("title", "Unknown")
        url     = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)