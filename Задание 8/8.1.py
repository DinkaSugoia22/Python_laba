class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def capitalize_first_letter(self, string):
        return string[0].upper()

    def get_initials(self):
        return self.capitalize_first_letter(self.name) + self.capitalize_first_letter(self.surname)


# Пример использования:
student = Student("eвдоким", "cмирнов",)
initials = student.get_initials()
print(initials)  
