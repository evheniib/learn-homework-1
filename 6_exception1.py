"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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
