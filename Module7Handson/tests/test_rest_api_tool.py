from app.tools.rest_api_tool import call_rest_api


def test_rest_api_tool():

    result = call_rest_api(
        "users"
    )

    print("\nREST API Result:")

    print(
        f"Status Code: "
        f"{result.get('status_code')}"
    )

    print(
        f"Resource: "
        f"{result.get('resource')}"
    )

    print("\nData:")

    for user in result["data"][:3]:

        print(
            f"{user['name']} - "
            f"{user['email']}"
        )


if __name__ == "__main__":
    test_rest_api_tool()