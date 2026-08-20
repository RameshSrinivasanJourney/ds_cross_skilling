from app.tools.web_scraper_tool import scrape_web_page


def test_web_scraper_validation():

    result = scrape_web_page(
        url="example.com",
        max_chars=1000,
    )

    print("\nValidation Result:")
    print(result)


if __name__ == "__main__":
    test_web_scraper_validation()