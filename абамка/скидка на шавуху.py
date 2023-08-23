order_cost = 250 # стоимость заказа
discount_cost = 1 # множитель скидки. Если 1, то платят полную стоимость, если 0, то не платят ничего.

age = int(input("Введите свой возраст: "))

if age < 18:
    discount_cost = 0.05
if age < 30:
    discount_cost = 0.15
if age < 60:
    discount_cost = 0.25
if age < 100:
    discount_cost = 0.50

print("Стоимость заказа со скидкой:", order_cost * discount_cost)