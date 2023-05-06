# Noughts and crosses 2 human players
# Checks that space is free and for winners

game_over = False
turn = 'X'
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


    
print_board()

while not game_over:
    print('Player',turn,'go:')
    while not valid_go:
        go = input()
        if go.isnumeric() and int(go) < 9 and board[int(go)] == '-':
            valid_go = True
    board[int(go)] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    go = ''
    valid_go = False
    count += 1
    print(count,'turns')
    print_board()
    check_board()

print('Game over!')
print('Winner is',winner)
