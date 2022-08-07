
import json

adres_dict = \
    {1:
{
    'city': 'Snt. Petersburg',
    'street': 'Sofii Covalevskoj',
    'house': '16',
    'apartment': '4',
    'tel': '123456',
},
    2:
{
    'city': 'Snt. Petersburg',
    'street': 'Sofii Covalevskoj',
    'house': '1',
    'apartment': '26',
    'tel': '123789',
},
    3:
{
    'city': 'Snt. Petersburg',
    'street': 'Sofii Covalevskoj',
    'house': '12',
    'apartment': '49',
    'tel': '123159',
},
    4:
{
    'city': 'Snt. Petersburg',
    'street': 'Nauki',
    'house': '10',
    'apartment': '98',
    'tel': '123753',
},
    5:
{
    'city': 'Snt. Petersburg',
    'street': 'Grazhdanskij',
    'house': '36',
    'apartment': '85',
    'tel': '123852',
},
    6:
{
    'city': 'Snt. Petersburg',
    'street': 'Vernosty',
    'house': '3',
    'apartment': '105',
    'tel': '123698',
},
    7:
{
    'city': 'Snt. Petersburg',
    'street': 'Vernosty',
    'house': '14',
    'apartment': '135',
    'tel': '123874',
},
    8:
{
    'city': 'Snt. Petersburg',
    'street': 'Karpinskogo',
    'house': '29',
    'apartment': '56',
    'tel': '123524',
},
    9:
{
    'city': 'Snt. Petersburg',
    'street': 'Vavilovih',
    'house': '23',
    'apartment': '78',
    'tel': '123854',
},
    10:
{
    'city': 'Snt. Petersburg',
    'street': 'Severnij',
    'house': '105',
    'apartment': '457',
    'tel': '123378'
},
    11:
{
    'city': 'Snt. Petersburg',
    'street': 'Severnij',
    'house': '114',
    'apartment': '35',
    'tel': '785412'
},
    12:
{
    'city': 'Snt. Petersburg',
    'street': 'Rudneva',
    'house': '75/1',
    'apartment': '96',
    'tel': '785964'
},
    13:
{
    'city': 'Snt. Petersburg',
    'street': 'Lunacharskogo',
    'house': '98',
    'apartment': '404',
    'tel': '785478'
}
    }

with open('adress.json', 'w') as f:
        json.dump(adres_dict, f, indent =3)