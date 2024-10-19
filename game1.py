# tictactose game
import random

Computer = '0'
plyr     = 'X'

a = [' '] * 10

def display_board(a):

    print(f'{a[1]} | {a[2]} | {a[3]}')
    print("_" * 10)
    print(f'{a[4]} | {a[5]} | {a[6]}')

    print("_" * 10)
    print(f'{a[7]} | {a[8]} | {a[9]}')
    print('-' * 10)
def check_win():
    if  a [1] == a [2] == a [3] and a [1]!=' ':
            return True
    elif a[4] == a [5] == a [6] and a [4]!=' ':
            return True
    elif a [7] == a [8] == a[9] and a [7]!=' ':
            return True
    elif a [1]== a [4]==a [7] and a [1]!=' ':
            return True
    elif a [2]== a [5]== a [8] and a [2]!=' ':
            return True
    elif a [3]== a[6]== a [9] and a [3]!=' ':
            return True
    elif a [1]==a [5]==a [9] and a [1]!=' ':
            return True
    elif a [7]== a [5]== a [3] and a [7]!=' ':
        return True
    else :
        return False
    
def Space(position):
    return True if a [position] == ' ' else False
# print("TRY AGAIN")

def insert(letter,position):
    if Space(position):
        a[position]= letter
        display_board(a)
        if check_win():
            if letter == 'X':
                print('Player win')
            else:
                print('Computer win')
                exit()
        
def human_move(letter):
    position = int(input("enter the position to inert:"))
    insert(letter,position)

def computer_move(letter):
    position = random.randint(1,9)
    insert(letter,position)

while not check_win():

    display_board(a)
    computer_move(Computer)
    human_move(plyr)
