class Person():
    def __init__(self, age, name, last_name):
        self.age = age
        self.last_name = last_name
        self.name = name


person1 = Person(25, "Pasha","Kozhanov")
print(person1.age)
print(person1.name)
print(person1.last_name)
