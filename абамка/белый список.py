white_list = set()
answers = set()

white_request = " "
request = " "

while white_request != "":
    white_request = input()
    if white_request:
        white_list.add(white_request)

while request != '':
    request = input()
    answers.add(request)


for answer in answers:
    if answer in white_list:
        print(answer)
