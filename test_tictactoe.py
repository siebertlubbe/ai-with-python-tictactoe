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
        

if __name__ == '__main__':
    unittest.main()