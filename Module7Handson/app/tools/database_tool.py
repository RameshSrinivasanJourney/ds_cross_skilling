from app.database.database import get_connection


def query_database(city: str) -> dict:
    """
    Find employees by city using a parameterized query.
    """

    sql = """
        SELECT name, department, city, experience
        FROM employees
        WHERE city = ?
    """

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            sql,
            (city,)
        )

        columns = [
            description[0]
            for description in cursor.description
        ]

        rows = cursor.fetchall()

        results = [
            dict(zip(columns, row))
            for row in rows
        ]

        return {
            "city": city,
            "rows": results,
            "row_count": len(results),
        }

    finally:
        connection.close()