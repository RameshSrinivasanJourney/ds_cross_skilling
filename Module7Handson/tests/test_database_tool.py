from app.database.database import (
    initialize_database,
)
from app.tools.database_tool import (
    query_database,
)


def test_database_tool():

    initialize_database()

    result = query_database(
        """
        SELECT name, department, city
        FROM employees
        WHERE city = 'Chennai'
        """
    )

    print("\nDatabase Result:")

    print(result)


if __name__ == "__main__":
    test_database_tool()