# Тема 3. Операторы, условия, циклы.
Отчет по Теме #3 выполнил(а):
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
Напишите программу, которая преобразует 1 в 31.
Для выполнения поставленной задачи необходимо обязательно и только один раз использовать:
•	Цикл for
•	*= 5
•	+= 1
Никаких других действий или циклов использовать нельзя.
```python
varIntStart = 1;
for i in range(2) :
    varIntStart *= 5;
    varIntStart += 1;
print(varIntStart)
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t1.png)

## Задание №2
Напишите программу, которая фразу «Hello World» выводит в обратном порядке, и каждая буква находится в одной строке консоли. Пример вывода в консоль:
При этом необходимо обязательно использовать любой цикл, а также программа должна занимать не более 3 строк в редакторе кода.
```python
str = "Hello World!";
for i in range(len(str)-1, -1, -1):
    print(str[i])
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t2.png)

## Задание №3
Напишите программу, на вход которой поступает значение из консоли, оно должно быть числовым и в диапазоне от 0 до 10 включительно (это необходимо учесть в программе). Если вводимое число не подходит по требованиям, то необходимо вывести оповещение об этом в консоль и остановить программу. Код должен вычислять в каком диапазоне находится полученное число. Нужно учитывать три диапазона:
•	от 0 до 3 включительно
•	от 3 до 6
•	от 6 до 10 включительно
Результатом работы программы будет выведенный в консоль диапазон. Программа должна занимать не более 10 строчек в редакторе кода.
 
```python
intInput = int(input("Enter an integer: "))
if intInput < 0 or intInput > 10:
    print("Please enter an integer between 0 and 10")
elif intInput >= 0 and intInput <= 3:
    print("The integer between 0 and 3")
elif intInput > 3 and intInput < 6:
    print("The integer between 3 and 6")
elif intInput >= 6 and intInput <= 10:
    print("The integer between 6 and 10")
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t31.png)

![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t32.png)

![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t33.png)

![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t34.png)

## Задание №4
Манипулирование строками. Напишите программу на Python, которая принимает предложение (на английском) в качестве входных данных от пользователя. Выполните следующие операции и отобразите результаты:
•	Выведите длину предложения.
•	Переведите предложение в нижний регистр.
•	Подсчитайте количество гласных (a, e, i, o, u) в предложении.
•	Замените все слова "ugly" на "beauty".
•	Проверьте, начинается ли предложение с "The" и заканчивается ли на "end".
Проверьте работу программы минимум на 3 предложениях, чтобы охватить проверку всех поставленных условий.
```python
str = input("Введите предложение на английском")
letters = {"a", "e", "i", "o", "u", "y"};
print("Длинна предложения =", len(str));
count = 0;
for letter in str:
    if letter.lower() in letters:
        count += 1;
print("Количество глассных букв =", count);
newStr = str.lower().replace("ugly", "beauty");
print(newStr);
if (str.lower().startswith("the")):
    print("Строка начинается с the");
if (str.lower().endswith("end")):
    print("Строка заканчивается на end");
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t4.png)

## Задание №5
Составьте программу, результатом которой будет данный вывод в консоль:

Программу нужно составить из данных фрагментов кода:
Строки кода можно использовать только один раз. Не обязательно использовать все строки кода.
```python
counter = 0
values = [0, 2, 4, 6, 8, 10]
string = 'world'
while counter != 10:
    string = 'hello'
    if counter in values:
        string = string + ' world'
    print(string)
    counter += 1
while ' world' not in string:
    string = string + ' world'
    print(string)
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab3/pic/t5.png)


