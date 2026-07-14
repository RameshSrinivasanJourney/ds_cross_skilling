print("*****************")
print("LOGGING IN PYTHON")
print("*****************")

#Basic Logger
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application Started")
logging.warning("Salary Not Updated")
logging.error("Database Connection Failed")




#Log Levels
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")


#Custom Log Format
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Employee Created")
#2026-06-22 10:30:15,000 - INFO - Employee Created


'''
Common Format Variables

%(asctime)s     -> Time
%(levelname)s   -> Log Level
%(message)s     -> Actual Message
%(filename)s    -> File Name
%(funcName)s    -> Function Name
%(lineno)d      -> Line Number
'''

#Employee Example
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

employee_name = "Ramesh Srinivasan"

logging.info(
    f"Employee Created : {employee_name}"
)

logging.warning(
    "Salary Not Available"
)

logging.error(
    "Employee Not Found"
)

'''
2026-06-22 10:30:15 | INFO | Employee Created : Ramesh Srinivasan
2026-06-22 10:30:16 | WARNING | Salary Not Available
2026-06-22 10:30:17 | ERROR | Employee Not Found
'''

#Logging Inside Functions

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

def calculate_bonus(salary):

    logging.info(
        f"Calculating Bonus For Salary {salary}"
    )

    bonus = salary * 0.10

    logging.info(
        f"Bonus Calculated {bonus}"
    )

    return bonus

calculate_bonus(100000)

'''
INFO - Calculating Bonus For Salary 100000
INFO - Bonus Calculated 10000.0
'''


#Logging Exceptions
import logging

logging.basicConfig(level=logging.INFO)

try:

    employee_id = int(
        input("Enter Employee ID: ")
    )

except Exception as ex:

    logging.error(
        f"Error Occurred : {ex}"
    )


'''
Input - ABC
Output - ERROR:root:Error Occurred :
invalid literal for int()
'''


#Writing Logs To File
import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info(
    "Employee Created Successfully"
)

'''
employee.log
2026-06-22 10:30:15 | INFO | Employee Created Successfully
'''


#Employee Management Logging
import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def create_employee(
        employee_id,
        employee_name
):

    logging.info(
        f"Creating Employee : {employee_name}"
    )

    print(
        f"Employee Created : {employee_name}"
    )

create_employee(
    1001,
    "Ramesh Srinivasan"
)

'''
Employee Created : Ramesh Srinivasan
'''

#Logger Object
import logging

logger = logging.getLogger("EmployeeLogger")

logging.basicConfig(
    level=logging.INFO
)

logger.info(
    "Employee Created"
)

logger.warning(
    "Salary Missing"
)

'''
INFO:EmployeeLogger:Employee Created
WARNING:EmployeeLogger:Salary Missing
'''


print("\nEmployee Management Logging")
print("=============================")

import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("EmployeeSystem")

def create_employee(
        employee_id,
        employee_name,
        salary
):

    logger.info(
        f"Creating Employee {employee_name}"
    )

    print(f"Employee ID   : {employee_id}")
    print(f"Employee Name : {employee_name}")
    print(f"Salary        : {salary}")

    logger.info(
        f"Employee Created Successfully"
    )

try:

    create_employee(
        1001,
        "Ramesh Srinivasan",
        100000
    )

except Exception as ex:

    logger.error(
        f"Error : {ex}"
    )


'''
Sample employee.log
2026-06-22 10:30:15 | INFO | Creating Employee Ramesh Srinivasan
2026-06-22 10:30:16 | INFO | Employee Created Successfully
'''