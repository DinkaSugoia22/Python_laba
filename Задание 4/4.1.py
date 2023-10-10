class Employee:
    def __init__(self):
        self.name = ''
        self.salary = 0

employee1 = Employee()
employee2 = Employee()
employee3 = Employee()

employee1.name = 'Евгений'
employee1.salary = 23000

employee2.name = 'Максим'
employee2.salary = 17000

employee3.name = 'Алиса'
employee3.salary = 22000

all_salary = (employee1.salary + employee2.salary + employee3.salary)

print('Сумма зарплат: ', all_salary)
