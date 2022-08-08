import numpy as np
import Util.Move as Move


# gamesFile = open('C:/Stuff/cleaned_1.pgn', 'r')  # open the
# file containing the games. file must use .pgn format for chess games. Each game should be on its own line.
# dataSetDir = 'C:/Users/m00ki/PycharmProjects/Chess_ML/Data/'     # directory in which to save finished dataset

print(
    "Enter the full path to the file containing the PGN formatted games: ")  # file containing the games. file must
# use .pgn format for chess games. Each game should be on its own line.
gamesPath: str = input()

print(
    "Enter the path to the directory where you would like the game structures saved: ")  # Directory in which to save
# finished dataset. must contain sub folders below:
# White Win
# Black Win
# Draw
# Other
dataSetDir: str = input()

gamesFile = open(gamesPath, 'r')

currentGame = gamesFile.readline()  # get first line from file, get first game (each line is a list of moves in .PGN


# format)


def generate_positions(bd, pos):
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


board = np.zeros((8, 8))
# create starting position
# Black Rooks
board[0, 0] = -5
board[0, 7] = -5

# Black Knights
board[0, 1] = -3
board[0, 6] = -3

# Black Bishops
board[0, 2] = -4
board[0, 5] = -4

# Black King and Queen
board[0, 3] = -9
board[0, 4] = -10

# Black Pawns
board[1, 0:8] = -1

# White Rooks
board[7, 0] = 5
board[7, 7] = 5

# White Knights
board[7, 1] = 3
board[7, 6] = 3

# White Bishops
board[7, 2] = 4
board[7, 5] = 4

# White King and Queen
board[7, 3] = 9
board[7, 4] = 10

# White Pawns
board[6, 0:8] = 1

start = board.copy()
positions = []
moves = 0
print('Building Data Set . . .')
i = 0
maxLength = 0
blank = np.zeros((8, 8))
folder = ''
while currentGame:
    end = len(currentGame)
    if '*' in currentGame or currentGame == '\n' or end <= 30:
        currentGame = gamesFile.readline()  # get next game (line) from file
        continue
    currentGame = currentGame.replace("!", "")
    currentGame = currentGame.replace("?", "")
    currentGame = currentGame.replace("]", "")
    print('Games Done: ', i)
    currentGameResult = currentGame.split('-')  # gets the game result from the end of line
    board = start.copy()  # Chess starting position
    positions.append(start.copy())  # Append starting position to list of positions (it is always the first index)

    #   Get appropriate folder path for saving
    if '0' in currentGameResult[-1]:  # 1-0 = white wins
        folder = 'White Win/'
    elif '2' in currentGameResult[-1]:  # 1/2-1/2 = draw
        folder = 'Draw/'
    elif '1' in currentGameResult[-1]:  # 0-1 = black wins
        folder = 'Black Win/'
    else:
        folder = 'Other/'  # bad things happened

    generate_positions(board, positions)  # use moves to generate all positions reached during the current game
    positionCopy = np.asarray(positions.copy())  # convert list to ndarray for saving

    # ********************************** IMPLEMENT ROTATION HERE *********************************** #

    np.save((dataSetDir + folder + str(i)), positionCopy)  # save array to file
    positions.clear()  # clear list of positions for next game / iteration of loop
    currentGame = gamesFile.readline()  # get next game (line) from file
    i += 1  # iterate game counter
print('Games Done: ', i)

# save labels to file as well
gamesFile.close()

# need to change each g in games to be 3d array, rather than list of arrays.
