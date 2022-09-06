import Util.Move as Move
import numpy as np


def generate_start():
    chessGame = np.zeros((8, 8))
    # create starting position
    # Black Rooks
    chessGame[0, 0] = -5
    chessGame[0, 7] = -5

    # Black Knights
    chessGame[0, 1] = -3
    chessGame[0, 6] = -3

    # Black Bishops
    chessGame[0, 2] = -4
    chessGame[0, 5] = -4

    # Black King and Queen
    chessGame[0, 3] = -9
    chessGame[0, 4] = -10

    # Black Pawns
    chessGame[1, 0:8] = -1

    # White Rooks
    chessGame[7, 0] = 5
    chessGame[7, 7] = 5

    # White Knights
    chessGame[7, 1] = 3
    chessGame[7, 6] = 3

    # White Bishops
    chessGame[7, 2] = 4
    chessGame[7, 5] = 4

    # White King and Queen
    chessGame[7, 3] = 9
    chessGame[7, 4] = 10

    # White Pawns
    chessGame[6, 0:8] = 1

    return chessGame


def generate_position(mv,currentBoardState,fullGameArray,color):  # mv is the given move (ex: "d5"), currentBoardState is the current state of the game board,
                                                                  # fullGameArray is the current game array, color is the side making the move

    # White Move
    if color=='w' :
        if '=' in mv:
            Move.pawn(mv, currentBoardState, 1)
        elif 'O-O' in mv.strip():
            currentBoardState[7, 7] = 0
            currentBoardState[7, 6] = 10
            currentBoardState[7, 5] = 5
            currentBoardState[7, 4] = 0
        elif 'O-O-O' in mv.strip():
            currentBoardState[7, 0] = 0
            currentBoardState[7, 1] = 0
            currentBoardState[7, 2] = 10
            currentBoardState[7, 3] = 5
            currentBoardState[7, 4] = 0
        elif 'K' in mv:
            Move.king(mv, currentBoardState, 1)
        elif 'B' in mv:
            Move.bishop(mv, currentBoardState, 1)
        elif 'Q' in mv:
            Move.queen(mv, currentBoardState, 1)
        elif 'N' in mv:
            Move.knight(mv, currentBoardState, 1)
        elif 'R' in mv:
            Move.rook(mv, currentBoardState, 1)
        else:
            Move.pawn(mv, currentBoardState, 1)
        fullGameArray.append(currentBoardState.copy())
    else :
        # Black Move
        if '=' in mv:
            Move.pawn(mv, currentBoardState, -1)
        elif 'O-O' in mv.strip():
            currentBoardState[0, 7] = 0
            currentBoardState[0, 6] = -10
            currentBoardState[0, 5] = -5
            currentBoardState[0, 4] = 0
        elif 'O-O-O' in mv.strip():
            currentBoardState[0, 0] = 0
            currentBoardState[0, 1] = 0
            currentBoardState[0, 2] = -10
            currentBoardState[0, 3] = -5
            currentBoardState[0, 4] = 0
        elif 'K' in mv:
            Move.king(mv, currentBoardState, -1)
        elif 'B' in mv:
            Move.bishop(mv, currentBoardState, -1)
        elif 'Q' in mv:
            Move.queen(mv, currentBoardState, -1)
        elif 'N' in mv:
            Move.knight(mv, currentBoardState, -1)
        elif 'R' in mv:
            Move.rook(mv, currentBoardState, -1)
        else:
            Move.pawn(mv, currentBoardState, -1)
        fullGameArray.append(currentBoardState.copy())


def update_Move_List_String(chessBoard):
    legalMoves = chessBoard.legal_moves.__str__()
    i = 0
    while legalMoves[i] != '(':
        i += 1
    legalMoves = legalMoves.replace(",", "")
    legalMoves = legalMoves.replace("(", "")
    legalMoves = legalMoves.replace(")", "")
    legalMoves = legalMoves.replace(">", "")
    legalMoves = legalMoves[i:]

    flegalMoves = legalMoves.split(' ')
    return flegalMoves

