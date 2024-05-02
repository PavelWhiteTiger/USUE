# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Кожанов Павел Дмитриевич
- ИНО ОЗБ ПОАС 22-1

| Задание      | Сам_раб |
| ------------ | ------- |
| Задание 1    | +       |
| Задание 2    | +       |
| Задание 3    | +       |
| Задание 4    | +       |
| Задание 5    | +       |


Работу проверили:
- к.э.н., доцент Панов М.А.

## Задание №1
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Person():
    def __init__(self, age, name, last_name):
        self.age = age
        self.last_name = last_name
        self.name = name


person1 = Person(25, "Pasha","Kozhanov")
print(person1.age)
print(person1.name)
print(person1.last_name)

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab8/pic/t1.png)

## Задание №2
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab8/pic/t2.png)

## Задание №3
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab8/pic/t3.png)

## Задание №4
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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

    def get_full_name(self): return self.__last_name

    def toString(self): return f"Name ={self.get_name()} LastName={self.get_last_name()} Age={self.get_age()}"


class Student(Person):
    def __init__(self, age, name, last_name, student_number):
        super().__init__(age, name, last_name)
        self.__student_number = student_number

    def get_student_number(self): return self.__student_number

    def set_student_number(self, student_number): self.__student_number = student_number


person1 = Student(25, "Pasha", "Kozhanov", 3245345)
print(person1.get_last_name())
print(person1.get_age())
print(person1.get_student_number())
print(person1.get_full_name())
print(person1.toString())

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab8/pic/t4.png)

## Задание №5
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
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

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab8/pic/t5.png)

