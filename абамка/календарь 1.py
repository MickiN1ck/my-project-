months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
'Декабрь')

winter = months[-1:] + months[0:2]
spring = months[2:5]
summer = months[5:8]
autumn = months[8:11]

mon1, mon2, mon3 = winter

half_year1 = winter, spring
half_year2 = summer, autumn

print(mon1, mon2, mon3)

print(half_year1, half_year2)