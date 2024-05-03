def fib(n):
    f1, f2 = 0, 1
    for __ in range(n + 1):
        yield f1
        f1, f2 = f2, f1 + f2


fibonacci = fib(201);


for n in fibonacci:
    print(n)
