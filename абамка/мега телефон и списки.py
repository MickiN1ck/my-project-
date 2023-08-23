book_phones = {
  'Квам-Дамн': '-79899899889',
  'Лук Скамворкер': '112',
  'Петард Вейпер': '1',
  'Лия Моргала': '+09998765432',
  'Эдуард Скамворкер': '0'
}

a = input('Выберите действие: ')

if a == '1':
    name = input()
    if name in book_phones:
        print(book_phones[name])
    else:
        print('Нет в телефонной книге')

if a == '2' or a == '3':
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    book_phones[name] = phone
    for key in book_phones:
        print(f'{key}: {book_phones[key]}')

if a == '4':
    del book_phones[input('Введите имя: ')]
    print('Контакт успешно удален.')
    for key in book_phones:
        print(f'{key}: {book_phones[key]}')