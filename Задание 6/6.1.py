class User:
	def show(self,name, surname, Salary ):
		return name + surname + Salary 
user = User()
print(user.show('Егор', ' Зобов', ' 20 000')) 