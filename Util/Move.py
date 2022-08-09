import numpy as np


def king(move, board, color):
    # print(move)
    indexes = np.where(board == (10 / color))
    captures = 1 if 'x' in move else 0
    move = move.strip('+')
    move = move.strip('#')
    move = move.replace('x', '')
    file = 0
    if 'b' in move:
        file = 1
    elif 'c' in move:
        file = 2
    elif 'd' in move:
        file = 3
    elif 'e' in move:
        file = 4
    elif 'f' in move:
        file = 5
    elif 'g' in move:
        file = 6
    elif 'h' in move:
        file = 7
    rank = 8 - (int(move[-1]))
    board[rank, file] = (10 / color)
    board[indexes[0], indexes[1]] = 0


def queen(move, board, color):
    # print(move)
    indexes = np.where(board == (9 / color))
    ranks = (indexes[0]).tolist()
    files = (indexes[1]).tolist()
    i = 0
    move = move.strip('+')
    move = move.strip('#')
    captures = 1 if 'x' in move else 0
    move = move.replace('x', '')
    file = 0
    rank = 0
    if move[-2] == 'b':
        file = 1
    elif move[-2] == 'c':
        file = 2
    elif move[-2] == 'd':
        file = 3
    elif move[-2] == 'e':
        file = 4
    elif move[-2] == 'f':
        file = 5
    elif move[-2] == 'g':
        file = 6
    elif move[-2] == 'h':
        file = 7
    rank = 8 - (int(move[-1]))
    rk = rank
    fl = file
    done = 0
    file = 0
    rank = 0
    if len(move) > 3:
        if move[1].isalpha():
            if move[1] == 'b':
                file = 1
            elif move[1] == 'c':
                file = 2
            elif move[1] == 'd':
                file = 3
            elif move[1] == 'e':
                file = 4
            elif move[1] == 'f':
                file = 5
            elif move[1] == 'g':
                file = 6
            elif move[1] == 'h':
                file = 7
            if len(move) == 5:
                rank = 8 - (int(move[2]))
                board[(rank, file)] = 0
            else:
                while i < len(ranks):
                    if int(files[i]) == file:
                        board[((int(ranks[i])), file)] = 0
                        break
                    else:
                        i += 1
        elif move[1].isdigit():
            while i < len(ranks):
                if int(ranks[i]) == int(move[1]):
                    board[int(ranks[i]), int(files[i])] = 0
                    break
                else:
                    i += 1
    else:

        done = 0
        f = fl - 1
        r = rk - 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r -= 1
                f -= 1

        f = fl + 1
        r = rk - 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r -= 1
                f += 1

        f = fl - 1
        r = rk + 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r += 1
                f -= 1
        f = fl + 1
        r = rk + 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r += 1
                f += 1

        f = fl - 1
        r = rk
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                f -= 1
        f = fl + 1
        r = rk
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                f += 1
        f = fl
        r = rk - 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r -= 1
        f = fl
        r = rk + 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (9 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r += 1

    board[rk, fl] = (9 / color)


def knight(move, board, color):
    # print(move)
    indexes = np.where(board == (3 / color))
    ranks = (indexes[0]).tolist()
    files = (indexes[1]).tolist()
    i = 0
    move = move.strip('+')
    move = move.strip('#')
    captures = 1 if 'x' in move else 0
    move = move.replace('x', '')
    file = 0
    rank = 0
    if move[-2] == 'b':
        file = 1
    elif move[-2] == 'c':
        file = 2
    elif move[-2] == 'd':
        file = 3
    elif move[-2] == 'e':
        file = 4
    elif move[-2] == 'f':
        file = 5
    elif move[-2] == 'g':
        file = 6
    elif move[-2] == 'h':
        file = 7
    rank = 8 - (int(move[-1]))
    rk = rank
    fl = file
    done = 0
    file = 0
    rank = 0

    if len(move) > 3:
        if move[1].isalpha():
            if move[1] == 'b':
                file = 1
            elif move[1] == 'c':
                file = 2
            elif move[1] == 'd':
                file = 3
            elif move[1] == 'e':
                file = 4
            elif move[1] == 'f':
                file = 5
            elif move[1] == 'g':
                file = 6
            elif move[1] == 'h':
                file = 7
            if len(move) == 5:
                rank = 8 - int(move[2])
                board[(rank, file)] = 0
            else:
                while i < len(ranks):
                    if int(files[i]) == file:
                        board[((int(ranks[i])), file)] = 0
                        break
                    else:
                        i += 1
        elif move[1].isdigit():
            while i < len(ranks):
                if int(ranks[i]) == int(move[1]):
                    board[int(ranks[i]), int(files[i])] = 0
                    break
                else:
                    i += 1
    else:
        file = fl - 1
        rank = rk + 2
        done = 0
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl + 1
        rank = rk + 2
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl - 2
        rank = rk + 1
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl - 2
        rank = rk - 1
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl - 1
        rank = rk - 2
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl + 1
        rank = rk - 2
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl + 2
        rank = rk - 1
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
        file = fl + 2
        rank = rk + 1
        if ((0 <= file <= 7) and (0 <= rank <= 7)) and done == 0:
            if board[rank, file] == (3 / color):
                board[rank, file] = 0
                done = 1
    board[rk, fl] = (3 / color)
    # print(move, ' Knight ', captures)


def bishop(move, board, color):
    # print(move)
    indexes = np.where(board == (4 / color))
    ranks = (indexes[0]).tolist()
    files = (indexes[1]).tolist()
    i = 0
    move = move.strip('+')
    move = move.strip('#')
    captures = 1 if 'x' in move else 0
    move = move.replace('x', '')
    file = 0
    rank = 0
    if move[-2] == 'b':
        file = 1
    elif move[-2] == 'c':
        file = 2
    elif move[-2] == 'd':
        file = 3
    elif move[-2] == 'e':
        file = 4
    elif move[-2] == 'f':
        file = 5
    elif move[-2] == 'g':
        file = 6
    elif move[-2] == 'h':
        file = 7
    rank = 8 - (int(move[-1]))
    rk = rank
    fl = file
    done = 0
    file = 0
    rank = 0
    if len(move) > 3:
        if move[1].isalpha():
            if move[1] == 'b':
                file = 1
            elif move[1] == 'c':
                file = 2
            elif move[1] == 'd':
                file = 3
            elif move[1] == 'e':
                file = 4
            elif move[1] == 'f':
                file = 5
            elif move[1] == 'g':
                file = 6
            elif move[1] == 'h':
                file = 7
            if len(move) == 5:
                rank = 8 - int(move[2])
                board[(rank, file)] = 0
            else:
                while i < len(ranks):
                    if int(files[i]) == file:
                        board[((int(ranks[i])), file)] = 0
                        break
                    else:
                        i += 1
        elif move[1].isdigit():
            while i < len(ranks):
                if int(ranks[i]) == (8 - int(move[1])):
                    board[int(ranks[i]), int(files[i])] = 0
                    break
                else:
                    i += 1
    else:
        done = 0
        f = fl - 1
        r = rk - 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (4 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r -= 1
                f -= 1
        f = fl + 1
        r = rk - 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (4 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r -= 1
                f += 1
        f = fl - 1
        r = rk + 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (4 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r += 1
                f -= 1

        f = fl + 1
        r = rk + 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (4 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r += 1
                f += 1

    board[rk, fl] = (4 / color)
    # print(move, ' Bishop ', captures)


def rook(move, board, color):
    # print(move)
    indexes = np.where(board == (5 / color))
    move = move.strip('+')
    move = move.strip('#')
    captures = 1 if 'x' in move else 0
    move = move.replace('x', '')

    indexes = np.where(board == (5 / color))
    ranks = (indexes[0]).tolist()
    files = (indexes[1]).tolist()
    i = 0

    file = 0
    rank = 0
    if move[-2] == 'b':
        file = 1
    elif move[-2] == 'c':
        file = 2
    elif move[-2] == 'd':
        file = 3
    elif move[-2] == 'e':
        file = 4
    elif move[-2] == 'f':
        file = 5
    elif move[-2] == 'g':
        file = 6
    elif move[-2] == 'h':
        file = 7
    rank = 8 - (int(move[-1]))
    rk = rank
    fl = file
    done = 0
    file = 0
    rank = 0
    if len(move) > 3:
        if move[1].isalpha():
            if move[1] == 'b':
                file = 1
            elif move[1] == 'c':
                file = 2
            elif move[1] == 'd':
                file = 3
            elif move[1] == 'e':
                file = 4
            elif move[1] == 'f':
                file = 5
            elif move[1] == 'g':
                file = 6
            elif move[1] == 'h':
                file = 7
            if len(move) == 5:
                rank = 8 - int(move[2])
                board[(rank, file)] = 0
            else:
                while i < len(ranks):
                    if int(files[i]) == file:
                        board[((int(ranks[i])), file)] = 0
                        break
                    else:
                        i += 1
        if move[1].isdigit():
            while i < len(ranks):
                if int(ranks[i]) == int(move[1]):
                    board[int(ranks[i]), int(files[i])] = 0
                    break
                else:
                    i += 1
    else:
        done = 0
        f = fl - 1
        r = rk
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (5 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                f -= 1

        f = fl + 1
        r = rk
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (5 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                f += 1

        f = fl
        r = rk - 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (5 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r -= 1

        f = fl
        r = rk + 1
        while ((0 <= f <= 7) and (0 <= r <= 7)) and done == 0:
            if board[r, f] == (5 / color):
                board[r, f] = 0
                done = 1
            elif board[r, f] != 0:
                break
            else:
                r += 1
    board[rk, fl] = (5 / color)


def pawn(move, board, color):
    # print(move)
    indexes = np.where(board == (1 / color))
    move = move.strip('+')
    move = move.strip('#')
    captures = 1 if 'x' in move else 0
    move = move.replace('x', '')
    file = 0
    moveValue = (1 / color)
    promotion = 1 if '=' in move else 0
    if promotion:
        if move[-1] == 'B':
            moveValue = 4 / color
        elif move[-1] == 'Q':
            moveValue = 9 / color
        elif move[-1] == 'R':
            moveValue = 5 / color
        elif move[-1] == 'N':
            moveValue = 3 / color
        move = move.replace(move[-1], '=')
        move = move.strip('=')
    rank = 8 - (int(move[-1]))
    rk = rank
    fl = file

    if captures:  # if a capture was made do this
        file0 = 0
        file1 = 0
        if move[0] == 'b':
            file0 = 1
        elif move[0] == 'c':
            file0 = 2
        elif move[0] == 'd':
            file0 = 3
        elif move[0] == 'e':
            file0 = 4
        elif move[0] == 'f':
            file0 = 5
        elif move[0] == 'g':
            file0 = 6
        elif move[0] == 'h':
            file0 = 7

        if move[1] == 'b':
            file1 = 1
        elif move[1] == 'c':
            file1 = 2
        elif move[1] == 'd':
            file1 = 3
        elif move[1] == 'e':
            file1 = 4
        elif move[1] == 'f':
            file1 = 5
        elif move[1] == 'g':
            file1 = 6
        elif move[1] == 'h':
            file1 = 7
        board[rk + color, file0] = 0  # remove pawn from old square
        fl = file1
        if board[rk, file1] == 0:  # if square the pawn is going to is zero, remove old pawn from next square down
            # file (en passant)
            board[rk + color, file1] = 0

    else:
        file = 0
        if move[0] == 'b':
            file = 1
        elif move[0] == 'c':
            file = 2
        elif move[0] == 'd':
            file = 3
        elif move[0] == 'e':
            file = 4
        elif move[0] == 'f':
            file = 5
        elif move[0] == 'g':
            file = 6
        elif move[0] == 'h':
            file = 7
        fl = file
        if not board[rk + color, fl] == 0:  # check for first move. if space behind pawn is any value other than zero,
            # set the square to zer0 (captures handled above).
            board[rk + color, fl] = 0
        else:
            board[rk + (2 * color), fl] = 0  # if space behind pawn is zero and captures is zero, then it must be the
            # first move and was moved up two squares

    board[rk, fl] = moveValue  # place piece at new square


def moveOne(mov, bd, color):
    if len(mov) < 2:
        return -1
    if color == 0:
        # White Move
        if '=' in mov:
            pawn(mov, bd, 1)
        elif "-" in mov and (len(mov.strip()) == 3):
            bd[7, 7] = 0
            bd[7, 6] = 10
            bd[7, 5] = 5
            bd[7, 4] = 0
        elif "-" in mov and (len(mov.strip()) > 3):
            bd[7, 0] = 0
            bd[7, 1] = 0
            bd[7, 2] = 10
            bd[7, 3] = 5
            bd[7, 4] = 0
        elif 'K' in mov:
            king(mov, bd, 1)
        elif 'B' in mov:
            bishop(mov, bd, 1)
        elif 'Q' in mov:
            queen(mov, bd, 1)
        elif 'N' in mov:
            knight(mov, bd, 1)
        elif 'R' in mov:
            rook(mov, bd, 1)
        else:
            pawn(mov, bd, 1)
        return

    # Black Move
    else:
        if '=' in mov:
            pawn(mov, bd, -1)
        elif "-" in mov and (len(mov.strip()) == 3):
            bd[0, 7] = 0
            bd[0, 6] = -10
            bd[0, 5] = -5
            bd[0, 4] = 0
        elif "-" in mov and (len(mov.strip()) > 3):
            bd[0, 0] = 0
            bd[0, 1] = 0
            bd[0, 2] = -10
            bd[0, 3] = -5
            bd[0, 4] = 0
        elif 'K' in mov:
            king(mov, bd, -1)
        elif 'B' in mov:
            bishop(mov, bd, -1)
        elif 'Q' in mov:
            queen(mov, bd, -1)
        elif 'N' in mov:
            knight(mov, bd, -1)
        elif 'R' in mov:
            rook(mov, bd, -1)
        else:
            pawn(mov, bd, -1)
        return
    return
