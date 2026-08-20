import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/employees.db")


def get_connection():
    """Create a database connection."""

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    return sqlite3.connect(
        DATABASE_PATH
    )


def initialize_database():
    """Create the employees table and sample data."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            city TEXT NOT NULL,
            experience INTEGER NOT NULL
        )
        """
    )

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    count = cursor.fetchone()[0]

    if count == 0:

        employees = [
            (
                1,
                "Ramesh",
                "Engineering",
                "Chennai",
                16
            ),
            (
                2,
                "Arun",
                "Engineering",
                "Bangalore",
                10
            ),
            (
                3,
                "Priya",
                "HR",
                "Chennai",
                8
            ),
            (
                4,
                "Karthik",
                "Finance",
                "Mumbai",
                12
            ),
            (
                5,
                "Divya",
                "Engineering",
                "Chennai",
                6
            ),
        ]

        cursor.executemany(
            """
            INSERT INTO employees
            (
                id,
                name,
                department,
                city,
                experience
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            employees
        )

    connection.commit()
    connection.close()