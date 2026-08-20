# Module 7 - Function Calling & Tool Use with LLMs

## Overview

This module focuses on **Function Calling and Tool Use with Large Language Models (LLMs)**.

In previous modules, we learned how LLMs generate text, work with prompts, embeddings, vector databases, and advanced RAG techniques.

In this module, we move one step further:

> **Instead of only generating text, the LLM learns how to decide when to call external tools and how to use their results.**

A modern AI agent can interact with:

- APIs
- Databases
- Files
- Web search
- Calculators
- Code execution
- Email systems
- Calendar systems
- Web pages
- Enterprise applications

The LLM itself does not directly execute these operations.

Instead, it:

1. Understands the user's request
2. Selects an appropriate tool
3. Generates structured arguments
4. Requests the application to execute the tool
5. Receives the tool result
6. Uses the result to generate the final response

---

# Learning Objectives

By the end of this module, you will understand and implement:

- Function calling fundamentals
- Tool definitions
- Tool descriptions
- Required and optional parameters
- Enum parameters
- Array parameters
- Tool detection
- Tool execution
- Tool result handling
- Multi-turn tool calling
- Parallel tool calling
- Web search tools
- Calculator / code execution tools
- Database tools
- File tools
- Email tools
- Calendar tools
- Web scraper tools
- Tool selection patterns
- Tool chaining
- Tool error handling
- Tool result formatting
- Role-based tool access control

---

# Module Architecture

The overall architecture implemented in this module is:

