#!/bin/python3

'''Tic Tac Toe'''

import random

def drawBoard(board):
    '''This function prints out the board'''

    '''Board is alist of 10 strings representing the board (ignore index 0'''
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    '''Lets the player type which letter they want to be'''
    '''Returns a list with the player's letter as the first item, and the computer's letter as the second'''
    letter = ''
    while not (letter == 'X' or letter == '0'):
        print('Do you want to be X or O)')
        letter = input().upper()

        '''the first element in the list is the player's letter, the second is the computer's letter.'''
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    '''Randomly choose the player who goes first.'''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    '''This functon returns True if the player wants to play again, otherwise it returns False.'''
    print('do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    '''Given a board and a player's letter, thisfunction returns True if the player has won.'''
    '''We use bo insyead of board and le insyead of letter so we don't have to type as much'''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or '''across the top'''
            (bo[1] == le and bo[2] == le and bo(3) == le) or '''across the bottom'''
            (bo[4] == le and bo[5] == le and bo(6) == le) or '''across the middle'''
            (bo[7] == le and bo[4] == le and bo[1] == le) or '''down the lef side'''
            (bo[8] == le and bo[5] == le and bo[2] == le) or '''down the middle'''
            (bo[9] == le and bo[6] == le and bo[3] == le) or '''down the right side'''
            (bo[7] == le and bo[5] == le and bo[3] == le) or '''diagonal'''
            (bo[9] == le and bo[5] == le and bo[1] == le)) '''diagonal'''

def getBoardCopy(board):
    '''Make a duplicate of the board list and return it the duplicate'''
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

        return dupeBoard

def isSpaceFree(board, move):
    '''Return true if the passed move is free on the passed board'''
    return board[move] == ' '

def getPlayerMove(board):
    '''let the player type in their move'''
    move = ' '
    while move not in ' 1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
        return int(move)

def chooseRandomMoveFromList(board, movesList):

    '''Returns a valid move from the passed list on the passed board.'''

    '''Returns None if there is no valid move.'''

    possibleMoves = []
    for i in movesList:

        if isSpaceFree(board, i):

            possibleMoves.append(i)

            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None

def getComputerMove(board, computerLetter):
    '''Given a board and the computer's letter, determine where to move and return that move'''
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):

        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
