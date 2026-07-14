def build_leave_extraction_prompt(user_message: str):
    return f"""
Extract the leave information.

Return ONLY valid JSON.

Schema:

{{
    "leave_type":"",
    "start_date":"",
    "end_date":""
}}

Employee Request:

{user_message}
"""