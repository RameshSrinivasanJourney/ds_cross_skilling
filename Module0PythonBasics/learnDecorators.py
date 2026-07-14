print("********************")
print("DECORATORS IN PYTHON")
print("********************")

print("\nFunctions As Objects")
print("--------------------")

def greet():

    print("Welcome To Data Science")

message = greet

message()



print("\nFunction Inside Function")
print("------------------------")

def outer():

    def inner():

        print("Inside Inner Function")

    inner()

outer()



print("\nReturning Function")
print("------------------")

def outer():

    def inner():

        print("Inside Inner Function")

    return inner

function_object = outer()

function_object()




print("\nBasic Decorator")
print("---------------")

def log_decorator(function):

    def wrapper():

        print("Logging Started")

        function()

        print("Logging Completed")

    return wrapper


def display_employee():

    print("Employee : Ramesh Srinivasan")

decorated_function = log_decorator(
    display_employee
)

decorated_function()




print("\nDecorator Using @")
print("-----------------")

def log_decorator(function):

    def wrapper():

        print("Logging Started")

        function()

        print("Logging Completed")

    return wrapper


@log_decorator
def display_employee():

    print("Employee : Ramesh Srinivasan")

display_employee()




print("\nDecorator With Arguments")
print("------------------------")

def log_decorator(function):

    def wrapper(employee_name):

        print("Logging Started")

        function(employee_name)

        print("Logging Completed")

    return wrapper


@log_decorator
def display_employee(employee_name):

    print(
        f"Employee Name : {employee_name}"
    )

display_employee(
    "Ramesh Srinivasan"
)





print("\nGeneric Decorator")
print("-----------------")

def log_decorator(function):

    def wrapper(*args, **kwargs):

        print("Logging Started")

        result = function(
            *args,
            **kwargs
        )

        print("Logging Completed")

        return result

    return wrapper


@log_decorator
def calculate_bonus(salary):

    return salary * 0.10

bonus = calculate_bonus(100000)

print(f"Bonus : {bonus}")



import time

print("\nExecution Time Decorator")
print("------------------------")

def timer(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(
            *args,
            **kwargs
        )

        end = time.time()

        print(
            f"Execution Time : "
            f"{end - start:.4f} Seconds"
        )

        return result

    return wrapper


@timer
def process_employees():

    time.sleep(2)

    print("Processing Employees")


process_employees()





print("\nAuthorization Decorator")
print("-----------------------")

def authorize(function):

    def wrapper(user_role):

        if user_role == "Admin":

            function(user_role)

        else:

            print("Access Denied")

    return wrapper


@authorize
def delete_employee(user_role):

    print(
        "Employee Deleted Successfully"
    )

delete_employee("Admin")
delete_employee("User")





print("\nEmployee Audit Example")
print("----------------------")

def audit(function):

    def wrapper(*args, **kwargs):

        print(
            "Audit Log Started"
        )

        result = function(
            *args,
            **kwargs
        )

        print(
            "Audit Log Completed"
        )

        return result

    return wrapper


@audit
def update_salary(
        employee_id,
        salary
):

    print(
        f"Employee {employee_id}"
        f" Salary Updated To "
        f"{salary}"
    )


update_salary(
    1001,
    120000
)




