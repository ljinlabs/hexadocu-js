# from sudoku_generator import Solver
from puzzle import Puzzle
from unittest import TestCase

# class SolverTestCase(TestCase):
#     def setUp(self):
#         code = "00000000000000000000000000000000405060000000000000900000000300000000000000000000000000000D0000C00000000080000000G200000F000000000000000000000000000000000000000000000000000000000000000001000000000A0000000000B0000000000E0000000000000000700000"
#         self.solver = Solver()
#         self.solver.code_to_board(code)

#     def test_get_row(self):
#         code = "0" * (16 * 16)
#         code = code[:3] + "3" + code[4:]
#         board = self.solver.code_to_board(code)
#         print(board)
#         first_row = self.solver.get_nth_row(0)
#         first_row_code = list(code)[:16]
#         self.assertEqual(first_row, first_row_code)
        
#     def test_row_check(self):
#         code = "0" * (16 * 16)
#         code = code[:3] + "3" + code[4:]
#         self.solver.code_to_board(code)
#         self.assertFalse(self.solver.check_row(0,"3"))

#     def test_col_check(self):
#         code = "0" * (16 * 16)
#         code = "3" + code[1:]
#         code = code[:16] + "3" + code[17:]
#         self.solver.code_to_board(code)
#         for elem in self.solver.get_nth_col(0):
#             print(elem, sep=" ")
#         self.assertFalse(self.solver.check_col(0,"3"))

#     # def test_is_valid(self):
#     #     code = "0" * (16 * 16)
#     #     code = code[:3] + "33" + code[5:]
#     #     self.solver.code_to_board(code)
#     #     self.assertFalse(self.solver.is_valid(0,3,"3"))

class PuzzleTestCase(TestCase):
    def setUp(self):
        self.code_16 = "0" * (16 * 16)
        self.code_9 = "0" * (9 * 9)
        self.code_9_last_box = 

    def test_init(self):
        # default case
        self.p = Puzzle()
        self.assertEqual(self.p.dimension,9)

        # case 16
        self.p = Puzzle(self.code_16)
        self.assertEqual(self.p.dimension, 16)

    def test_code_to_board(self):
        # test dimensions 9x9
        self.p = Puzzle()
        self.assertEqual(len(self.p.board), 9)
        self.assertEqual(len(self.p.board[0]), 9)

        #test dimensions 16x16
        self.p = Puzzle(self.code_16)
        self.assertEqual(len(self.p.board), 16)
        self.assertEqual(len(self.p.board[0]), 16)

    # def test