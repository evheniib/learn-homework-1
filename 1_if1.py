"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную +
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать +
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную +
* Вывести содержимое переменной на экран +

"""

def main():
    """
    Основная функция которая принимает корректный возраст
    и возвращает результат в переменную
    """
    while True:
        user_age = input("Enter your age: ")
        try:
            user_age = int(user_age)
        except ValueError:
            print("This is not a number, pls try again")
            continue
        else:
            check_age(user_age)
            break    
    return user_age
   
def check_age(age):
    """
    Вспомогательная функция для определения возраста
    """
    if age == 0:
        print("Thirstly you must to be born")
    elif age>=1 and age<=7:
        print("Probably you are child in kindergarten")
    elif age>=7 and age<=16:
        print("You are student in school")
    else:
        print("In medival times after 16 years every human is adult")    

if __name__ == "__main__":
    main()
