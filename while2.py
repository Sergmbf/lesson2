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




print(" Здравствуйте! ")
dict_for_meeting = {
  'Как дела?':'Хорошо!',
  'Что делаешь?':'Программирую!',
  'Еще вопросы есть?':'Нет'
  }
print(type(dict_for_meeting))


def ask_user_dict():
  
  # print(" первая точка ")      
  while True:
    # print(" вторая  точка ")
    print('Введите вопрос?')
    question = str(input())
    if question in dict_for_meeting != True: 
      # print('третья точка')
      print(dict_for_meeting[question])
    else:
      print('Неправильный вопрос')
  print(dict_for_meeting['question'])
print(ask_user_dict())

