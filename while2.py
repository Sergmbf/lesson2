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
question = str ('k') 
answer = str ('s')
dict1 = {question:answer}
# default = None
print (type(dict1))
dict1 = {'Как дела?':'Хорошо!','Что делаешь?':'Программирую!','Еще вопросы есть?':'Нет'}
# print(" Введите вопрос? ")
# question = str(input())
def ask_user_dict(dict1):
question = 'k'
  # answer = str ('s')
  print(type(question),' question ')
while dict1.question(question) != True:
  print(" Введите вопрос? ")      
  question = str(input())
else:
  print ('условие while не сработало')

print  (dict1.keys(question), ' Молодец! ') 