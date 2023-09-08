board = list(range(0, 9))
cells = 3
dashes = 13
spaces = 14

counter = 0
is_Win = False
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),(2, 4, 6)
)

player_token = ''

print('Tic-tac toe-the game for two players')

while not is_Win:
    for i in range(cells):
        print(' ' * spaces, end='')
        print('-' * dashes)
        print(' ' * spaces, end='')
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print(' ' * spaces, end='')
        print('-' * dashes)

    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    player_answer = input(f'Where we put a {player_token}?: ')
    player_answer = int(player_answer)

    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print('This cell is already taken.')
        continue

    counter += 1
    if counter > 4:
        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_Win = True
                break
        if is_Win:
            print(f'{player_token} is win!')
            for i in range(cells):
                print(' ' * spaces, end='')
                print('-' * dashes)
                print(' ' * spaces, end='')
                print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
                print(' ' * spaces, end='')
                print('-' * dashes)
            break
    if counter == 9:
        for i in range(cells):
            print(' ' * spaces, end='')
            print('-' * dashes)
            print(' ' * spaces, end='')
            print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
            print(' ' * spaces, end='')
            print('-' * dashes)
        print('Draw! You are amazing!')
        break