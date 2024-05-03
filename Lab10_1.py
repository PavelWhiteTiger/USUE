import time

def timer(func):
    def wrapper():
        start_time =time.time();
        func()
        print()
        print(f"{time.time()-start_time} second")
    return wrapper

@timer
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')


if __name__ == '__main__':
    fibonacci()