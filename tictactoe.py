"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_cells = 0
    for row in board:
        empty_cells = empty_cells + row.count(EMPTY)
    
    return X if empty_cells % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for id_row, row in enumerate(board):
        for id_cell, cell in enumerate(row):
            actions.add((id_row, id_cell)) if cell == EMPTY else None

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3: return X
        if row.count(O) == 3: return O

    if [board[0][0], board[1][1], board[2][2]].count(X) == 3: return X
    if [board[0][0], board[1][1], board[2][2]].count(O) == 3: return O

    board = list(map(list, zip(*board)))
    for row in board:
        if row.count(X) == 3: return X
        if row.count(O) == 3: return O

    board.reverse()
    if [board[0][0], board[1][1], board[2][2]].count(X) == 3: return X
    if [board[0][0], board[1][1], board[2][2]].count(O) == 3: return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_cells = 0
    for row in board:
        empty_cells = empty_cells + row.count(EMPTY)
    
    return True if empty_cells == 0 or winner(board) == O or winner(board) == X else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
