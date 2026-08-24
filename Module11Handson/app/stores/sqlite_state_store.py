import json
import sqlite3
from pathlib import Path
from typing import Any

from app.stores.state_store import StateStore


DATABASE_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "session_state.db"
)


class SQLiteStateStore(StateStore):
    """Local SQLite-backed state store."""

    def __init__(self) -> None:

        DATABASE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.connection = sqlite3.connect(
            DATABASE_PATH
        )

        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS session_state (
                state_key TEXT PRIMARY KEY,
                state_value TEXT NOT NULL
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
            INSERT OR REPLACE INTO session_state
            (state_key, state_value)
            VALUES (?, ?)
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
            SELECT state_value
            FROM session_state
            WHERE state_key = ?
            """,
            (key,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return json.loads(row[0])

    def close(self) -> None:
        self.connection.close()
        