# Тема 5. Базовые коллекции: множества, списки 
Отчет по Теме #5 выполнил(а):
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
Ресторан на предприятии ведет учет посещений за неделю при помощи кода работника. У них есть список со всеми посещениями за неделю. Ваша задача почитать:
- Сколько было выдано чеков
- Сколько разных людей посетило ресторан
- Какой работник посетил ресторан больше всех раз Список выданных чеков за неделю:
```python
checks = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222,
          3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643,
          5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506,
          4506]
count = len(checks)
peopleCount = len(set(checks))
print("Check count =", count)
print("Count of different persons =", peopleCount)
mapPeople = {}
for i in checks:
    if i in mapPeople:
        countChecks = mapPeople[i]
        mapPeople[i] = countChecks + 1
    else:
        mapPeople[i] = 1

maxPeopeCount = 0
maxPeopeIndex = -1

for mapPerson in mapPeople:
    if mapPeople[mapPerson] > maxPeopeCount:
        maxPeopeCount = mapPeople[mapPerson]
        maxPeopeIndex = mapPerson

print(f"Больше всего посещений у {maxPeopeIndex}. Количество = {maxPeopeCount}")

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab5/pic/t1.png)

## Задание №2
На физкультуре студенты сдавали бег, у преподавателя физкультуры есть список всех результатов, ему нужно узнать
- Три лучшие результата
- Три худшие результата
- Все результаты начиная с 10 

```python
results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9,
           12.9, 37.4]
allResultOver10 = [x for x in results if str(x).startswith("10")]
threeBestResult = sorted(results)[-3:]
threeWorseResult = sorted(results)[:3]

print("3Best: ", threeBestResult)
print("3Worse: ", threeWorseResult)
print("Результаты начинающиеся с 10 =", allResultOver10)

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab5/pic/t2.png)

## Задание №3
Преподаватель по математике придумал странную задачку. У вас есть три списка с элементами, каждый элемент которых – длина стороны треугольника, ваша задача найти площади двух треугольников, составленные из максимальных и минимальных элементов полученных списков. Результатом выполнения задачи будет: листинг кода, и вывод в консоль, в котором будут указаны два этих значения.

Три списка:
 
one = [12, 25, 3, 48, 71]

two = [5, 18, 40, 62, 98]

three = [4, 21, 37, 56, 84]

```python
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]


def getTriangleArea(a, b, c):
    return (a * b * c) / 2;


minOne = min(one);
maxOne = max(one);
minTwo = min(two);
maxTwo = max(two);
minThree = min(three);
maxThree = max(three);

print(getTriangleArea(minOne, minTwo, minThree));
print(getTriangleArea(maxOne, maxTwo, maxThree));

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab5/pic/t3.png)

## Задание №4
Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все тройки заменить на четверки.
Списки оценок (проверить работу программы на всех трех вариантах): 
```python
var1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
var2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
var3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

exp = lambda inputList: list(map(lambda a: max(4, a), filter(lambda a: a != 2, inputList)))

print(exp(var1))
print(exp(var2))
print(exp(var3))

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab5/pic/t4.png)

## Задание №5
Вам предоставлены списки натуральных чисел, из них необходимо сформировать множества. При этом следует соблюдать это правило: если какое-либо число повторяется, то преобразовать его в строку по следующему образцу: например, если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка «44», строка
«444».
```python
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def getResult(listInput):
    mapResult = {}
    setResult = set();

    for i in listInput:
        if i in mapResult:
            countChecks = mapResult[i]
            mapResult[i] = countChecks + 1
            setResult.add(str(i) *  mapResult[i])
        else:
            mapResult[i] = 1
            setResult.add(str(i))

    return sorted(setResult)


print(getResult(list_1))
print(getResult(list_2))
print(getResult(list_3))

```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab5/pic/t5.png)

