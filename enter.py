import json

def enter_person():
    with open('people.json') as file:
        p_data = json.load(file)
    key = []
    for k in p_data:
        key.append(k[0])
        key_id = int(max(key)) + 1
    print(key_id)

    Firstname = input('Введите имя: ')
    Lastname = input('Введите фамилию: ')
    Birthday = input('Введите Дату Рождения: ')
    Academic_performance = input('Успеваемость: ')
    Class = input('Класс: ')
    Status = input('Статус: ')
    new_person = \
        {
            key_id:{
                'Lastname': Lastname,
                'Firstname': Firstname,
                'Birthday': Birthday,
                'Academic_performance': Academic_performance,
                'Class': Class,
                'Status': Status
            }
        }
    result = {**p_data,**new_person}
    with open('people.json', 'w') as f:
        json.dump(result, f, indent =3)
    return

def enter_adress():
    with open('adress.json') as file:
        a_data = json.load(file)
    key = []
    for k in a_data:
        key.append(k[0])
        key_id = int(max(key)) + 1
    print(key_id)

    city = input('Город: ')
    street = input('Улица: ')
    house = input('Дом: ')
    apartment = input('Квартира: ')
    tel = input('Номер телефона: ')
   
    new_adress = \
        {
            key_id:{
                'city': city,
                'street': street,
                'house': house,
                'apartment': apartment,
                'tel': tel,
            }
        }
    result = {**a_data,**new_adress}
    with open('adress.json', 'w') as f:
        json.dump(result, f, indent =3)
    return