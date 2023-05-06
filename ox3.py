# Noughts and crosses.
# Can choose who goes first.
# Computer is a lot more clever.
from time import sleep

game_over = False
go = ''
valid_go = False
winner = 'Draw'
board = ['-','-','-','-','-','-','-','-','-']
count = 0

def print_board():
    for a in range(0, 8, 3):
        print(a,a+1,a+2,'  ',board[a],board[a+1],board[a+2])

def check_board():
    global game_over, winner
    # check rows
    for i in range(0, 8, 3):
        if board[i] == 'X' and board[i+1] == 'X' and board[i+2] == 'X':
            winner = 'X'
            game_over = True
    for i in range(0, 8, 3):
        if board[i] == 'O' and board[i+1] == 'O' and board[i+2] == 'O':
            winner = 'O'
            game_over = True
    # check columns
    for i in range(3):
        if board[i] == 'X' and board[i+3] == 'X' and board[i+6] == 'X':
            winner = 'X'
            game_over = True
        if board[i] == 'O' and board[i+3] == 'O' and board[i+6] == 'O':
            winner = 'O'
            game_over = True
    # check diagonals
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        winner = 'X'
        game_over = True
    if board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        winner = 'O'
        game_over = True
    if board[6] == 'X' and board[4] == 'X' and board[2] == 'X':
        winner = 'X'
        game_over = True
    if board[6] == 'O' and board[4] == 'O' and board[2] == 'O':
        winner = 'O'
        game_over = True
    # check for draw
    if count == 9:
        game_over = True

def choose_move():
    move_weight = []
    # scan for playable squares and set up move_weight array
    for i in range(9):
        if board[i] != '-':
            move_weight.append(0)
        else:
            move_weight.append(1)
            
    # scan rows
    for row in range(0, 7, 3):
        nought_count = 0
        cross_count = 0
        for i in range(row, row+3):
            if board[i] == 'O':
                nought_count += 1
            elif board[i] == 'X':
                cross_count += 1
            elif board[i] == '-':
                empty_square = i
        if nought_count == 2 and cross_count == 0:
            print('danger at',empty_square)
            move_weight[empty_square] = move_weight[empty_square] + 5
        elif nought_count == 0 and cross_count == 2:
            print('winning move at',empty_square)
            move_weight[empty_square] = move_weight[empty_square] + 6
        elif nought_count == 1 and cross_count == 0:
            move_weight[empty_square] = move_weight[empty_square] + 1
    # scan columns
    for column in range(3):
        nought_count = 0
        cross_count = 0
        for i in range(column, column+7, 3):
            if board[i] == 'O':
                nought_count += 1
            elif board[i] == 'X':
                cross_count += 1
            elif board[i] == '-':
                empty_square = i
        if nought_count == 2 and cross_count == 0:
            print('danger at',empty_square)
            move_weight[empty_square] = move_weight[empty_square] + 5
        elif nought_count == 0 and cross_count == 2:
            print('winning move at',empty_square)
            move_weight[empty_square] = move_weight[empty_square] + 6
        elif nought_count == 1 and cross_count == 0:
            move_weight[empty_square] = move_weight[empty_square] + 1

    # scan \ diagonal
    nought_count = 0
    cross_count = 0
    for i in range(0, 9, 4):
        if board[i] == 'O':
            nought_count += 1
        elif board[i] == 'X':
            cross_count += 1
        elif board[i] == '-':
            empty_square = i
    if nought_count == 2 and cross_count == 0:
        print('danger at',empty_square)
        move_weight[empty_square] = move_weight[empty_square] + 5
    elif nought_count == 0 and cross_count == 2:
        print('winning move at',empty_square)
        move_weight[empty_square] = move_weight[empty_square] + 6
    elif nought_count == 1 and cross_count == 0:
        move_weight[empty_square] = move_weight[empty_square] + 1

    # scan / diagonal
    nought_count = 0
    cross_count = 0
    for i in range(2, 7, 2):
        if board[i] == 'O':
            nought_count += 1
        elif board[i] == 'X':
            cross_count += 1
        elif board[i] == '-':
            empty_square = i
    if nought_count == 2 and cross_count == 0:
        print('danger at',empty_square)
        move_weight[empty_square] = move_weight[empty_square] + 5
    elif nought_count == 0 and cross_count == 2:
        print('winning move at',empty_square)
        move_weight[empty_square] = move_weight[empty_square] + 6
    elif nought_count == 1 and cross_count == 0:
        move_weight[empty_square] = move_weight[empty_square] + 1

    # choose best move
    print(move_weight)
    maxvalue = max(move_weight)
    best_move = move_weight.index(maxvalue)
    return(best_move)

while not valid_go:
    turn = input('Who plays first? Enter X for computer, O for human: ')
    if turn == 'X' or turn == 'O':
        valid_go = True

valid_go = False

print_board()
print()

while not game_over:
    if turn == 'O':
        print('Player',turn,'go:')
        while not valid_go:
            go = input()
            if go.isnumeric() and int(go) < 9 and board[int(go)] == '-':
                valid_go = True
        board[int(go)] = turn
        turn = 'X'
        go = ''
        valid_go = False
        count += 1
    else:
        print('Computer thinking...')
        sleep(1)
        board[choose_move()] = 'X'
        count += 1
        turn = 'O'
    print_board()
    print()
    check_board()

print('Game over!')
if winner == 'Draw':
    print('It\'s a draw')
else:
    print('Winner is',winner)
