list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def getResult(listInput):
    mapResult = {}
    setResult = set();

    for i in listInput:
        if i in mapResult:
            countChecks = mapResult[i]
            mapResult[i] = countChecks + 1
            setResult.add(str(i) *  mapResult[i])
        else:
            mapResult[i] = 1
            setResult.add(str(i))

    return sorted(setResult)


print(getResult(list_1))
print(getResult(list_2))
print(getResult(list_3))
