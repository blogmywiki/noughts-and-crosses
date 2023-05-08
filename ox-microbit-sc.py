# Noughts and crosses self-contained version
# which you can play just on the micro:bit
# Press A to go first, B for micro:bit to go first.
# Press B to step through possible play squares which blink.
# Press A to choose a square to play.
from microbit import *
import speech

game_over = False
go = ''
valid_go = False
winner = 'Draw'
board = ['-','-','-','-','-','-','-','-','-']
count = 0
led_lookup = {
    0: [0,0],
    1: [2,0],
    2: [4,0],
    3: [0,2],
    4: [2,2],
    5: [4,2],
    6: [0,4],
    7: [2,4],
    8: [4,4]
}

def print_board():
    for i in range(9):
        x = led_lookup[i][0]
        y = led_lookup[i][1]
        if board[i] == 'O':
            b = 9
        elif board[i] == 'X':
            b = 5
        else:
            b = 0
        display.set_pixel(x,y,b)
        

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

def first_free_square():
    for i in range(9):
        if board[i] == '-':
            free = i
            break
    return(free)

display.show(Image.DIAMOND)

speech.say('Press ay to go first')
sleep(1000)
speech.say('Press B for MEE to go first')

while not valid_go:
    if button_a.was_pressed():
        turn = 'O'
        display.show(Image('90909:'
                           '00000:'
                           '90909:'
                           '00000:'
                           '90909'))
        sleep(1000)
        valid_go = True
    elif button_b.was_pressed():
        turn = 'X'
        display.show(Image('50505:'
                           '00000:'
                           '50505:'
                           '00000:'
                           '50505'))
        sleep(1000)
        valid_go = True

valid_go = False
print_board()



while not game_over:
    if turn == 'O':
        choice = first_free_square()
        while not valid_go:
            x = led_lookup[choice][0]
            y = led_lookup[choice][1]
            display.set_pixel(x,y,9)
            sleep(500)
            display.set_pixel(x,y,0)
            sleep(500)
            if button_b.was_pressed():
                for i in range(choice,9):
                    choice += 1
                    if choice > 8:
                        choice = first_free_square()
                        break
                    if board[choice] == '-':
                        x = led_lookup[choice][0]
                        y = led_lookup[choice][1]
                        break
            if button_a.was_pressed():
                go = choice
                valid_go = True
        board[int(go)] = turn
        turn = 'X'
        go = ''
        valid_go = False
        count += 1
    else:
        sleep(1000)
        board[choose_move()] = 'X'
        count += 1
        turn = 'O'
    print_board()
    check_board()

speech.say('Game over!')
if winner == 'Draw':
    speech.say('Its a draw')
elif winner == 'X':
    speech.say('I win')
else:
    speech.say('You win')
