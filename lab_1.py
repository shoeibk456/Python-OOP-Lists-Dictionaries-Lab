# Employee Salary System

class EmployeeSystem:
    def __init__(self):
        # Private list to store employee records
        self.__employees = []

    # Add employee
    def add_employee(self, name, position, salary):
        employee = {
            "name": name,
            "position": position,
            "salary": float(salary)
        }
        self.__employees.append(employee)
        print("Employee added successfully.")

    # Display all employees
    def display_employees(self):
        if len(self.__employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for employee in self.__employees:
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary:", employee["salary"])
                print("--------------------")

    # Search employee by name
    def search_employee(self, name):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                print("\nEmployee Found:")
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary:", employee["salary"])
                return

        print("Employee not found.")

    # Increase employee salary
    def increase_salary(self, name, amount):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                employee["salary"] += amount
                print("Salary updated successfully.")
                print("New Salary:", employee["salary"])
                return

        print("Employee not found.")



system = EmployeeSystem()

# Add employees
num = int(input("How many employees do you want to add? "))

for i in range(num):
    print("Enter Employee", i + 1)

    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    system.add_employee(name, position, salary)

# Display all employees
print("All Employee Records")
system.display_employees()

# Search employee
search_name = input("Enter employee name to search: ")
system.search_employee(search_name)

# Increase salary
name = input("Enter employee name to increase salary: ")
amount = float(input("Enter salary increase amount: "))

system.increase_salary(name, amount)

# Display updated records
print("Updated Employee Records")
system.display_employees()