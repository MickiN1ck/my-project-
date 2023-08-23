recipe = []
while True:
    a = input('')
    if a == '':
        break
    else:
        recipe.append(a)
    if a == 'лук':
        recipe.pop()
print(recipe)
