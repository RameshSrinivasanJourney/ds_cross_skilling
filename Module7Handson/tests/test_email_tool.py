from app.tools.email_tool import send_email


def test_email_tool():

    result = send_email(
        to="ramesh@example.com",
        subject="Module 7 Test",
        body="This is a test email from the Module 7 tool.",
    )

    print("\nEmail Result:")
    print(result)


if __name__ == "__main__":
    test_email_tool()