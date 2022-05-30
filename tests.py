from sudoku_generator import Solver
from unittest import TestCase

class SolverTestCase(TestCase):
    def setUp(self):
        self.solver = Solver()

    def test_get_row(self):
        code = "0" * (16 * 16)
        code = code[:3] + "3" + code[4:]
        board = self.solver.code_to_board(code)
        print(board)
        first_row = self.solver.get_nth_row(0)
        first_row_code = list(code)[:16]
        self.assertEqual(first_row, first_row_code)
        
    def test_row_check(self):
        code = "0" * (16 * 16)
        code = code[:3] + "3" + code[4:]
        self.solver.code_to_board(code)
        self.assertFalse(self.solver.check_row(0,"3"))

    def test_col_check(self):
        code = "0" * (16 * 16)
        code = "3" + code[1:]
        code = code[:16] + "3" + code[17:]
        self.solver.code_to_board(code)
        for elem in self.solver.get_nth_col(0):
            print(elem, sep=" ")
        self.assertFalse(self.solver.check_col(0,"3"))

    # def test_is_valid(self):
    #     code = "0" * (16 * 16)
    #     code = code[:3] + "33" + code[5:]
    #     self.solver.code_to_board(code)
    #     self.assertFalse(self.solver.is_valid(0,3,"3"))