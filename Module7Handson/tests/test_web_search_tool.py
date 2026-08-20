from app.tools.web_search_tool import search_web


def test_web_search():

    query = "Python FastAPI"

    result = search_web(
        query=query,
        max_results=3
    )

    print("\nSearch Query:")
    print(query)

    print("\nSearch Results:")

    for item in result["results"]:
        print("\nTitle:")
        print(item["title"])

        print("URL:")
        print(item["url"])

        print("Snippet:")
        print(item["snippet"])


if __name__ == "__main__":
    test_web_search()