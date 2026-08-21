from dataclasses import dataclass


@dataclass
class TaskDefinition:
    """Represent one decomposed task."""

    name: str
    description: str
    dependencies: list[str]


def decompose_leave_report() -> list[TaskDefinition]:
    """Break the employee report into subtasks."""

    return [
        TaskDefinition(
            name="policy_research",
            description=(
                "Research the important policy "
                "information needed for the employee "
                "leave report."
            ),
            dependencies=[],
        ),
        TaskDefinition(
            name="eligibility_research",
            description=(
                "Research eligibility-related "
                "information needed for the report."
            ),
            dependencies=[],
        ),
        TaskDefinition(
            name="process_research",
            description=(
                "Research the process and procedure "
                "information needed for the report."
            ),
            dependencies=[],
        ),
        TaskDefinition(
            name="analysis",
            description=(
                "Analyze all research findings and "
                "identify the most important conclusions."
            ),
            dependencies=[
                "policy_research",
                "eligibility_research",
                "process_research",
            ],
        ),
        TaskDefinition(
            name="report",
            description=(
                "Generate the final employee-facing "
                "leave-policy report."
            ),
            dependencies=["analysis"],
        ),
    ]