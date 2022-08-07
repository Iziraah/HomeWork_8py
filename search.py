import json

def search():
    needKey=0
    search = input("Что искать будем? ")
    with open('people.json') as file:
        data_people = json.load(file)
    #print(data)
    for key, val in data_people.items():
        for k, v in val.items():
            if v == search:
                needKey = key
                print(f'Человек: {data_people[key]}')
    with open('adress.json') as file:
        data_adres = json.load(file)
    print(f'Адрес: {data_adres[needKey]}')
    with open('kabinet_uroki.json') as file:
        data_kabinet = json.load(file)
    for k1, v1 in data_kabinet.items():
        for k2, v2 in v1.items():
            for k3, v3 in v2.items():                
                for k4, v4 in v3.items():                    
                    for k5, v5 in v4.items():
                        if str(v5) == str(needKey):
                            print(f'Кабинет: {k1}, Предмет: {k2}, Ряд: {k3}, Парта: {k4}, Вариант: {k5}')
                            # print(k1,k2,k3,k4,k5)

    return
search()