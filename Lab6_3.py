import collections

def getDict(inputLong):
    myDict = {};
    for i in list(str(inputLong)):
        key = int(i)
        if key in myDict:
            myDict[key] = myDict[key] + 1
        else:
            myDict[key] = 1
    tmpTuples = sorted(myDict.items(), key=lambda kv: kv[1]);
    return  dict(tmpTuples[len(tmpTuples)-3:])


randomStr = 2352364573755467
randomStr2 = 735674567245263802194024

print(getDict(randomStr))
print(getDict(randomStr2))
