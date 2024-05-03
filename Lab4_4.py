def getAbg(*args):
    argsCount = len(args);
    argsSum = 0;
    for i in range(argsCount):
        argsSum += args[i]
    return argsSum/argsCount;

abg = getAbg(1,2,3,4,5,6,7,8)
print(abg)