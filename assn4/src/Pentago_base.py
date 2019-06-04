# ---------------------------------------------------------------------------
# Pentago
# This program is designed to play Pentago, using lookahead and board
# heuristics.  It will allow the user to play a game against the machine, or
# allow the machine to play against itself for purposes of learning to
#  improve its play.  All 'learning'code has been removed from this program.
#
# Pentago is a 2-player game played on a 6x6 grid subdivided into four
# 3x3 subgrids.  The game begins with an empty grid.  On each turn, a player
# places a token in an empty slot on the grid, then rotates one of the
# subgrids either clockwise or counter-clockwise.  Each player attempts to
# be the first to get 5 of their own tokens in a row, either horizontally,
# vertically, or diagonally.
#
# The board is represented by a matrix with extra rows and columns forming a
# boundary to the playing grid.  Squares in the playing grid can be occupied
# by either 'X', 'O', or 'Empty' spaces.  The extra elements are filled with
# 'Out of Bounds' squares, which makes some of the computations simpler.
#
# JL Popyack, ported to Python, May 2019
#   This is a program shell that leaves implementation of miniMax, win,
#   and heuristics to the student.
# ---------------------------------------------------------------------------

# from __future__ import print_function
import random
from random import randrange
import copy
import re
from amr439_h import *

BOARD_SIZE = 6
GRID_SIZE = 3
GRID_ELEMENTS = GRID_SIZE * GRID_SIZE
INFINITY = 10000


