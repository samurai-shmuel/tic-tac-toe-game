# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:02:34 2020

@author: Samuel
"""

from IPython.display import clear_output

from numpy import random

def display_board(board):
    clear_output()
    print()
    print(board[7],' |',board[8],' |',board[9])
    print('--','|','--','|','--')
    print(board[4],' |',board[5],' |',board[6])
    print('--','|','--','|','--')
    print(board[1],' |',board[2],' |',board[3])

def player_desg():
    playlist = {'X':'', 'O':' '}
    playlist['X'] = input("Who's taking 'X'?: ")
    playlist['O'] = input("Who's taking 'O' then?: ")
    print("Players are", playlist['X'],"and", playlist['O'])
    return playlist
    
def win_check(board, mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
 
def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def choose_first(playlist):
    if random.randint(0, 1) == 0:
        return 'X'
    else:
        return 'O'

def replay():    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def player_choice(board):
    attack = int(input("Where do you put your mark?: "))
    if(space_check(board,attack)) and (attack in range(1,10)):
        return attack

print('Welcome to Tic Tac Toe!')

playlist = player_desg()
#while True:
choice = True
while choice:
    board = [' ' for i in range(0,10)]
    display_board(board)
    
    turn1= choose_first(playlist)
    if turn1=='X':
        turn2 ='O'
    elif turn1=='O':
        turn2 ='X'

# Set the game up here
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        #Player 1 Turn
        print(f"{playlist[turn1]}'s turn.")
        loc = int(player_choice(board))
        board[loc] = turn1
        display_board(board)
        if win_check(board, turn1):
            print(playlist[turn1], "wins")
            break
        if full_board_check(board):
            print("Draw")
            break
        
        # Player2's turn.
        print(f"{playlist[turn2]}'s turn.")
        loc = player_choice(board)
        board[loc] = turn2
        display_board(board)
        if win_check(board, turn2):
            print(playlist[turn2], "wins")
            break
            #pass
    
    choice = replay()
    if choice==0:
        break

    #if not replay():
        #break    

