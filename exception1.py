"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


dict_for_meeting = {
  'Как дела?':'Хорошо!',
  'Что делаешь?':'Программирую!',
  'Еще вопросы есть?':'Нет'
  }
print(type(dict_for_meeting))


def ask_user_dict():
  
  # print(" первая точка ")      
  while True:
    try:
    # print(" вторая  точка ")
      print('Введите вопрос?')
      question = str(input())
      if question in dict_for_meeting != True: 
      # print('третья точка')
        print(dict_for_meeting[question])
      else:
        print('Неправильный вопрос')
    except KeyboardInterrupt:
      print('Пока!')
      break
  # print(dict_for_meeting['question'])
# print(ask_user_dict())
ask_user_dict()




