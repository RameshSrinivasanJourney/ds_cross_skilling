from app.orchestration.role_based_system import (
    run_role_based_system,
)


def test_agent_roles():

    goal = (
        "Prepare a clear employee-facing explanation "
        "of how an employee should approach a question "
        "about company leave policy."
    )

    result = run_role_based_system(
        goal
    )

    print("\n=== FINAL RESULT ===")
    print(result["final"])


if __name__ == "__main__":
    test_agent_roles()