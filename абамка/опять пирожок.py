money = int(input())
if money >= 35:
    print('Оплата успешно прошла')
    money = money - 35
else:
    print('Недостаточно средств')

print("Осталось: ", money)