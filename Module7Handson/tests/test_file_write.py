from app.tools.file_tool import write_file


def test_file_write():

    result = write_file(
        "output.txt",
        "This file was created using a tool."
    )

    print("\nWrite Result:")
    print(result)


if __name__ == "__main__":
    test_file_write()