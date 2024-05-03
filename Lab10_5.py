class ManAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Введенный возраст: {self.age}. " \
               f"Возраст должен быть от {self.minage} до {self.maxage}"


class Man:
    def __init__(self, name, age):
        self.name = name
        minage = 1
        maxage = 120
        if minage < age < maxage:
            self.age = age
        else:
            raise ManAgeException(age, minage, maxage)


try:
    Dima = Man("Dima", 131)
except ManAgeException as e:
    print(e)

try:
    Leha = Man("Leha", -23)
except ManAgeException as e:
    print(e)
