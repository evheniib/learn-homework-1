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
    chat_keys = list(chat_dict.keys())
    quation = input("Спроси меня \n")

    key = 0
    while key <= len(chat_keys):
        try:
            if quation == chat_keys[key]:
                print(chat_dict[quation])
                quation = input("Хочешь спросить что-то еще? \n")
                key = 0 
            else:
                key = key + 1
        except KeyboardInterrupt:
            print("Пока")
            break  

    
if __name__ == "__main__":
    ask_user()
