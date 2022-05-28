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
        self.assertTrue(self.solver.check_row(0,"3"))
