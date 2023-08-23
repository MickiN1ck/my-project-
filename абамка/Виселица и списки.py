import os
import random

clear = lambda: os.system('clear')

print('Привет! Я загадал слово, твоя задача-угадать его по буквам.')
input('*НАЖМИ ENTER, ЧТОБЫ ПРОДОЛЖИТЬ*')

clear()

print('Поехали!')

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    print(letters)
    for symb in word:
        if symb in letters:
            print(symb, end = ' ')
        else:
            print('*', end = ' ')
            isWin = False
    print()

    if isWin:
        print('Ты угадал! Харооош!')
        break

    letter = input('Введите букву: ')
    letters.append(letter)

    if letter not in word:
        hp -= 1
        print(f'Осталось попыток: {hp}')

    if hp == 0:
        print('Ты проиграл! У тебя закончилось кол-во поп-иток.')