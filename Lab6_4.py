tuple1 = (1, 2, 3);
tuple2 = (1, 8, 3, 4, 8, 8, 9, 2);
tuple3 = (1, 2, 8, 5, 1, 2, 9);


def getIndexInput(tupleInput, id, inputNumber):
    currentInput = 0;
    for i in range(len(tupleInput)):
        if id == tupleInput[i]:
            currentInput += 1;
            if currentInput == inputNumber:
                return i;

    return None;


def getTuple(tupleInput, id):
    firstInput = getIndexInput(tupleInput, id, 1);
    secondInput = getIndexInput(tupleInput, id, 2);
    if firstInput == None:
        return tuple();
    if secondInput == None or secondInput == len(tupleInput):
        return tupleInput[firstInput:];
    return tupleInput[firstInput:secondInput + 1];


print(getTuple(tuple1, 8));
print(getTuple(tuple2, 8));
print(getTuple(tuple3, 8));
