import random;


def randint():
    res = random.randint(1, 6)
    print("Вам выпало", res)
    if res == 3 or res == 4:
        return randint();
    if res == 1 or res == 2:
        return "Вы проиграли"
    return "Вы победили"


print(randint());
