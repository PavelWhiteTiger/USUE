import os

fileName = "./resources/" + input("Введите название файла") + ".txt"
openMode = "a+"
if os.path.exists(fileName):
    openFileMode = input("Вы хотите перезаписать файл (y/n)?")
    if openFileMode == "y":
        openMode = "w"

text = input("Введите текст")
with open(fileName, openMode) as f:
    f.write(text)
    f.flush()
