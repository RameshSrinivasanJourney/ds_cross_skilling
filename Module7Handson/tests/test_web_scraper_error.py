from app.tools.web_scraper_tool import scrape_web_page


def test_web_scraper_error():

    result = scrape_web_page(
        url="https://this-domain-does-not-exist-123456789.com",
        max_chars=1000,
    )

    print("\nError Result:")
    print(result)


if __name__ == "__main__":
    test_web_scraper_error()