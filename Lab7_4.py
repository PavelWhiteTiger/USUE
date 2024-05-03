inputText = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
with open("./resources/input2.txt", "r", ) as myFile:
    words = myFile.read().split(" ");

uppercaseCharacters = []

for i in range(len(inputText)):
    if (inputText[i] == inputText[i].upper()):
        uppercaseCharacters.append(i)

for word in words:
    inputText = inputText.lower().replace(word, "*" * len(word))

inputText = list(inputText)

for ind in uppercaseCharacters:
    inputText[ind] = inputText[ind].upper()

inputText = str.join('', inputText)

print(uppercaseCharacters)
print(inputText)
