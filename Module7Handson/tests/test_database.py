from app.database.database import (
    initialize_database,
    get_connection,
)


def test_database():

    initialize_database()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM employees"
    )

    rows = cursor.fetchall()

    print("\nEmployees:")

    for row in rows:
        print(row)

    connection.close()


if __name__ == "__main__":
    test_database()