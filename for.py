"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
list_scores_school = [
  {'school_class':'4a','scores':[3,4,5,5,3,4,3]},
  {'school_class':'3b','scores':[5,5,5,5,5,5,5]},
  {'school_class':'7a','scores':[3,4,5,4,3,3,3]},
  {'school_class':'4b','scores':[5,5,5,5,5,4,5]},
  {'school_class':'5a','scores':[5,5,5,5,4,4,3]}
  ]



def scores_school_new():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    average_scores_school = 0
    sum_scores = 0
    sum_scores_school = 0
   
    for school_class in list_scores_school:
      for score in ['scores']:
        sum_scores += score  
      return sum_scores
    average_scores = sum_scores/ (len('scores'))
    print(school_class, average_scores )
    sum_scores_school += average_scores
    return sum_scores_school
  
  
    average_scores_school = sum_scores_school/len(list_scores_school)
    print('average_scores_school=', average_scores_school)  
    print (scores_school_new)
