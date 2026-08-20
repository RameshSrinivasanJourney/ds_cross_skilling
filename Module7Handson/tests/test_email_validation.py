from app.tools.email_tool import send_email


def test_email_validation():

    result = send_email(
        to="invalid-email",
        subject="Test",
        body="Hello",
    )

    print("\nValidation Result:")
    print(result)


if __name__ == "__main__":
    test_email_validation()