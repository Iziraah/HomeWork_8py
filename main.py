from enter import enter_adress, enter_person
from search import search

i = int(input('Что Вы желаете сделать?\
                1. Поиск? \
                2. Запись?\
                Ведите цифру: '))


if i ==1:
    search()
elif i == 2:
    enter_person()
    j = int(input('Может, еще и адрес добавим? 1 - да/ 2 - нет. Введите цифру:'))
    if j ==1:
        enter_adress()
    elif j ==2:
        print('А придется =)')
        enter_adress()
else: print('Некорректный ввод. попробуйте еще раз.')