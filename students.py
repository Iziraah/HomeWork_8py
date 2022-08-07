
# ФИО ученика
# год рождения
# класс
# место в классе (ряд, парта, вариант)
# статус по оценкам (отличник, ударник, троечник или двоечник)
# и другие данные, которые захочется хранить

import json

people_dict = \
    {1:
{
    'Lastname': 'Budilo',
    'Firstname': 'Anna',
    'Birthday': '12.01.1990',
    'Academic_performance': '4',
    'Class': '5a',
    'Status': 'student'
},
    2:
{
    'Lastname': 'Talashko',
    'Firstname': 'Mikhail',
    'Birthday': '18.05.1991',
    'Academic_performance': '3',
    'Class': '5a',
    'Status': 'student'
},
    3:
{
    'Lastname': 'Nickolaeva',
    'Firstname': 'Elena',
    'Birthday': '28.10.1990',
    'Academic_performance': '4',
    'Class': '5a',
    'Status': 'student'
},
    4:
{
    'Lastname': 'Nuzhdin',
    'Firstname': 'Evgenij',
    'Birthday': '29.04.1991',
    'Academic_performance': '2',
    'Class': '5a',
    'Status': 'student'
},
    5:
{
    'Lastname': 'Dubrovskiy',
    'Firstname': 'Sergey',
    'Birthday': '04.09.1990',
    'Academic_performance': '3',
    'Class': '5a',
    'Status': 'student'
},
    6:
{
    'Lastname': 'Dobrovolskaya',
    'Firstname': 'Svetlana',
    'Birthday': '09.01.1991',
    'Academic_performance': '5',
    'Class': '5b',
    'Status': 'student'
},
    7:
{
    'Lastname': 'Smelova',
    'Firstname': 'Irina',
    'Birthday': '13.10.1991',
    'Academic_performance': '5',
    'Class': '5b',
    'Status': 'student'
},
    8:
{
    'Lastname': 'Khorkov',
    'Firstname': 'Arkadiy',
    'Birthday': '24.06.1990',
    'Academic_performance': '3',
    'Class': '5b',
    'Status': 'student'
},
    9:
{
    'Lastname': 'Gilody',
    'Firstname': 'Evgenij',
    'Birthday': '26.09.1990',
    'Academic_performance': '3',
    'Class': '5b',
    'Status': 'student'
},
    10:
{
    'Lastname': 'Zhur',
    'Firstname': 'Aleksandr',
    'Birthday': '12.11.1991',
    'Academic_performance': '4',
    'Class': '5b',
    'Status': 'student'
},
    11:
{
    'Lastname': 'Loginova',
    'Firstname': 'Natalya',
    'Birthday': '10.07.1973',
    'Academic_performance': '-',
    'Class': '-',
    'Status': 'teacher'
},
    12:
{
    'Lastname': 'Bessudnova',
    'Firstname': 'Irina',
    'Birthday': '12.01.1969',
    'Academic_performance': '-',
    'Class': '-',
    'Status': 'teacher'
},
    13:
{
    'Lastname': 'Vinogradova',
    'Firstname': 'Tatyana',
    'Birthday': '22.05.1978',
    'Academic_performance': '-',
    'Class': '-',
    'Status': 'teacher'
}
    }

with open('people.json', 'w') as f:
        json.dump(people_dict, f, indent =3)
