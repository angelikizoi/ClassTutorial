
# OOP Basics with Python - Classes Demonstration

## Introduction

This project demonstrates the **fundamentals of Object-Oriented Programming (OOP)** in Python using two independent examples: one for handling employee information and another for managing temperature conversion. Each file highlights key OOP principles such as class creation, properties, methods, and encapsulation.

- **`main.py`**: Demonstrates handling employee information, including name, salary, and email creation. It also showcases class methods, static methods, and magic methods like `__repr__`, `__str__`, `__add__`, and `__len__`.
- **`temperature.py`**: Focuses on temperature management, specifically implementing **getter** and **setter** methods using the `@property` decorator to control access to temperature values and enforce validation.

## Files

- **`main.py`**: A class (`Employee`) handling employee details and demonstrating multiple OOP concepts.
- **`temperature.py`**: A class (`Celsius`) demonstrating getter and setter methods to manage temperature conversions.

## Features

### 1. `main.py` - Employee Class

The `Employee` class encapsulates employee details and includes the following features:

- **Attributes**: 
  - `first`: First name of the employee.
  - `last`: Last name of the employee.
  - `pay`: Salary of the employee.
  
- **Methods**:
  - **`fullname`**: Returns the full name of the employee.
  - **`email`**: Generates an email address based on the employee's name.
  - **`apply_raise`**: Increases the employee's salary using a class-level raise percentage.
  - **`from_string`**: A class method to create an employee instance from a formatted string.
  
- **Magic Methods**:
  - `__repr__`: Provides an unambiguous string representation of the object.
  - `__str__`: Provides a user-friendly string representation.
  - `__add__`: Adds the salaries of two employees.
  - `__len__`: Returns the length of the employee's full name.
  
### 2. `temperature.py` - Celsius Class

The `Celsius` class demonstrates controlling the access to attributes using getter and setter methods:

- **Attributes**:
  - `temperature`: The temperature value (in Celsius), with validation.
  
- **Methods**:
  - **`to_fahrenheit`**: Converts the Celsius temperature to Fahrenheit.
  
- **Getter and Setter**:
  - The class uses the `@property` decorator to control access to the `temperature` attribute, ensuring that temperatures cannot be set below -275°C.

## Usage

### 1. `main.py` - Working with the Employee Class

- **Creating an Employee**:

  You can create an employee instance by passing the first name, last name, and salary:

  ```python
  emp1 = Employee("John", "Doe", 50000)
  print(emp1.fullname)  # John Doe
  print(emp1.email)     # John.Doe@company.com
  ```

- **Applying a Raise**:

  You can apply a raise to the employee's salary:

  ```python
  emp1.apply_raise()
  print(emp1.pay)  # New salary after the raise
  ```

- **Using Class Methods**:

  You can create an employee from a string:

  ```python
  emp_str = "Jane-Doe-60000"
  emp2 = Employee.from_string(emp_str)
  print(emp2.fullname)  # Jane Doe
  ```

### 2. `temperature.py` - Working with the Celsius Class

- **Creating a Celsius Object**:

  You can create an instance of `Celsius` with an initial temperature:

  ```python
  temp = Celsius(25)
  print(temp.temperature)  # 25
  ```
- Initialization (Celsius(25)):

The __init__ method is called, which invokes the temperature setter (self.temperature = temperature). It stores the value 25 in the private attribute _temperature.

- Accessing the temperature property (print(temp.temperature)):

When you access temp.temperature, the getter (@property) is called, which returns the value stored in _temperature.

- **Converting to Fahrenheit**:

  Convert the temperature to Fahrenheit:

  ```python
  print(temp.to_fahrenheit())  # 77.0
  ```
  
The to_fahrenheit method internally calls self.temperature, which triggers the getter before performing the calculation and returning the result.

- **Validating Temperature**:

  The `temperature` setter ensures no temperature below -275°C is allowed:

  ```python
  temp.temperature = -300  # Raises ValueError: "Temperature below -275 is not valid!"
  ```

## Concepts Demonstrated

### 1. **Encapsulation**:
Both classes demonstrate encapsulation by bundling data (attributes) and methods that operate on that data into single units (classes).

### 2. **Class Methods**:
The `Employee` class includes class methods such as `from_string`, which shows how to use the `@classmethod` decorator to create alternative constructors.

### 3. **Static Methods**:
In `main.py`, static methods like `workday` are used to provide utility functions that aren't tied to a specific instance of the class.

### 4. **Properties (Getters and Setters)**:
The `Celsius` class demonstrates how to use the `@property` decorator to implement getter and setter methods that control access to the temperature attribute and perform validation.

### 5. **Magic Methods**:
In `main.py`, magic methods like `__repr__`, `__str__`, `__add__`, and `__len__` are implemented to enhance the class's behavior with Python's built-in functions.


