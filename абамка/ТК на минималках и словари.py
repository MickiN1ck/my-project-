book_phones = {
    'Квам-Дамн': '-79899899889',
    'Лук Скамворкер': '112',
    'Петард Вейпер': '1',
    'Лия Моргала': '+09998765432',
    'Эдуард Скамворкер': '0',
}
a = input()
isVolue = a in book_phones
if isVolue:
    print(book_phones[a])
else:
    print('Неправильно набрано имя.')
