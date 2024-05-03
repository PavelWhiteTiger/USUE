import time

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
tuple2 = (3, 3, 56, 735, -12, 5, 8)
tuple3 = (1, 22, 3333, 4444, 55555, 666666, 7777777, 88888888, 999999999)


def getSummEverySquare(tupleIn):
    summ = 0;
    for i in tupleIn:
        summ += i ** 2

    return summ


print(getSummEverySquare(tuple1))
print(getSummEverySquare(tuple2))
print(getSummEverySquare(tuple3))
