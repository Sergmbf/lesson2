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

def scores_school():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # average_score_class('school_class') = dict()
    sum_scores_school = 0
    for j in ['school_class']:
        sum_scores_school += sum_scores_school
        sum_scores_class('school_class') = 0 
        for i in ['scores']:
            sum_scores_class('school_class') += sum_scores_class('school_class')
        average_scores_class('school_class') = sum_scores_class('school_class')/ int(len('scores'))
        return average_scores_class('school_class')
    average_scores_school = sum_scores_school/ int(len('school_class'))
    return average_scores_school

print('average_score_class =', average_score_class('4a'))
print('average_scores_school =', average_scores_school )
