from app.tools.weather_tool import get_weather
from app.tools.calculator_tool import calculate
from app.tools.web_search_tool import search_web
from app.tools.code_execution_tool import execute_code
from app.tools.database_tool import query_database
from app.tools.rest_api_tool import call_rest_api
from app.tools.file_tool import (
    read_file,
    write_file,
)
from app.tools.email_tool import send_email
from app.tools.calendar_tool import (
    create_calendar_event,
)
from app.tools.web_scraper_tool import (
    scrape_web_page,
)

TOOL_REGISTRY = {
    "get_current_weather": get_weather,
    "calculate": calculate,
    "search_web": search_web,
    "execute_code": execute_code,
    "query_database": query_database,
    "call_rest_api": call_rest_api,
    "read_file": read_file,
    "write_file": write_file,
    "send_email": send_email,
    "create_calendar_event": create_calendar_event,
    "scrape_web_page": scrape_web_page,
}