def initBoard():
    # ---------------------------------------------------------------------------
    # Initialize Pentago game board.
    # ---------------------------------------------------------------------------
    board = [['.' for col in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]
    return board


#	for i in range(BOARD_SIZE):
#		for j in range(BOARD_SIZE):
#			board[i][j] = '.'


def showBoard(board):
    # ---------------------------------------------------------------------------
    # Prints Pentago game board.
    # ---------------------------------------------------------------------------
    print("+-----+-----+")
    for offset in range(0, BOARD_SIZE, GRID_SIZE):
        for i in range(0 + offset, GRID_SIZE + offset):
            print("|", end='')
            for j in range(0, GRID_SIZE):
                print(board[i][j], end='')
                if (j < GRID_SIZE - 1):
                    print(" ", end='')
            print("|", end='')
            for j in range(GRID_SIZE, BOARD_SIZE):
                print(board[i][j], end='')
                if (j < BOARD_SIZE - 1):
                    print(" ", end='')
            print("|")
        print("+-----+-----+")


def getMoves(player, board):
    # ---------------------------------------------------------------------------
    # Determines all legal moves for player with current board,
    # and returns them in moveList.
    # ---------------------------------------------------------------------------
    moveList = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == '.':
                # ---------------------------------------------------------------
                #  For each empty cell on the grid, determine its block (1..4)
                #  and position (1..9)  (1..GRID_SIZE^2)
                # ---------------------------------------------------------------
                gameBlock = (i // GRID_SIZE) * 2 + (j // GRID_SIZE) + 1
                position = (i % GRID_SIZE) * GRID_SIZE + (j % GRID_SIZE) + 1
                pos = str(gameBlock) + "/" + str(position) + " "
                # ---------------------------------------------------------------
                #  For each block, can place a token in the given cell and
                #  rotate the block either left or right.
                # ---------------------------------------------------------------
                for k in range(4):  # (BOARD_SIZE//GRID_SIZE)^2
                    block = str(k + 1)
                    moveList.append(pos + block + "L")
                    moveList.append(pos + block + "R")

    return moveList


def getHumanMove(player, board):
    # ---------------------------------------------------------------------------
    # If the opponent is a human, the user is prompted to input a legal move.
    # Determine the set of all legal moves, then check input move against it.
    # ---------------------------------------------------------------------------
    moveList = getMoves(player, board)
    move = None

    ValidMove = False
    while (not ValidMove):
        hMove = input('Input your move (block/position block-to-rotate direction): ')

        for move in moveList:
            if move == hMove:
                ValidMove = True
                break

        if (not ValidMove):
            print('Invalid move.  ')

    return hMove


def rotateLeft(board, gameBlock):
    # ---------------------------------------------------------------------------
    # Rotate gameBlock counter-clockwise.  gameBlock is in [1..4].
    # ---------------------------------------------------------------------------
    rotLeft = copy.deepcopy(board)

    rowOffset = ((gameBlock - 1) // 2) * GRID_SIZE
    colOffset = ((gameBlock - 1) % 2) * GRID_SIZE
    for i in range(0 + rowOffset, GRID_SIZE + rowOffset):
        for j in range(0 + colOffset, GRID_SIZE + colOffset):
            rotLeft[2 - j + rowOffset + colOffset][i - rowOffset + colOffset] = board[i][j]

    return rotLeft


def rotateRight(board, gameBlock):
    # ---------------------------------------------------------------------------
    # Rotate gameBlock clockwise.  gameBlock is in [1..4].
    # ---------------------------------------------------------------------------
    rotRight = copy.deepcopy(board)

    rowOffset = ((gameBlock - 1) // 2) * GRID_SIZE
    colOffset = ((gameBlock - 1) % 2) * GRID_SIZE
    for i in range(0 + rowOffset, GRID_SIZE + rowOffset):
        for j in range(0 + colOffset, GRID_SIZE + colOffset):
            rotRight[j + rowOffset - colOffset][2 - i + rowOffset + colOffset] = board[i][j]

    return rotRight


def applyMove(board, move, player):
    # ---------------------------------------------------------------------------
    # Perform the given move, and update board.
    # ---------------------------------------------------------------------------

    newBoard = copy.deepcopy(board)
    gameBlock = int(move[0])
    position = int(move[2])
    rotBlock = int(move[4])
    direction = move[5]

    i = (position - 1) // GRID_SIZE + GRID_SIZE * ((gameBlock - 1) // 2);
    j = ((position - 1) % GRID_SIZE) + GRID_SIZE * ((gameBlock - 1) % 2);
    newBoard[i][j] = player

    if (direction == 'r' or direction == 'R'):
        newBoard = rotateRight(newBoard, rotBlock);
    else:  # direction=='l' or direction=='L'
        newBoard = rotateLeft(newBoard, rotBlock);

    return newBoard


def win(player, board):
    # ---------------------------------------------------------------------------
    # Determines if player has won, by finding '5 in a row'.
    # Student code needed here.
    # ---------------------------------------------------------------------------
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] is player:

                # right horizontal
                ti = i
                tj = j + 4
                if not (ti >= len(board) or tj >= len(board[j])):
                    if board[ti][tj] is player:
                        viable = True
                        while tj is not j and viable:
                            if board[ti][tj] is not player:
                                viable = False
                            tj = tj - 1

                        if viable:
                            return True

                # down vertical
                ti = i + 4
                tj = j
                if not (ti >= len(board) or tj >= len(board[j])):
                    if board[ti][tj] is player:
                        viable = True
                        while ti is not i and viable:
                            if board[ti][tj] is not player:
                                viable = False
                            ti = ti - 1
                        
                        if viable:
                            return True
                
                # down-right diagonal
                ti = i + 4
                tj = j + 4
                if not (ti >= len(board) or tj >= len(board[j])):
                    if board[ti][tj] is player:
                        viable = True
                        while ti is not i and tj is not j and viable:
                            if board[ti][tj] is not player:
                                viable = False
                            ti = ti - 1
                            tj = tj - 1
                        
                        if viable:
                            return True
                
                # down-left diagonal
                ti = i + 4
                tj = j - 4
                if not (ti >= len(board) or tj >= len(board[j])):
                    if board[ti][tj] is player:
                        viable = True
                        while ti is not i and tj is not j and viable:
                            if board[ti][tj] is not player:
                                viable = False
                            ti = ti - 1
                            tj = tj + 1
                        
                        if viable:
                            return True
                
                # # left horizontal
                # ti = i
                # tj = j - 4
                # if not (ti >= len(board) or tj >= len(board[j])):
                #     if board[ti][tj] is player:
                #         viable = True
                #         while tj is not j and viable:
                #             if board[ti][tj] is not player:
                #                 viable = False
                #             tj = tj + 1
                        
                #         if viable:
                #             return True

                # # up vertical
                # ti = i - 4
                # tj = j
                # if not (ti >= len(board) or tj >= len(board[j])):
                #     if board[ti][tj] is player:
                #         viable = True
                #         while ti is not i and viable:
                #             if board[ti][tj] is not player:
                #                 viable = False
                #             ti = ti + 1
                        
                #         if viable:
                #             return True

    return False;


def h(player, board):
    # ---------------------------------------------------------------------------
    # Heuristic evaluation of board, presuming it is player's move.
    # Student code needed here.
    # Heuristic should not do further lookahead by calling miniMax.  This
    # function estimates the value of the board at a terminal node.
    # ---------------------------------------------------------------------------
    return amr439_h(player, board);


def miniMax(player, board, opponent, min, depth, maxDepth):
    # ---------------------------------------------------------------------------
    # Use MiniMax algorithm to determine best move for player to make for given
    # board.  Return the chosen move and the value of applying the heuristic to
    # the board.
    # To examine each of player's moves and evaluate them with no lookahead,
    # maxDepth should be set to 1.  To examine each of the opponent's moves,
    #  set maxDepth=2, etc.
    # Increase depth by 1 on each recursive call to miniMax.
    # min is the minimum value seen thus far by
    #
    # If a win is detected, the value returned should be INFINITY-depth.
    # This rates 'one move wins' higher than 'two move wins,' etc.  This ensures
    # that Player moves toward a win, rather than simply toward the assurance of
    # a win.
    #
    # Student code needed here.
    # Alpha-Beta pruning is recommended for Extra Credit.
    # Argument list for this function may be altered as needed.
    # ---------------------------------------------------------------------------

    if maxDepth == 0:
        moveList = getMoves(player, board)
        moveValues = []
        for move in moveList:
            if win(player, move):
                return move, INFINITY
            new_board = applyMove(board, move, player)
            moveValues.append(h(player, new_board))
        max_h = max(moveValues)
        index = moveValues.index(max_h)
        return moveList[index], max_h  # return move and backed-up value
    else:
        if depth % 2:  # even depth - calculate player's moves and choose the highest value
            moveList = getMoves(player, board)
            moveValues = []
            for move in moveList:
                new_board = applyMove(board, move, player)
                moveValues.append(h(player, new_board))

            # Suffle moves so that moves aren't choosen in the same order if the highest values are the same
            # https://stackoverflow.com/questions/23289547/shuffle-two-list-at-once-with-same-order
            c = list(zip(moveList, moveValues))
            random.shuffle(c)
            moveList, moveValues = zip(*c)

            # do while emulation (I like this method of do-while in python)
            while True:
                max_h = max(moveValues)  # get max h value from avaliable moves
                index = moveValues.index(max)  # get the index from that list
                moveValues.pop(index)  # pop that h value out of that list (in case we need to loop)
                best_move = moveList.pop(index)  # pop the move according to the best h value (in case we need to loop)
                new_board = applyMove(board, best_move, player)
                if win(player, new_board):
                    return best_move, (INFINITY - depth)
                if depth == maxDepth:
                    return best_move, max_h
                miniMove, miniValue = miniMax(player, new_board, opponent, max_h, depth + 1, maxDepth)  # calculate opponents moves from the current best move
                if(miniValue <= max_h):  # if the opponent cannot get a better move from our current best move, then end the loop
                    break

            return best_move, max_h

        else:  # odd depth - calculate opponent's moves and choose the lowest value
            moveList = getMoves(opponent, board)
            max_h = 0 - INFINITY
            best_move = moveList[0]
            for move in moveList:
                new_board = applyMove(board, move, opponent)
                h_val = h(player, new_board)
                if h_val > max_h:
                    max_h = h_val
                    best_move = move
            
            if max_h > min or depth == maxDepth:
                return best_move, max_h  # if an opponent's move can beat the players, return that move so that the preceeding call knows
            else:
                new_board = applyMove(board, best_move, opponent)
                return miniMax(player, new_board, opponent, 0, depth + 1, maxDepth)


def miniMaxRandom(player, board, opponent, min, depth, maxDepth):
    # This code just picks a random move
    moveList = getMoves(player, board)  # find all legal moves
    k = randrange(0, len(moveList))  # pick one at random
    move = moveList[k]
    value = h(player, board)
    return move, value  # return move and backed-up value


def getComputerMove(player, board):
    # ---------------------------------------------------------------------------
    # If the opponent is a computer, use artificial intelligence to select
    # the best move.
    # For this demo, a move is chosen at random from the list of legal moves.
    # ---------------------------------------------------------------------------
    opponent = 'w' if player == 'b' else 'b'
    move, value = miniMax(player, board, opponent, INFINITY, 0, 0)
    return move


def getComputerMoveRandom(player, board):
    opponent = 'w' if player == 'b' else 'b'
    move, value = miniMaxRandom(player, board, opponent, INFINITY, 0, 0)
    return move


def playerMove(board, player, playerType):
    # ---------------------------------------------------------------------------
    # Depending on the player type, return either a Human move or Computer move.
    # ---------------------------------------------------------------------------
    if playerType == "Human":
        # return getHumanMove(player, board)
        return getComputerMoveRandom(player, board)
    else:
        return getComputerMove(player, board)


def showInstructions():
    # ---------------------------------------------------------------------------
    # Initialize "legend" board with position numbers
    # ---------------------------------------------------------------------------
    print(
        """
Two players alternate turns, placing marbles on a 6x6 grid, each
trying to be the first to get 5 of their own colored marbles,
black or white) in a row, either horizontally, vertically, or
diagonally.  After placing a marble on the grid, the player rotates
one of 4 subgrids clockwise (Right) or counter-clockwise (Left).
Moves have the form "b/n gD", where b and n describe the subgrid and
position where the marble will be placed, g specifies the subgrid to
rotate, and D is either L or R, for rotating the subgrid left or right.
Numbering follows the scheme shown below (between 1 and 9), where
subgrids 1 and 2 are on the top, and 3 and 4 are on the bottom:
""")

    legend = initBoard()
    #	print(legend)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            legend[i][j] = (GRID_SIZE * i + j % GRID_SIZE) % GRID_ELEMENTS + 1
    showBoard(legend)

    print("\nRotating subgrid " + str(1) + " Right:")
    newBoard = rotateRight(legend, 1)
    showBoard(newBoard)

    print("\nRotating subgrid " + str(3) + " Left:")
    newBoard = rotateLeft(legend, 3)
    showBoard(newBoard)


if __name__ == "__main__":

    print("\n-------------------\nWelcome to Pentago!\n-------------------")
    ch = input("Do you want to see instructions (y/n)? ")
    if ch == 'y' or ch == 'Y':
        showInstructions()

    board = initBoard()
    numEmpty = 36

    # -----------------------------------------------------------------------
    # Get player information
    # -----------------------------------------------------------------------
    playerName = [None for i in range(2)]
    playerColor = [None for i in range(2)]  # b or w
    playerType = [None for i in range(2)]  # "Human" or "Computer"

    print("Welcome to Pentago!")
    print("Player 1 plays first.")
    for i in range(2):
        playerName[i] = input("\nName of Player " + str(i + 1) + ": ")
        ch = input("Human or Computer Player (h/c)? ")
        playerType[i] = "Human" if (ch == 'h' or ch == 'H') else "Computer"

    ch = input("Will " + playerName[0] + " play Black or White (b/w)?")
    playerColor[0] = 'b' if (ch == 'b' or ch == 'B') else 'w'
    playerColor[1] = 'w' if (ch == 'b' or ch == 'B') else 'b'
    showBoard(board)

    # -----------------------------------------------------------------------
    # Play game, alternating turns until a win encountered, or board full.
    # -----------------------------------------------------------------------
    gameOver = False
    currentPlayer = 0
    while (not gameOver):
        move = playerMove(board, playerColor[currentPlayer], playerType[currentPlayer])
        print(playerName[currentPlayer] + "'s move: " + move)
        board = applyMove(board, move, playerColor[currentPlayer])
        showBoard(board)
        numEmpty = numEmpty - 1

        win0 = win(playerColor[0], board)
        win1 = win(playerColor[1], board)
        gameOver = win0 or win1 or numEmpty == 0

        currentPlayer = 1 - currentPlayer;

    # -----------------------------------------------------------------------
    # Game is over, determine winner.
    # -----------------------------------------------------------------------
    if (win0 and win1):
        print("Game ends in a tie (multiple winners).")
    elif win0:
        print(playerName[0] + "(" + playerColor[0] + ") wins")
    elif win1:
        print(playerName[1] + "(" + playerColor[1] + ") wins")
    else:  # numEmpty==0
        print("Game ends in a tie (no winner).")
