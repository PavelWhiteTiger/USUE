# Тема 7. Работа с файлами (ввод, вывод) 
Отчет по Теме #7 выполнил(а):
- Кожанов Павел Дмитриевич
- ИНО ОЗБ ПОАС 22-1

| Задание       | Сам_раб |
| ------------- | ------- |
| Задание 1  -  | +       |
| Задание 2  -  | +       |
| Задание 3  -  | +       |
| Задание 4  -  | +       |
| Задание 5  -  | +       |


Работу проверили:
- к.э.н., доцент Панов М.А.

## Задание №1
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
import codecs
import re

words = dict();

with codecs.open("./resources/lab7_1.txt", "r", "utf_8_sig") as myFile:
    lines = list(filter(lambda x: x != "", [line.strip() for line in myFile.readlines()]))
    for line in lines:
        line = re.sub("\\.*'*-*:*,*«*»*\"*\\?*!*", "", line).split(" ")
        for word in line:
            words[word.lower()] = words.get(word.lower(), 0) + 1

words = dict(reversed(sorted(words.items(), key=lambda item: item[1]), ))

for key in words:
    print(f"{key} - {words[key]}")

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab7/pic/t1.png)

## Задание №2
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
with open("./resources/lab7_2.txt", "a+", ) as myFile:
    myFile.write(input("Введите запись"))
    myFile.write("\n")
    myFile.flush()

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab7/pic/t2.png)

## Задание №3
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
```python
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
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab7/pic/t3.png)

## Задание №4
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если
 
файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
-	Запрещенные слова:
hello email python the exam wor is

```python
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

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab7/pic/t4.png)

## Задание №5
5)	Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
```python
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

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab7/pic/t5.png)


