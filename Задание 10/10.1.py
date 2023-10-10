class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
employee1 = Employee("Саша Смирнов", 20, 666)

print(employee1.name)
print(employee1.age)    
print(employee1.salary)  
