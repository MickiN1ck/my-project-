commands = input('Команды: ')
ribbon = [0] * 5000
index = 0
maxValue = 255
minValue = 0

# Символы: ← →

if commands == '→':
    index += 1
elif commands == '←':
    index -= 1
elif commands == '+':
    ribbon += 1
elif commands == '-':
    ribbon += 1
elif commands == '.':


