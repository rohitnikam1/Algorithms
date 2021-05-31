#! /home/rohit/anaconda3/envs/cs231n/bin/python3.7

# Tick-Tac-Toe Game
# Board is a 3*3 matrix with positions as follows

# 00 | 01 | 02 
#--------------
# 10 | 11 | 12  
#--------------
# 20 | 21 | 22 

#Please enter the board (matrix) index as shown above, to access the respective position.


import numpy as np

def board_positions():
    print(f"00 | 01 | 02")
    print(12*'-')
    print(f"10 | 11 | 12")
    print(12*'-')
    print(f"20 | 21 | 22")



def printboard(board):
    print(f"{board[0,0]} | {board[0,1]} | {board[0,2]}")
    print(12*'-')
    print(f"{board[1,0]} | {board[1,1]} | {board[1,2]}")
    print(12*'-')
    print(f"{board[2,0]} | {board[2,1]} | {board[2,2]}")



def check_win(board, turn):
    for i in range(N):
        if np.all(board[:,i] == turn) or np.all(board[i,:] == turn):
            return True
    if np.all(board.diagonal()==turn) or np.all(np.fliplr(board).diagonal()==turn):
        return True
    return False



def indices(n):
    lst = list(str(move))
    return int(lst[0]), int(lst[1])



if __name__ == "__main__":

    print('Please use the following index system to access respective positions.')
    board_positions()
    N = 3
    board = np.full((N,N), ' ')
    print('\n')
    printboard(board)

    turn = 'X'

    for i in range(N*N):
        print(f'Where to put {turn}?')
        move = input()
        i1, i2 = indices(move)
        while board[i1, i2] != ' ':
            print('Position already filled. Try other one.')
            move = input()
            i1, i2 = indices(move)
        board[i1, i2] = turn
        printboard(board)
        if check_win(board, turn):
            print(f'\n {turn} has won!')
            break
        elif i == N*N-1:
            print('Tied! Play again!')
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
