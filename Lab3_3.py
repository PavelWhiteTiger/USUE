intInput = int(input("Enter an integer: "))
if intInput < 0 or intInput > 10:
    print("Please enter an integer between 0 and 10")
elif intInput >= 0 and intInput <= 3:
    print("The integer between 0 and 3")
elif intInput > 3 and intInput < 6:
    print("The integer between 3 and 6")
elif intInput >= 6 and intInput <= 10:
    print("The integer between 6 and 10")

