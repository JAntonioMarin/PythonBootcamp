# pip3 install IPython
# from IPython.display import clear_output
import os
import random

# Global variables
theBoard = [' '] * 10
available = [str(num) for num in range(0,10)]
players = [0,'X','O']

clear_terminal = lambda: os.system('clear')  # In windows is cls


def display_board(a,b):
    print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
          a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n  '+
          a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n  '+
          a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')


def display_board(a,b):
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')


def place_marker(avail,board,marker,position):
    board[position] = marker
    avail[position] = ' '


def win_check(board, mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or \
           (board[4] == mark and board[5] == mark and board[6] == mark) or \
           (board[7] == mark and board[8] == mark and board[9] == mark) or \
           (board[7] == mark and board[4] == mark and board[1] == mark) or \
           (board[8] == mark and board[5] == mark and board[2] == mark) or \
           (board[9] == mark and board[6] == mark and board[3] == mark) or \
           (board[7] == mark and board[5] == mark and board[3] == mark) or \
           (board[1] == mark and board[5] == mark and board[9] == mark)


def random_player():
    return random.choice((-1, 1))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def player_choice(board, player):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Player %s, choose your next position: (1-9) ' % (player)))
        except:
            print("I'm sorry, please try again.")

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    clear_terminal()
    print('Welcome to Tic Tac Toe!')

    toggle = random_player()
    player = players[toggle]
    print('For this round, Player %s will go first!' % (player))

    game_on = True
    input('Hit Enter to continue')
    while game_on:
        display_board(available, theBoard)
        position = player_choice(theBoard, player)
        place_marker(available, theBoard, player, position)

        if win_check(theBoard, player):
            display_board(available, theBoard)
            print('Congratulations! Player ' + player + ' wins!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available, theBoard)
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                clear_terminal()

    # reset the board and available moves list
    theBoard = [' '] * 10
    available = [str(num) for num in range(0, 10)]

    if not replay():
        break