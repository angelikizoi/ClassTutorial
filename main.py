import datetime as dt

class Employee:
    # Class variables to track the number of employees and raise amount
    num_empl = 0
    raise_amount = 1.04  # Default raise amount (4%)

    def __init__(self, first, last, pay):
        # Instance variables for first name, last name, and salary
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_empl += 1  # Increment class variable for each new employee

    @property
    def email(self):
        # Automatically generate an email address from first and last names
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        # Return the full name of the employee
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # Apply a raise to the employee's salary using the class's raise amount
        self.pay = int(self.pay * self.raise_amount)

    def full_details(self):
        # Return a string containing the full details of the employee
        return "Employee Name: {}, Email: {}, Salary: {}".format(self.fullname, self.email, self.pay)

    @classmethod
    def set_raise_amount(cls, amount):
        # Class method to update the raise amount for all employees
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # Create an employee object from a string in the format "first-last-pay"
        try:
            first, last, pay = emp_str.split("-")
            return cls(first, last, int(pay))
        except ValueError:
            raise ValueError("String format should be 'First-Last-Pay'")

    @staticmethod
    def workday(day):
        # Static method to check if a day is a workday (Monday-Friday)
        if day.weekday() == 5 or day.weekday() == 6:  # 5 = Saturday, 6 = Sunday
            return False
        return True

    def __repr__(self):
        # Official string representation of the employee object (for debugging)
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        # Informal string representation of the employee object
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        # Define the behavior of the + operator for employees (sum of their salaries)
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        # Define the behavior of the len() function (length of the employee's full name)
        return len(self.fullname)


# Example usage
emp1 = Employee("Angeliki", "Zoi", 5000)
emp2 = Employee("George", "Nikolaou", 30000)

# Print basic details
print(emp1.fullname)  # Angeliki Zoi
print(emp2.email)     # George.Nikolaou@company.com

# Apply raise and print new salary
emp1.apply_raise()
print(emp1.pay)  # Increased salary after applying raise

# Change the raise amount for all employees
Employee.set_raise_amount(1.10)  # 10% raise
emp2.apply_raise()  # Applying new raise amount
print(emp2.pay)  # New salary after 10% raise

# Create an employee from a string
emp_str_3 = "Maria-Katerina-45000"
emp3 = Employee.from_string(emp_str_3)
print(emp3.full_details())  # Print full details of the new employee

# Check if a date is a workday
my_date = dt.date(2023, 7, 30)
print(Employee.workday(my_date))  # False (it's a Sunday)

# Demonstrating magic methods
print(emp1 + emp2)  # Sum of salaries of emp1 and emp2
print(len(emp3))    # Length of emp3's full name
