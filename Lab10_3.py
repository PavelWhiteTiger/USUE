def sumTwoWithInput():
    try:
        personNumber = int(input("Enter a number: "))
        print(2 + personNumber)
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


sumTwoWithInput()
