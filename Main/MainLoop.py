import os
import time
import chess as chs
import numpy as np


import Model.Model
from Util import GameTools as gt
from Util import Move, CreateTrainingData


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def createArrayFromPGN(bd, pos, currentGame):  # creates a game array using a single PGN string
    currentGame=currentGame.strip()
    color = 1
    for x in currentGame.split(' '):
        if (len(x) < 2) or ('.' in x) or ('-' in x) or (x.isdigit()):
            if (
                    'O' not in x):  # result at the end of the line has '-', keep going if the move is castling (
                # 'O'), otherwise skip it
                continue
        mv = x
        if color == 1:
            # White Move
            if '=' in mv:
                Move.pawn(mv, bd, color)
            elif 'O-O' in mv.strip():
                bd[7, 7] = 0
                bd[7, 6] = 10
                bd[7, 5] = 5
                bd[7, 4] = 0
            elif 'O-O-O' in mv.strip():
                bd[7, 0] = 0
                bd[7, 1] = 0
                bd[7, 2] = 10
                bd[7, 3] = 5
                bd[7, 4] = 0
            elif 'K' in mv:
                Move.king(mv, bd, color)
            elif 'B' in mv:
                Move.bishop(mv, bd, color)
            elif 'Q' in mv:
                Move.queen(mv, bd, color)
            elif 'N' in mv:
                Move.knight(mv, bd, color)
            elif 'R' in mv:
                Move.rook(mv, bd, color)
            else:
                Move.pawn(mv, bd, color)
            pos.append(bd.copy())
        if color == -1:
            # Black Move
            if '{' in mv:  # break loop if end of game line is reached (indicated by '{' in black move
                continue
            if '=' in mv:
                Move.pawn(mv, bd, color)
            elif 'O-O' in mv.strip():
                bd[0, 7] = 0
                bd[0, 6] = -10
                bd[0, 5] = -5
                bd[0, 4] = 0
            elif 'O-O-O' in mv.strip():
                bd[0, 0] = 0
                bd[0, 1] = 0
                bd[0, 2] = -10
                bd[0, 3] = -5
                bd[0, 4] = 0
            elif 'K' in mv:
                Move.king(mv, bd, color)
            elif 'B' in mv:
                Move.bishop(mv, bd, color)
            elif 'Q' in mv:
                Move.queen(mv, bd, color)
            elif 'N' in mv:
                Move.knight(mv, bd, color)
            elif 'R' in mv:
                Move.rook(mv, bd, color)
            else:
                Move.pawn(mv, bd, color)
            pos.append(bd.copy())

        color = color * -1  # swap color


def play(color):  # Play against model
    c = int(color)
    while c not in {-1, 1, 2}:
        cls()
        print("Invalid choice for color!")
        print("Which color would you like to play as?")
        print("1   Play as White")
        print("2   Play as Black")
        c = int(input())
    startPosition = gt.generate_start()
    gameArray = []
    gameArray.append(
        startPosition.copy())  # Append starting position to list of game's positions (it is always the first index)
    chessBoard = chs.Board()
    moveCount = 0
    gamePGN = ""  # keeps track of moves done in game. can be used to train model after ???
    moveColor=1 # always white first
    while (chessBoard.is_game_over() != 1):
        cls()
        print(chessBoard)
        currentLegalMoves = gt.update_Move_List_String(chessBoard)
        if (moveColor == int(color)):                            # get move from user input
            while (1):
                print("Legal Moves: "+str(currentLegalMoves))
                print("Enter your move: ")
                moveChosen=input()
                if moveChosen in currentLegalMoves :
                    chessBoard.push_san(moveChosen)
                    gamePGN = gamePGN + " " + moveChosen
                    createArrayFromPGN(startPosition, gameArray, gamePGN)
                    break
                else:
                    cls()
                    print(chessBoard)
                    print("Invalid move, try again. ")
        else :                                              # get move from model evaluation
            listOfValuations = [len(currentLegalMoves)]
            if (gamePGN!=""):                                       # if movesString is empty, then it is the first move, so no need to create array yet
                createArrayFromPGN(startPosition,gameArray,gamePGN)
            i = 0
            tensors = []
            for mv in currentLegalMoves:  # create an object for the model using each possible move and appending it to movesString
                tGame=gameArray.copy()          # copy current game array. will append possible position to it
                gt.generate_position(mv, np.asarray(tGame[-1].copy()), tGame, moveColor)
                #tGame[0]=CreateTrainingData.Convert(tGame)     # reuses code to create tensor for model. includes tensors for resulting positions for all possible moves
                tensors.append(tGame.copy())                # append to list of tenors
                i += 1
            e = 0
            tensors=CreateTrainingData.Convert(np.asarray(tensors))     # convert tensors
            moveChosenIndex = 0             # index for move model likes most
            bestEval = ""        # gauge model choices
            evalList = Model.Model.into_model(tensors, len(currentLegalMoves))
            while e<len(currentLegalMoves) :                        # loop through list of tensors and evaluate each one using model. choose move that results in a position with the lowest probability of an opponent win.
                eval=evalList[e]
                if (moveColor==1) :     # it is white's move, choose move that results in a position ith the lowest probability of an black win
                    if bestEval=="" :
                        bestEval=float(eval[2])
                        moveChosenIndex=e
                    elif (bestEval<float(eval[2])) :
                        bestEval=float(eval[2])
                        moveChosenIndex=e
                else :                  # it is black's move, choose move that results in a position ith the lowest probability of an white win
                    if bestEval=="" :
                        bestEval=float(eval[0])
                        moveChosenIndex=e
                    elif (bestEval<float(eval[0])) :
                        bestEval=float(eval[0])
                        moveChosenIndex=e
                e+=1
            print(str(currentLegalMoves[moveChosenIndex]))
            chessBoard.push_san(currentLegalMoves[moveChosenIndex])           ## push move to the chess game
            gamePGN = gamePGN + " " + currentLegalMoves[moveChosenIndex]  # record the chosen move on the movesString
            time.sleep(3)       # wait 3 seconds
        if moveColor==1:        # swap move color for next move
            moveColor=2
        else :
            moveColor=1
        moveCount+=1
    print(gamePGN)
    return chessBoard.result()


while (1):  # main loop. takes input from user
    print("Waiting for Input...")
    print("Options: ")
    print("1   Play against model.")
    print("2   Spectate model vs. model")
    print("3   Quit")
    i = input()
    if not (i.isdigit()) :
        cls()
        print("Invalid Input. Try again...")
    if int(i) == 3:  # quit app
        break
    elif int(i) == 1:
        # now, to clear the screen
        cls()
        print("Which color would you like to play as?")
        print("1   Play as White")
        print("2   Play as Black")
        play(input())
    elif int(i) == 2:
        cls()
        print(play(-1))
    else:
        cls()
        print("Invalid Input. Try again...")
print("Thanks for playing!")
