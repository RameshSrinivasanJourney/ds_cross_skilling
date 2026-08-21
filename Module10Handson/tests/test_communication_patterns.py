from app.communication.blackboard import (
    run_blackboard,
)
from app.communication.hierarchical import (
    run_hierarchical,
)
from app.communication.hub_spoke import (
    run_hub_and_spoke,
)
from app.communication.peer_to_peer import (
    run_peer_to_peer,
)
from app.communication.pipeline import (
    run_pipeline,
)


GOAL = (
    "Prepare a clear employee-facing explanation "
    "of how an employee should approach a question "
    "about company leave policy."
)


def test_hub_and_spoke():

    result = run_hub_and_spoke(GOAL)

    print("\nResult:")
    print(result["pattern"])
    print("Review:")
    print(result["review"])


def test_peer_to_peer():

    result = run_peer_to_peer(GOAL)

    print("\nResult:")
    print(result["pattern"])
    print("Draft:")
    print(result["draft"])


def test_hierarchical():

    result = run_hierarchical(GOAL)

    print("\nResult:")
    print(result["pattern"])
    print("Draft:")
    print(result["draft"])


def test_blackboard():

    result = run_blackboard(GOAL)

    print("\nResult:")
    print(result["pattern"])

    print("\nShared State Keys:")
    print(
        list(
            result["state"].keys()
        )
    )


def test_pipeline():

    result = run_pipeline(GOAL)

    print("\nResult:")
    print(result["pattern"])

    print("Review:")
    print(result["review"])


if __name__ == "__main__":

    test_hub_and_spoke()
    test_peer_to_peer()
    test_hierarchical()
    test_blackboard()
    test_pipeline()