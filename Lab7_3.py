import re

with open("./resources/input.txt", "r", ) as myFile:
    allText = myFile.readlines();
    letters = []
    for i in range(len(allText)):
        allText[i] = allText[i].strip()
        letters += list(filter(lambda x: x != " ", re.sub("\\.*'*-*:*,*«*»*\"*\\?*!*", "", allText[i])))

    words = []

    for i in range(len(allText)):
        words += allText[i].split(" ")

    print(f"{len(letters)} letters")
    print(f"{len(words)} words")
    print(f"{len(allText)} lines")
