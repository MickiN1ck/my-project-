book_phones = {
    'Квам-Дамн': '-79899899889',
    'Лук Скамворкер': '112',
    'Петард Вейпер': '1',
    'Лия Моргала': '+09998765432',
    'Эдуард Скамворкер': '0'
}

name = input()
phone = input()

if name != '' and phone != '':
    book_phones[name] = phone
    for key in book_phones:
        print(f'{key}: {book_phones[key]}')

elif name != '' and name in book_phones:
    print(book_phones[name])
else:
    print('Нет в телефонной книге')
