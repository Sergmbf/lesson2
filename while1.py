"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

answer = str ('NO')
def ask_user(answer):
    """
    Замените pass на ваш код
    """
    while answer != 'Хорошо' :
      print(" Как дела? ")
      answer = str(input())

print ( ask_user(answer), ' Молодец! ')


