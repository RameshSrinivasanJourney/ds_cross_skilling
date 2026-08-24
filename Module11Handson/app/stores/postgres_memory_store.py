import json
from typing import Any

import psycopg

from app.stores.state_store import StateStore


class PostgreSQLMemoryStore(StateStore):
    """PostgreSQL-backed structured memory."""

    def __init__(
        self,
        connection_string: str,
    ) -> None:

        self.connection = (
            psycopg.connect(
                connection_string
            )
        )

        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS agent_memory (
                memory_key TEXT PRIMARY KEY,
                memory_value JSONB NOT NULL
            )
            """
        )

        self.connection.commit()

    def save(
        self,
        key: str,
        value: dict[str, Any],
    ) -> None:

        self.connection.execute(
            """
            INSERT INTO agent_memory
                (memory_key, memory_value)
            VALUES (%s, %s)
            ON CONFLICT (memory_key)
            DO UPDATE SET
                memory_value = EXCLUDED.memory_value
            """,
            (
                key,
                json.dumps(value),
            ),
        )

        self.connection.commit()

    def get(
        self,
        key: str,
    ) -> dict[str, Any] | None:

        cursor = self.connection.execute(
            """
            SELECT memory_value
            FROM agent_memory
            WHERE memory_key = %s
            """,
            (key,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    def close(self) -> None:
        self.connection.close()