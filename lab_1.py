class EmployeeSystem:
    def __init__(self):
        self._employees=[]
    
    def add_employee(self,name,position,salary):
        employee={
            "name":name,
            "position":position,
            "salary":float(salary)
        }
        self._employees.append(employee)

    def display_employee(self):
        if len(self._employees) == 0:
            print("No employee records found.")
            return
        
        
