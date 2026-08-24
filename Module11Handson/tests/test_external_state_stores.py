from app.stores.sqlite_state_store import (
    SQLiteStateStore,
)


def test_sqlite_state_store():

    store = SQLiteStateStore()

    key = "session:employee-001"

    state = {
        "user_id": "employee-001",
        "current_task": (
            "Learning Memory Systems"
        ),
        "current_module": 11,
        "completed_topics": [
            1,
            2,
            3,
        ],
    }

    print(
        "\n=== SQLITE SAVE ==="
    )

    store.save(
        key,
        state,
    )

    print(state)

    print(
        "\n=== SQLITE LOAD ==="
    )

    loaded = store.get(
        key
    )

    print(loaded)

    assert loaded == state

    store.close()


if __name__ == "__main__":
    test_sqlite_state_store()