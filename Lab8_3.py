class Person():
    def __init__(self, age, name, last_name):
        self.age = age
        self.last_name = last_name
        self.name = name

    def getFullName(self): return f"{self.name} {self.last_name}"

    def toString(self): return f"Name ={self.name} LastName={self.last_name} Age={self.age}"


class Student(Person):
    def __init__(self, age, name, last_name, student_number):
        super().__init__(age, name, last_name)
        self.student_number = student_number


person1 = Student(25, "Pasha", "Kozhanov", 3245345)
print(person1.getFullName())
print(person1.toString())
print(person1.student_number)
