from employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, title, manager=None, employees=[]):
        super().__init__(name, salary, title, manager)
        self.employees=employees

    def addEmployee(self, employee):
        self.employees.append(employee)

splinter = Manager('Splinter', 100000, 'Sensai')
Leo = Employee('Leonardo', 90000, 'Ninja', splinter)

splinter.addEmployee(Leo)
print(splinter.employees[0].name)
