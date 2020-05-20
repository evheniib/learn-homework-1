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
    switcher = True
    while switcher is True:
        user_str = input("Enter text")
        try:
            int(user_str)
        except ValueError:
            print("This is not a number, pls try again")
            continue
        else:
            user_age = int(user_str)
            print(f"So you are {user_age}`th years old!")
            check_age(user_age)
            switcher = False      
    return user_age
   
def check_age(age):
    """
    Вспомогательная функция для определения возраста
    """
    if age == 0:
        print("Thirstly you must to be born")
    elif age in range(1,7):
        print("Probably you are child in kindergarten")
    elif age in range(7, 16):
        print("You are student in school")
    else:
        print("In medival times after 16 years every human is adult")    

if __name__ == "__main__":
    main()
