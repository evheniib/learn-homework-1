"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки +
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0 +
* Если строки одинаковые, вернуть 1 +
* Если строки разные и первая длиннее, вернуть 2 +
* Если строки разные и вторая строка 'learn', возвращает 3 +
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты +

"""

def main(str1, str2):
    if type(str1) is str and type(str2) is str:
        if str1 == str2:
            return 1
        elif len(str1) > len(str2) and str2 != "learn":
            return 2
        elif str1 != str2 and str2 == "learn":
            return 3
    else:
        return 0
        raise ValueError("Your variables are not string")


test_var = [
    {"str1": "Hello world", "str2": "Hello world"},
    {"str1": "Hello my beautiful world!", "str2": "Hello world"},
    {"str1": "Hello my beautiful world!", "str2": "learn"},
    {"str1": 11111, "str2": "learn"},
]
    
if __name__ == "__main__":
    for i in test_var:
     result = main(i["str1"], i["str2"])
     print(" The result is {result} \n".format(result = result))
