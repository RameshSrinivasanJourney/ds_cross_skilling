from app.tools.web_scraper_tool import scrape_web_page


def test_web_scraper():

    result = scrape_web_page(
        url="https://example.com",
        max_chars=1000,
    )

    print("\nWeb Scraper Result:")
    print(result)


if __name__ == "__main__":
    test_web_scraper()