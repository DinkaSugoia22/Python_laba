class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

employee = Employee("Зобов Егор", 17, 0)

print("Name:", employee.name)
print("Age:", employee.age)
print("Salary:", employee.salary)