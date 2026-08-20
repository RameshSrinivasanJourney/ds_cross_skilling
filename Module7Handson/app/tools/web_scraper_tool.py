from html.parser import HTMLParser

import httpx


class TextExtractor(HTMLParser):
    """Extract visible text from HTML."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_content = False

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip_content = True

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.skip_content = False

    def handle_data(self, data):
        if not self.skip_content:
            text = data.strip()

            if text:
                self.text_parts.append(text)

    def get_text(self):
        return " ".join(self.text_parts)


def scrape_web_page(
    url: str,
    max_chars: int = 3000,
) -> dict:
    """
    Fetch a web page and extract visible text.

    This tool only reads publicly accessible pages.
    """

    if not url.startswith(("http://", "https://")):
        return {
            "status": "failed",
            "error": "URL must start with http:// or https://.",
        }

    if max_chars <= 0:
        return {
            "status": "failed",
            "error": "max_chars must be greater than zero.",
        }

    try:
        response = httpx.get(
            url,
            timeout=10.0,
            follow_redirects=True,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Module7Handson Web Scraper)"
                )
            },
        )

        response.raise_for_status()

    except httpx.HTTPError as exc:
        return {
            "status": "failed",
            "error": f"Unable to fetch webpage: {exc}",
        }

    parser = TextExtractor()
    parser.feed(response.text)

    text = parser.get_text()

    if not text:
        return {
            "status": "failed",
            "error": "No readable text found on the webpage.",
        }

    return {
        "status": "success",
        "url": str(response.url),
        "status_code": response.status_code,
        "content": text[:max_chars],
        "content_length": len(text),
    }