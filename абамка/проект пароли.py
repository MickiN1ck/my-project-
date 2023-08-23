import random

print('Добро пожаловать в генератор паролей!')

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*+-=?'

number = int(input('Кол-во паролей:'))

length = int(input('Кол-во символов в пароле:'))

print('Пароли:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(symbols)
    print(passwords)