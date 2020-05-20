"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов  +
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе. +_
* Посчитать и вывести средний балл по каждому классу. +

На слайде было еще два задания которые не описаны здесь. 
Их решение прикладываю в комментарий

"""

"""
numbers = [number for number in range(10)]
new_numbers = [number + 1 for number in numbers]
print(new_numbers)

user_input = input("\n Pls enter your text")
for letter in user_input:
    print(letter + "\n")
"""

def main():
    students = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '5a', 'scores': [4,4,4,1,2]},
        {'school_class': '6a', 'scores': [3,4,4,3,2]},
        {'school_class': '7a', 'scores': [3,2,4,5,5]},
        {'school_class': '8a', 'scores': [3,4,4,5,5]},
    ]
    total_summary = 0
    for s_class in students:
        s_class["summary"] = sum(s_class["scores"])
        total_summary += s_class["summary"] 
        print(f"The summary score in {s_class['school_class']} is {s_class['summary']}")

    print(f"The total summary is {total_summary}")
    
if __name__ == "__main__":
    main()
