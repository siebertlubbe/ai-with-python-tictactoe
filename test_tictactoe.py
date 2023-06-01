import unittest

import tictactoe as ttt

class TestTicTacToe(unittest.TestCase):

    def test_player(self):
        X = "X"
        O = "O"
        EMPTY = None

        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.player(board), X)

        board = [[X, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.player(board), O)


    def test_actions(self):
        X = "X"
        O = "O"
        EMPTY = None

        board = [[X, X, X],
                [X, X, X],
                [X, X, X]]
        self.assertEqual(ttt.actions(board), set())

        board = [[EMPTY, X, X],
                [X, X, X],
                [X, X, X]]
        self.assertEqual(ttt.actions(board), {(0,0)})

        board = [[EMPTY, X, X],
                [X, EMPTY, X],
                [X, X, X]]
        self.assertEqual(ttt.actions(board), {(0,0),(1,1)})


    def test_actions(self):
        X = "X"
        O = "O"
        EMPTY = None

        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        result = [[X, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.result(board, (0,0)), result)

        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        result = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, X],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.result(board, (1,2)), result)

        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, X],
                [EMPTY, EMPTY, EMPTY]]
        result = [[O, EMPTY, EMPTY],
                [EMPTY, EMPTY, X],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.result(board, (0,0)), result)


    def test_winner(self):
        X = "X"
        O = "O"
        EMPTY = None

        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.winner(board), None)
        
        board = [[X, X, X],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.winner(board), X)

        board = [[EMPTY, EMPTY, EMPTY],
                [O, O, O],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.winner(board), O)

        board = [[EMPTY, EMPTY, O],
                [EMPTY, EMPTY, O],
                [EMPTY, EMPTY, O]]
        self.assertEqual(ttt.winner(board), O)

        board = [[X, EMPTY, EMPTY],
                [EMPTY, X, EMPTY],
                [EMPTY, EMPTY, X]]
        self.assertEqual(ttt.winner(board), X)

        board = [[EMPTY, EMPTY, X],
                [EMPTY, X, EMPTY],
                [X, EMPTY, EMPTY]]
        self.assertEqual(ttt.winner(board), X)


    def test_terminal(self):
        X = "X"
        O = "O"
        EMPTY = None

        board = [[X, O, X],
                [X, O, O],
                [O, X, X]]
        self.assertEqual(ttt.terminal(board), True)

        board = [[X, O, X],
                [X, O, O],
                [O, X, EMPTY]]
        self.assertEqual(ttt.terminal(board), False)

        board = [[X, O, X],
                [X, O, X],
                [O, O, EMPTY]]
        self.assertEqual(ttt.terminal(board), True)

        board = [[X, O, X],
                [X, O, X],
                [O, EMPTY, X]]
        self.assertEqual(ttt.terminal(board), True)

    def test_utility(self):
        X = "X"
        O = "O"
        EMPTY = None

        board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.utility(board), 0)
        
        board = [[X, X, X],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.utility(board), 1)

        board = [[EMPTY, EMPTY, EMPTY],
                [O, O, O],
                [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(ttt.utility(board), -1)

if __name__ == '__main__':
    unittest.main()