# Тема 5. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
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
При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.
```python
crazyString = input("Введите цифры разделенные пробелом")
listResult = list(filter(lambda x: x != " ", list(crazyString)))
tupleResult = tuple(listResult)
print(listResult)
print(tupleResult)
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab6/pic/t1.png)

## Задание №2
Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).
```python
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
tuple3 = (2, 4, 5, 5, 4, 2)


def newTuple(tuple1, number):
    listResult = list(tuple1);
    if number in listResult:
        listResult.remove(number);
    return tuple(listResult);


print(newTuple(tuple1, 1))
print(newTuple(tuple2, 3))
print(newTuple(tuple3, 9))
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab6/pic/t2.png)

## Задание №3
Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.
```python
import collections

def getDict(inputLong):
    myDict = {};
    for i in list(str(inputLong)):
        key = int(i)
        if key in myDict:
            myDict[key] = myDict[key] + 1
        else:
            myDict[key] = 1
    tmpTuples = sorted(myDict.items(), key=lambda kv: kv[1]);
    return  dict(tmpTuples[len(tmpTuples)-3:])


randomStr = 2352364573755467
randomStr2 = 735674567245263802194024

print(getDict(randomStr))
print(getDict(randomStr2))
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab6/pic/t3.png)

## Задание №4
Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.
Если элемента нет вовсе – вернуть пустой кортеж.
Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
```python
tuple1 = (1, 2, 3);
tuple2 = (1, 8, 3, 4, 8, 8, 9, 2);
tuple3 = (1, 2, 8, 5, 1, 2, 9);


def getIndexInput(tupleInput, id, inputNumber):
    currentInput = 0;
    for i in range(len(tupleInput)):
        if id == tupleInput[i]:
            currentInput += 1;
            if currentInput == inputNumber:
                return i;

    return None;


def getTuple(tupleInput, id):
    firstInput = getIndexInput(tupleInput, id, 1);
    secondInput = getIndexInput(tupleInput, id, 2);
    if firstInput == None:
        return tuple();
    if secondInput == None or secondInput == len(tupleInput):
        return tupleInput[firstInput:];
    return tupleInput[firstInput:secondInput + 1];


print(getTuple(tuple1, 8));
print(getTuple(tuple2, 8));
print(getTuple(tuple3, 8));
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab6/pic/t4.png)

## Задание №5
Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи
```python
import time
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
tuple2 = (3, 3, 56, 735, -12, 5, 8)
tuple3 = (1, 22, 3333, 4444, 55555, 666666, 7777777, 88888888, 999999999)


def getSummEverySquare(tupleIn):
    summ = 0;
    for i in tupleIn:
        summ += i ** 2

    return summ


print(getSummEverySquare(tuple1))
print(getSummEverySquare(tuple2))
print(getSummEverySquare(tuple3))
```
![Результат](https://github.com/PavelWhiteTiger/USUE/blob/lab5/pic/t5.png)

