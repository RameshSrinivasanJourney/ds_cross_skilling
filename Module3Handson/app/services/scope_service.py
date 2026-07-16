class ScopeService:

    HR_KEYWORDS = [

        "leave",

        "salary",

        "payroll",

        "benefits",

        "employee",

        "holiday",

        "policy",

        "promotion",

        "attendance",

        "manager"

    ]

    @staticmethod
    def is_hr_related(question: str):

        question = question.lower()

        return any(

            keyword in question

            for keyword in ScopeService.HR_KEYWORDS

        )