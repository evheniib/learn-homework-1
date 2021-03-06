"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():        
    chat_dict = {
        "Как дела?": "Хорошо!",
        "Что делаешь?": "Программирую"
    }
    quation = input("Спроси меня \n")
    while True:
        try:
            if quation in chat_dict:
                print(chat_dict[quation])
                quation = input("Хочешь спросить что-то еще? \n")
            else:
                quation = input("Такого вопроса нет, спроси что-то еще \n")
        except KeyboardInterrupt:
            print("Пока")
            break  

    
if __name__ == "__main__":
    ask_user()
