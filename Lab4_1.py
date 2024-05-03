#импортируем класс datetime из модуля datetime
from datetime import datetime
#импортируем метод sqrt из модуля math
from math import sqrt


def main(**kwargs):
    """
       Определяем функцию main
       :params kwargs: в аргументы кладется словарь
       Каждый элемент представляет пару ключ : значение
    """
    # Вычисление длины гипотенузы прямоугольного треугольника
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Вывод результата в консоль
        print(result)

    # Проверка, что скрпт запущен напрямую
if __name__ == '__main__':
    # запись стартового времени перед выполнением программы
    start_time = datetime.now()
    # Вызов функции main с передачей аргументов
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    # Подсчет времени выполнения
    time_costs = datetime.now() - start_time
    # Выводим время выполнения
    print(f"Время выолнения  - {time_costs}")
