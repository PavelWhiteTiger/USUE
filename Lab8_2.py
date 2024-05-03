class Person():
    def __init__(self, age, name, last_name):
        self.age = age
        self.last_name = last_name
        self.name = name

    def getFullName(self): return f"{self.name} {self.last_name}"

    def toString(self): return f"Name ={self.name} LastName={self.last_name} Age={self.age}"


person1 = Person(25, "Pasha", "Kozhanov")
print(person1.getFullName())
print(person1.toString())
