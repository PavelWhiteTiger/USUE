class Person():
    def __init__(self, age, name, last_name):
        self.__age = age
        self.__last_name = last_name
        self.__name = name

    def get_last_name(self): return self.__last_name

    def set_last_name(self, fn):  self.last_name = fn

    def get_age(self): return self.__age

    def set_age(self, age): self.__age = age

    def get_name(self): return self.__name

    def set_name(self, name): self.__name = name

    def get_full_name(self): return self.__last_name + " " + self.__name

    def toString(self): return f"Name ={self.get_name()} LastName={self.get_last_name()} Age={self.get_age()}"


class Student(Person):
    def __init__(self, age, name, last_name, student_number):
        super().__init__(age, name, last_name)
        self.__student_number = student_number

    def get_student_number(self): return self.__student_number

    def set_student_number(self, student_number): self.__student_number = student_number


class Emploee(Person):
    def __init__(self, age, name, last_name, salary):
        super().__init__(age, name, last_name)
        self.__salary = salary

    def get_salary(self): return self.__salary

    def set_salary(self, salary): self.__salary = salary


man1 = Student(25, "Pasha", "Kozhanov", 3245345)
man2 = Emploee(32, "Dima", "Ivanov", 3245345)
man3 = Person(61, "Greesha", "Petrov")

mans = [man1, man2, man3];

for man in mans:
    print(man.get_full_name())
