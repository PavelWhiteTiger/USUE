def reversedF(func):
    def wrapper(st):
        return str(func(st))[::-1];

    return wrapper


@reversedF
def concatingCopyUpperCase(st):
    st += str(st).upper()
    return st


@reversedF
def summMultyPow(in1):
    return in1 ** in1 * in1 + in1;


print(concatingCopyUpperCase("Привет"))
print(summMultyPow(2))
