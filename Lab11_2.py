import Lab11_1 as l1

with open("./resources/fib.txt", "a+") as f:
    for e in l1.fib(201):
        f.write(f"{str(e)}\n")
