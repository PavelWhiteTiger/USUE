tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
tuple3 = (2, 4, 5, 5, 4, 2)


def newTuple(tuple1, number):
    listResult = list(tuple1);
    if number in listResult:
        listResult.remove(number);
    return tuple(listResult);


print(newTuple(tuple1, 1))
print(newTuple(tuple2, 3))
print(newTuple(tuple3, 9))
