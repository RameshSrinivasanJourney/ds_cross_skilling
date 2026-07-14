def build_json_prompt(user_question: str):
    return f"""
You are an Employee Helpdesk AI.

Analyze the employee request and return ONLY valid JSON.

Use this schema exactly:

{{
    "department": "",
    "category": "",
    "priority": "",
    "summary": "",
    "employee_response": ""
}}

Rules:

- Return JSON only.
- No markdown.
- No explanation.
- No additional text.
- Fill every field.

Employee Request:

{user_question}
"""