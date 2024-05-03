with open("./resources/lab7_2.txt", "a+", ) as myFile:
    myFile.write(input("Введите запись"))
    myFile.write("\n")
    myFile.flush()