```text
                         User
                           |
                           v
                    +-------------+
                    |     LLM     |
                    +-------------+
                           |
                    Tool Selection
                           |
                           v
                 +-------------------+
                 |   Tool Definition |
                 +-------------------+
                           |
                           v
                 Tool Name + Arguments
                           |
                           v
                 +-------------------+
                 |   Tool Registry   |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | Authorization    |
                 | / Role Check      |
                 +-------------------+
                           |
                           v
                    Tool Execution
                           |
                           v
                 +-------------------+
                 | Tool Result       |
                 +-------------------+
                           |
                           v
                 +-------------------+
                 | Result Formatting  |
                 +-------------------+
                           |
                           v
                         LLM
                           |
                           v
                    Final Response

# Project Structure

The Module 7 hands-on project is organized approximately as follows:

Module7Handson/
│
├── app/
│   ├── models/
│   │   └── tool_models.py
│   │
│   ├── prompts/
│   │
│   ├── security/
│   │   └── tool_access.py
│   │
│   ├── services/
│   │   ├── ollama_service.py
│   │   ├── tool_executor.py
│   │   └── tool_result_formatter.py
│   │
│   ├── tools/
│   │   ├── weather_tool.py
│   │   ├── calculator_tool.py
│   │   ├── database_tool.py
│   │   ├── file_tool.py
│   │   ├── email_tool.py
│   │   ├── calendar_tool.py
│   │   ├── web_search_tool.py
│   │   ├── web_scraper_tool.py
│   │   └── tool_registry.py
│   │
│   └── ...
│
├── tests/
│   ├── test_required_optional.py
│   ├── test_enum_parameter.py
│   ├── test_array_parameter.py
│   ├── test_tool_detection.py
│   ├── test_tool_execution.py
│   ├── test_tool_result_return.py
│   ├── test_final_response.py
│   ├── test_multi_turn_tools.py
│   ├── test_parallel_tool_calls.py
│   ├── test_aggregate_results.py
│   ├── test_web_search_tool_calling.py
│   ├── test_web_search_complete.py
│   ├── test_code_execution_tool_calling.py
│   ├── test_code_execution_complete.py
│   ├── test_database.py
│   ├── test_database_tool.py
│   ├── test_database_tool_calling.py
│   ├── test_database_complete.py
│   ├── test_file_read.py
│   ├── test_file_write.py
│   ├── test_file_tool_calling.py
│   ├── test_file_complete.py
│   ├── test_email_tool.py
│   ├── test_email_validation.py
│   ├── test_email_tool_calling.py
│   ├── test_email_complete.py
│   ├── test_calendar_tool.py
│   ├── test_calendar_validation.py
│   ├── test_calendar_tool_calling.py
│   ├── test_calendar_complete.py
│   ├── test_web_scraper.py
│   ├── test_web_scraper_validation.py
│   ├── test_web_scraper_tool_calling.py
│   ├── test_web_scraper_complete.py
│   ├── test_web_scraper_error.py
│   ├── test_tool_chaining.py
│   ├── test_tool_error_handling.py
│   ├── test_tool_result_formatting.py
│   ├── test_tool_execution_formatting.py
│   ├── test_tool_access_control.py
│   └── test_role_based_tool_execution.py
│
├── data/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

# 1. Introduction to Function Calling
What is Function Calling?

Function calling allows an LLM to identify that a user's request requires an external function or tool.

For example:

User:
What is the weather in Chennai?

Instead of responding with an invented answer, the LLM can generate:

Tool:
get_current_weather


Arguments:
{
    "city": "Chennai"
}

The application executes the function:

get_weather(city="Chennai")

The tool returns:

{
    "city": "Chennai",
    "temperature": 32,
    "unit": "Celsius",
    "condition": "Sunny"
}

The LLM can then generate:

The current weather in Chennai is sunny with a temperature of 32°C.

# 2. Tool Definitions

A tool definition describes a function that the LLM is allowed to call.

A typical tool definition contains:

Name
Description
Parameters
Required parameters
Optional parameters
Parameter types
Enum values
Array definitions

Example:

CURRENT_WEATHER_TOOL = {
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city."
                }
            },
            "required": ["city"]
        }
    }
}

# 2.1 Tool Definition Structure

A tool definition can be represented as:

Tool
 |
 +-- Name
 |
 +-- Description
 |
 +-- Parameters
      |
      +-- Parameter Name
      +-- Type
      +-- Description
      +-- Required / Optional
      +-- Enum
      +-- Array

The LLM uses this information to decide when and how to call the tool.

# 2.2 Writing Effective Tool Descriptions

Tool descriptions are extremely important.

The LLM uses the description to determine whether a tool is appropriate.

Weak description:

"Weather tool"

Better:

"Get the current weather conditions for a specified city."

Good descriptions should explain:

What the tool does
When it should be used
What information it requires
What the tool returns

Example:

"description": """
Get the current weather conditions for a city.
Use this tool when the user asks about current weather,
temperature, or weather conditions.
"""

A good description improves tool selection.

# 2.3 Writing Effective Tool Descriptions

Tool descriptions should be:

Clear
Specific
Action-oriented
Unambiguous

Bad:

"Search"

Good:

"Search the web for current information and return relevant search results."

Bad:

"Database"

Good:

"Search the employee database using a city and return matching employee records."

The more precise the description, the easier it is for the LLM to select the correct tool.

# 2.4 Required vs Optional Parameters

Parameters can be required or optional.

Example:

"parameters": {
    "type": "object",
    "properties": {
        "city": {
            "type": "string"
        },
        "days": {
            "type": "integer"
        },
        "unit": {
            "type": "string"
        }
    },
    "required": ["city"]
}

Here:

city  -> Required
days  -> Optional
unit  -> Optional

Example:

User:
Give me the weather forecast for Chennai.

The LLM generated:

{
    "city": "Chennai",
    "days": 3,
    "unit": "Celsius"
}

For:

Give me the weather forecast for Chennai
for the next 5 days in Celsius.

The LLM generated:

{
    "city": "Chennai",
    "days": "5",
    "unit": "Celsius"
}

This demonstrates how the model fills parameters from the user's request.

# 2.5 Enum Parameters

Enum parameters restrict a parameter to a known set of values.

Example:

"operation": {
    "type": "string",
    "enum": [
        "add",
        "subtract",
        "multiply",
        "divide",
        "modulo"
    ]
}

The user asks:

Calculate 25 modulo 4.

The LLM generates:

{
    "a": "25",
    "b": "4",
    "operation": "modulo"
}

Enums reduce invalid tool arguments.

# 2.6 Practical Parameter Validation

Tool arguments should be validated before execution.

Example:

if operation not in allowed_operations:
    raise ValueError("Invalid operation")

Validation provides an additional safety layer between the LLM and the actual application.

# 2.7 Arrays as Parameter Types

Arrays allow a tool to accept multiple values.

Example:

"skills": {
    "type": "array",
    "items": {
        "type": "string"
    },
    "description": "List of required employee skills."
}

User request:

Search for employees with these skills:
Python, SQL, AWS.
Location: Chennai.

Tool call:

{
    "skills": [
        "Python",
        "SQL",
        "AWS"
    ],
    "location": "Chennai"
}

Arrays are useful for:

Multiple skills
Multiple products
Multiple cities
Multiple IDs
Multiple search terms
Multiple filters

# 3. Tool Calling Lifecycle

The basic function calling lifecycle is:

User Question
      ↓
LLM
      ↓
Tool Selection
      ↓
Tool Name + Arguments
      ↓
Application
      ↓
Tool Execution
      ↓
Tool Result
      ↓
LLM
      ↓
Final Response

# 3.1 Tool Detection

The application first determines whether the LLM requested a tool.

Example:

tool_calls = response["message"].get(
    "tool_calls",
    []
)

If no tool call exists:

if not tool_calls:
    ...

If a tool call exists:

tool_call.function.name

returns the tool name.

Arguments can be accessed through:

tool_call.function.arguments

# 3.2 Tool Execution

After detecting a tool call, the application retrieves the function from the tool registry.

Example:

tool_function = TOOL_REGISTRY.get(
    tool_name
)

Then:

result = tool_function(
    **arguments
)

This creates the bridge between:

LLM Tool Call
      ↓
Python Function

# 3.3 Returning Tool Results

The tool result must be sent back to the LLM.

Example:

{
    "role": "tool",
    "tool_name": "get_current_weather",
    "content": "{\"city\":\"Chennai\",\"temperature\":32}"
}

The LLM can then use the tool result to generate the final response.

# 3.4 Final Response Generation

After receiving the tool result, the LLM produces a natural-language answer.

Example:

The current weather in Chennai is sunny
with a temperature of 32°C.

This creates the complete function calling loop.

# 3.5 Multi-Turn Tool Calling

Sometimes a single user request requires multiple tool calls.

Example:

User:
Calculate the weather temperature multiplied by 2,
then add 10.

The workflow can become:

User
 ↓
Weather Tool
 ↓
32
 ↓
Calculator
 ↓
64
 ↓
Calculator
 ↓
74
 ↓
Final Response

Our multi-turn example successfully executed:

32 × 2 = 64
64 + 10 = 74

This demonstrates chained reasoning through tool calls.

# 3.6 Multi-Turn Tools

Example:

Executing tool: calculate
Arguments:
{
    "a": 32,
    "b": 2,
    "operation": "multiply"
}


Tool result:
64

Then:

Executing tool: calculate
Arguments:
{
    "a": 66,
    "b": 10,
    "operation": "add"
}


Tool result:
76

Final response:

The final result is 76.

# 4. Parallel Tool Calling

Parallel tool calling allows multiple independent tools to execute concurrently.

Example:

User:
What is the weather in Chennai
and calculate 25 multiplied by 4?

The LLM generates two tool calls:

Tool 1:
get_current_weather
{
    "city": "Chennai"
}


Tool 2:
calculate
{
    "a": 25,
    "b": 4,
    "operation": "multiply"
}

Because they are independent, they can execute concurrently.

# 4.1 Parallel Tool Calling Theory

Sequential execution:

Tool A
  ↓
Tool B

Parallel execution:

        ┌── Tool A ──┐
Request ┤            ├── Results
        └── Tool B ──┘

Parallel execution can reduce total latency.

# 4.2 Concurrent Execution

Python's ThreadPoolExecutor can be used:

with ThreadPoolExecutor(
    max_workers=len(tool_calls)
) as executor:
    ...

This allows multiple independent tools to run at the same time.

# 4.3 Aggregating Results

After parallel execution, results can be aggregated:

[
    {
        "tool_name": "get_current_weather",
        "result": {...}
    },
    {
        "tool_name": "calculate",
        "result": {...}
    }
]

The aggregated results are then returned to the LLM.

# 5. Practical Tools

This module implements several real-world tool patterns.

# 5.1 Web Search Tool

A web search tool allows the LLM to retrieve current information.

Example:

User:
Search the web and tell me what the latest Python version is.

Tool call:

{
    "query": "latest Python version",
    "max_results": 10
}

Tool:

search_web

The tool returns search results containing:

Title
URL
Snippet

The LLM then summarizes the results.

# 5.2 Calculator / Code Execution Tool

A code execution tool can evaluate mathematical expressions.

Example:

Use the calculation tool to evaluate:
(25 + 15) * 3

Tool call:

{
    "expression": "(25 + 15) * 3"
}

Result:

120

Final response:

The result of the calculation (25 + 15) * 3 is 120.

# 5.3 Database Tool

A database tool allows the LLM to retrieve structured data.

Example database:

employees


id | name    | department  | city      | experience
-----------------------------------------------------
1  | Ramesh  | Engineering | Chennai   | 16
2  | Arun    | Engineering | Bangalore | 10
3  | Priya   | HR          | Chennai   | 8
4  | Karthik | Finance     | Mumbai    | 12
5  | Divya   | Engineering | Chennai   | 6

User:

Find all employees who are based in Chennai.

Tool call:

{
    "city": "Chennai"
}

Result:

{
    "city": "Chennai",
    "rows": [
        {
            "name": "Ramesh",
            "department": "Engineering",
            "city": "Chennai",
            "experience": 16
        },
        {
            "name": "Priya",
            "department": "HR",
            "city": "Chennai",
            "experience": 8
        },
        {
            "name": "Divya",
            "department": "Engineering",
            "city": "Chennai",
            "experience": 6
        }
    ],
    "row_count": 3
}

# 5.4 File Tools

File tools allow the agent to read and write files.

Example:

Read the contents of sample.txt.

Tool call:

{
    "filename": "sample.txt"
}

Result:

Module 7 Function Calling Practice


Topics covered:
- Tool definitions
- Tool calling
- Parallel tool calling
- Web search
- Calculator
- Database queries
- REST APIs
- File tools

File write example:

{
    "filename": "output.txt",
    "content": "..."
}

# 5.5 REST API Tools

REST API tools allow the LLM to interact with external services.

Typical flow:

User
 ↓
LLM
 ↓
API Tool
 ↓
HTTP Request
 ↓
REST API
 ↓
JSON Response
 ↓
LLM

This pattern is commonly used in production AI agents.

# 5.6 Email Tool

An email tool demonstrates an action-oriented tool.

Example:

Send an email to ramesh@example.com
with subject "Module 7 Test"
and body "Function calling is working."

Tool call:

{
    "to": "ramesh@example.com",
    "subject": "Module 7 Test",
    "body": "Function calling is working."
}

The tool validates the email address before execution.

Invalid email:

Validation Result:
{
    "status": "failed",
    "error": "Invalid email address."
}

Important production consideration:

LLM
 ↓
Authorization
 ↓
Validation
 ↓
Email Service

The LLM should never directly control SMTP credentials.

# 5.7 Calendar Tool

The calendar tool demonstrates scheduling operations.

Example:

Schedule a meeting called "Module 7 Review"
on August 20, 2026 from 10:00 to 11:00.

Tool call:

{
    "date": "2026-08-20",
    "start_time": "10:00",
    "end_time": "11:00",
    "title": "Module 7 Review"
}

Validation includes:

Date format
Time format
Start time
End time
End time must be later than start time

Example validation failure:

{
    "status": "failed",
    "error": "End time must be later than start time."
}

# 5.8 Browser / Web Scraper Tool

A web scraper tool retrieves content from a webpage.

Example:

Read the webpage https://example.com
and tell me what it is about.

Tool call:

{
    "url": "https://example.com",
    "max_chars": 3000
}

Result:

{
    "status": "success",
    "url": "https://example.com",
    "status_code": 200,
    "content": "...",
    "content_length": 142
}

The tool validates that the URL begins with:

http://

or:

https://

Error example:

{
    "status": "failed",
    "error": "URL must start with http:// or https://."
}

# 6. Tool Use Patterns

This section focuses on production-oriented tool patterns.

# 6.1 Tool Selection via Descriptions

The LLM chooses tools based on their descriptions.

Example:

get_current_weather

should have a description such as:

Get current weather conditions for a city.

While:

search_web

should describe web search capabilities.

Clear descriptions reduce incorrect tool selection.

# 6.2 Tool Chaining

Tool chaining occurs when the output of one tool becomes the input to another tool.

Example:

User:
Get the temperature in Chennai
and multiply it by 2.

Step 1:

get_current_weather
        ↓
temperature = 32

Step 2:

calculate
a = 32
b = 2
operation = multiply
        ↓
64

Final:

64°C

The important concept is:

Tool A Output
      ↓
Extract Required Value
      ↓
Tool B Input

# 6.3 Error Handling When a Tool Fails

Tools can fail because of:

Invalid parameters
Network errors
Database errors
Authentication failures
Invalid input
External service failures
Programming errors

Example:

{
    "a": "invalid-value",
    "b": 2,
    "operation": "multiply"
}

The calculator produces:

{
    "status": "failed",
    "error": "could not convert string to float: 'invalid-value'"
}

Instead of allowing the entire application to crash, the error is converted into a structured result.

# 6.4 Tool Result Formatting

A standardized tool result format is useful for all tools.

Success:

{
    "status": "success",
    "data": {
        "city": "Chennai",
        "temperature": 32,
        "unit": "Celsius"
    }
}

Failure:

{
    "status": "failed",
    "error": "Unable to retrieve weather."
}

This creates a consistent contract:

                Tool
                 |
        +--------+--------+
        |                 |
     Success            Failure
        |                 |
     status             status
     success            failed
        |                 |
      data              error

A centralized formatter can be used:

ToolResultFormatter.success(result)

and:

ToolResultFormatter.failure(error)

This prevents every tool from inventing its own result format.

# 6.5 Role-Based Tool Access Control

Not every user should have access to every tool.

Example:

Tool	Employee	Manager	Admin
Weather	Yes	Yes	Yes
Calculator	Yes	Yes	Yes
Database	No	Yes	Yes
Email	No	Yes	Yes
Calendar	Yes	Yes	Yes
Read File	No	Yes	Yes
Write File	No	No	Yes
Code Execution	No	No	Yes

Permissions are defined at the application layer.

Example:

ROLE_TOOL_ACCESS = {
    "employee": {
        "get_current_weather",
        "calculate",
        "create_calendar_event",
    },


    "manager": {
        "get_current_weather",
        "calculate",
        "query_database",
        "send_email",
        "create_calendar_event",
        "read_file",
        "scrape_web_page",
        "search_web",
    },


    "admin": {
        "get_current_weather",
        "calculate",
        "query_database",
        "send_email",
        "create_calendar_event",
        "read_file",
        "write_file",
        "scrape_web_page",
        "search_web",
        "execute_code",
    },
}

# Authorization:

is_tool_allowed(
    role,
    tool_name
)

# The security principle is:

The LLM can request a tool, but the application must authorize the tool before execution.

Never rely on an LLM prompt as the security boundary.

# Security Architecture

A production-oriented tool execution pipeline should look like:

                     User
                       |
                       v
                     LLM
                       |
                       v
                 Tool Selection
                       |
                       v
              Tool Name + Arguments
                       |
                       v
              +-------------------+
              | Authentication   |
              +-------------------+
                       |
                       v
              +-------------------+
              | Authorization    |
              +-------------------+
                       |
                       v
              +-------------------+
              | Input Validation |
              +-------------------+
                       |
                       v
              +-------------------+
              | Tool Execution    |
              +-------------------+
                       |
                       v
              +-------------------+
              | Error Handling    |
              +-------------------+
                       |
                       v
              +-------------------+
              | Result Formatting |
              +-------------------+
                       |
                       v
                     LLM
                       |
                       v
                 Final Response

# Key Concepts Learned

Function Calling

LLM generates structured requests to external functions.

Tool Definition

Describes the tool and its parameters.

Tool Registry

Maps LLM tool names to actual Python functions.

Example:

TOOL_REGISTRY = {
    "get_current_weather": get_weather,
    "calculate": calculate,
}

# Tool Execution

The application executes the selected Python function.

# Tool Chaining

Output from one tool becomes input to another.

# Parallel Tool Calling

Independent tools can execute concurrently.

# Tool Result Formatting

All tools should return a consistent result structure.

# Error Handling

Tool failures should be captured and returned as structured errors.

# Authorization

User permissions must be checked before executing sensitive tools.

# Practical Test Commands

Activate the environment:

.venv\Scripts\activate

Run tool detection:

python -m tests.test_tool_detection

Run tool execution:

python -m tests.test_tool_execution

Run multi-turn tools:

python -m tests.test_multi_turn_tools

Run parallel tools:

python -m tests.test_parallel_tool_calls

Run web search:

python -m tests.test_web_search_complete

Run code execution:

python -m tests.test_code_execution_complete

Run database tool:

python -m tests.test_database_complete

Run file tool:

python -m tests.test_file_complete

Run email tool:

python -m tests.test_email_complete

Run calendar tool:

python -m tests.test_calendar_complete

Run web scraper:

python -m tests.test_web_scraper_complete

Run tool chaining:

python -m tests.test_tool_chaining

Run tool error handling:

python -m tests.test_tool_error_handling

Run tool result formatting:

python -m tests.test_tool_result_formatting

Run role-based access control:

python -m tests.test_tool_access_control

Run role-based tool execution:

python -m tests.test_role_based_tool_execution
Module 7 Final Architecture

At the end of Module 7, the complete architecture is:

                         USER
                           |
                           v
                    +-------------+
                    |     LLM     |
                    +-------------+
                           |
                           v
                  Tool Selection
                           |
                           v
                +-------------------+
                | Tool Definition   |
                +-------------------+
                           |
                           v
                Tool Name + Arguments
                           |
                           v
                +-------------------+
                | Tool Detection    |
                +-------------------+
                           |
                           v
                +-------------------+
                | Authorization     |
                +-------------------+
                           |
                           v
                +-------------------+
                | Input Validation  |
                +-------------------+
                           |
                           v
                +-------------------+
                | Tool Registry     |
                +-------------------+
                           |
                           v
                +-------------------+
                | Tool Execution    |
                +-------------------+
                           |
                  +--------+--------+
                  |                 |
               Success            Error
                  |                 |
                  v                 v
             Tool Result       Error Result
                  |                 |
                  +--------+--------+
                           |
                           v
                +-------------------+
                | Result Formatting |
                +-------------------+
                           |
                           v
                         LLM
                           |
                           v
                    Final Response

# Module 7 Summary

Module 7 demonstrated how to transform an LLM from a simple text-generation system into a system capable of interacting with external tools.

Tool Definitions
      ↓
Tool Selection
      ↓
Tool Calling
      ↓
Parameter Validation
      ↓
Tool Detection
      ↓
Tool Execution
      ↓
Tool Chaining
      ↓
Parallel Tool Calling
      ↓
Web Search
      ↓
Code Execution
      ↓
Database Access
      ↓
File Operations
      ↓
Email
      ↓
Calendar
      ↓
Web Scraping
      ↓
Error Handling
      ↓
Result Formatting
      ↓
Role-Based Authorization

# Author

**Ramesh Srinivasan**

Generative AI Cross-Skilling Journey