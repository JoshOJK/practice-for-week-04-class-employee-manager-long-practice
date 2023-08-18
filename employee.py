class Employee:
    def __init__(self, name, salary, title, manager=None):
        self.name=name
        self.salary=salary
        self.title=title
        self.manager=manager


Leo = Employee('Leonardo', 90000, "Ninja")
print(Leo.salary)
