from app.tools.file_tool import read_file


def test_file_read():

    result = read_file(
        "sample.txt"
    )

    print("\nFile Result:")
    print(result)


if __name__ == "__main__":
    test_file_read()