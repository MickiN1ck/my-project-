white_list = []
answers = []
while True:
    white_request = input('Разрешенный запрос: ')
    if white_request == '':
        break
    white_list.append(white_request)
while True:
    answers_request = input('Ваш запрос: ')
    if answers_request == '':
        break
    if answers_request in white_list:
        answers.append(answers_request)
for i in answers:
    print(f'{i}')
