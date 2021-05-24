# DSA Project

# Project Title: Tic-tac-toe
#   GLOBAL VARIABLES 
board = [' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' '] 

move_record = [] #  stack to keep a record of turns of the two players
track_record = {'1':True, '2':True, '3':True, 
                '4':True, '5':True, '6':True, 
                '7':True,'8':True, '9':True} #  dictionary to keep a record of positions that have 
                                             #  already been marked
win = False #   bool variable which turns true in an event of victory
draw = False #   bool variable which turns true in an event of a draw
player1 = None #    name of player 1 
player2 = None #    name of player 2
player_1 = None #   sign of player 1
player_2 = None #   sign of player 2
player1_wins = 0 #  count of the wins of player 1
player2_wins = 0 #  count of the wins of player 2
turn = [] #  stack to make sure each player gets to take the FIRST turn in alternate matches
player =  None #    player who currently has their turn    

#   FUNCTIONS
def initialize(): #     to initialize the game
    global board, move_record, track_record, win, draw
    board = [' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']
    disp_board()
    move_record = []
    track_record = {'1':True, '2':True, '3':True, '4':True, '5':True, '6':True, '7':True,'8':True, '9':True}
    win = False
    draw = False

def push(stack, item):
    stack.append(item)
    return stack
def isEmpty(stack):
    if len(stack) < 1:
        return True
    return False
def top(stack):
    top = stack[len(stack)-1]
    return top

def names(): #  stores the name of each player
    global player1 
    global player2
    player1 = input("Name of Player 1: ")
    player2 = input("Name of Player 2: ")

def disp_board(): # displays the board
    global board
    print(' ' + board[0] + ' ' + '|' + ' ' +  board[1] + ' ' + '|' + ' ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' ' + '|' + ' ' +  board[4] + ' ' + '|' + ' ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' ' + '|' + ' ' +  board[7] + ' ' + '|' + ' ' + board[8]) 

def marks(): #  stores the mark of each player
    global player_1 
    global player_2
    print(player1, end = '')
    print(', choose from X and O, the mark you want for yourself, ', end = '')
    player_1 = input('1 for X and 2 for O: ')
    if player_1 == '1':
        player_1 = 'X'
        player_2 = 'O'    
    elif player_1 == '2':
        player_1 = 'O'
        player_2 = 'X'
    else:
        print('Warning! This input is invalid. Please try again')
        marks()

def current_player_sign(): #    return current player's mark
    global move_record 
    global player_1 
    global player_2
    global player
    global turn
    if isEmpty(turn) and isEmpty(move_record):
        push(turn, player_1)
        player = player_1
    elif isEmpty(move_record) and top(turn) == player_1:
        push(turn, player_2)
        player = player_2
    elif isEmpty(move_record) and top(turn) == player_2:
        push(turn, player_1)
        player = player_1
    else:
        if top(move_record) == player_2:
            player = player_1
        else:
            player =  player_2
    return player

def current_player_name(): #   returns current player's name 
    global track_record
    global player
    if player == player_1:
        return player1
    return player2

def input_mark(): #     asks for the position where current player wants to mark and stores in move_record
    global track_record
    global move_record
    cur_player = current_player_sign()
    curr_player =  current_player_name()
    correct = False
    while not correct:
        print(curr_player + "'s" + ' turn. ', end = '')
        print('Choose from 1 - 9, ', end = '')
        mark = input('the position in which you want to mark: ')
        if mark not in track_record.keys():
            print('Warning! This position is invalid, please try again!')
        elif track_record[mark] == False:
            print('Warning! This position has already been marked, please try again!') 
        else:
            track_record[mark] = False
            correct = True
    mark = int(mark) - 1
    board[mark] = cur_player
    push(move_record, cur_player)
    disp_board()

def check_win(): #  checks if there has been an event of a victory. If so, returns win as True
    check_row()
    check_column()
    check_diagonal()

def check_row():
    global win
    if (board[0] == board[1] == board[2] != ' ' or board[3] == board[4] == board[5] != ' ' or board[6] == board[7] == board[8] != ' '):
        win = True
    return win

def check_column():
    global win
    if (board[0] == board[3] == board[6] != ' ' or board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' '):
        win = True
    return win

def check_diagonal():
    global win
    if (board[0] == board[4] == board[8]!=' ') or (board[2] == board[4] == board[6]!=' '):
        win = True
    return win

def check_draw(): #  checks if there has been an event of a draw. If so, returns draw as True
    global draw
    global track_record
    win = check_win()
    if not win:
        for i in track_record:
            if track_record.get(i) == True:
                return draw
        draw = True
    return draw

def disp_scoreboard(): #    displays the scoreboard
    print("\t--------------------------")
    print("\t         SCOREBOARD       ")
    print("\t--------------------------")
 
    print("\t   " + str(player1) + ': ' + "\t    " + str(player1_wins))
    print("\t   " + str(player2) + ': ' + "\t    " + str(player2_wins))
 
    print("\t--------------------------\n")

def game():
    global win
    global draw
    global player1
    global player2
    global player1_wins
    global player2_wins
    global move_record
    names()
    disp_board()
    marks()
    while not win or not draw:
        input_mark()
        check_win()
        if win == True:
            winner = len(move_record)%2
            if winner == 0:
                player2_wins += 1
                print(player2, 'wins!')
            else:
                player1_wins += 1
                print(player1, 'wins!')
            disp_scoreboard()
            ask = input('Do you want to play again? Press 1 for Yes and 2 for No: ')
            if ask == '1':
                initialize()
            else:
                print('Thank you for playing! Hope you had a great time!')
                break
        check_draw()
        if draw == True:
            print("Match drawn")
            disp_scoreboard()
            ask = input('Do you want to play again? Press 1 for Yes and 2 for No: ')
            if ask == '1':
                initialize()
            else:
                print('Thank you for playing! Hope you had a great time!')
                break
    
game()