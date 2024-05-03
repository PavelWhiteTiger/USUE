var1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
var2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
var3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

exp = lambda inputList: list(map(lambda a: max(4, a), filter(lambda a: a != 2, inputList)))

print(exp(var1))
print(exp(var2))
print(exp(var3))
