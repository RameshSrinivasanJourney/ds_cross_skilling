from PythonBasics.learnDataTypes import salary

print("**********************************")
print("OBJECT ORIENTED PROGRAMMING (OOPS)")
print("**********************************")

print("\nClass and Object")
print("----------------")

class Employee:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name

    def display(self):
        print(self.employee_id)
        print(self.employee_name)


employeecb = Employee(
    1001,
    "Ramesh Srinivasan"
)

employeecb.display()


print("\nConstructor")
print("-----------")

class Employee:

    def __init__(self, employee_name):

        self.employee_name = employee_name

        print(
            f"{employee_name} object created."
        )

employeec = Employee("Ramesh")


print("\nInstance Variables")
print("------------------")

class Employee:

    def __init__(
            self,
            employee_id,
            employee_name,
            salary
    ):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display(self):

        print(f"ID      : {self.employee_id}")
        print(f"Name    : {self.employee_name}")
        print(f"Salary  : {self.salary}")


employeeiv = Employee(
    1001,
    "Ramesh Srinivasan",
    100000
)

employeeiv.display()


print("\nEncapsulation")
print("-------------")

class Employee:

    def __init__(self, salary):

        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary

employeee = Employee(
    100000
)

print(employeee.get_salary())

employeee.set_salary(120000)

print(employeee.get_salary())



print("\nInheritance")
print("-----------")

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name : {self.name}")

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")

employeei = Employee(
    1001,
    "Ramesh Srinivasan"
)

employeei.display_name()
employeei.display_employee()


print("\nPolymorphism")
print("-----------")

class Developer:
    def work(self):
        print("Developing Application")

class DataScientist:
    def work(self):
        print("Building Machine Learning Model")

employeep = [
    Developer(),
    DataScientist()
]


for employee in employeep:
    employee.work()


print("\nMethod Overriding")
print("-----------------")

class Person:

    def display_role(self):
        print("Person")


class Employee(Person):

    def display_role(self):
        print("Associate Architect")


personmo = Person()
personmo.display_role()

employeemo = Employee()
employeemo.display_role()

print("\nAbstraction")
print("-----------")

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_bonus(self):
        pass


class Architect(Employee):

    def calculate_bonus(self):
        return 25000


architect = Architect()

print(
    f"Bonus : {architect.calculate_bonus()}"
)


print("\nClass Variable - Shared by all objects")
print("--------------")
class Employee:

    company_name = "Ideas2IT"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Ramesh")
employee2 = Employee("John")

print(f"Name : {employee1.name} | Company Name : {employee1.company_name}")
print(f"Name : {employee2.name} | Company Name : {employee2.company_name}")



print("\nStatic Method - No object required")
print("----------------------------------")

class SalaryCalculator:

    @staticmethod
    def calculate_tax(salary):

        return salary * 0.10


tax = SalaryCalculator.calculate_tax(
    100000
)

print(f"Tax : {tax}")



print("\nEmployee Information")
print("--------------------")

class Employee_Information:

    company_name = "Ideas2IT"

    def __init__(
            self,
            employee_id,
            employee_name,
            salary
    ):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def calculate_bonus(self):

        return self.salary * 0.10

    def display(self):

        print(f"Employee ID : {self.employee_id}")
        print(f"Employee Name : {self.employee_name}")
        print(f"Salary : {self.salary}")
        print(f"Bonus : {self.calculate_bonus()}")


employeeinfo = Employee_Information(
    1001,
    "Ramesh Srinivasan",
    100000
)

employeeinfo.display()