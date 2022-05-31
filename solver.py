from random import shuffle, sample

from puzzle import Puzzle

HEX_CHOICES = set(["1","2","3","4","5","6","7","8","9","A","B","C","D","F","G"])
DEC_CHOICES = set(["1","2","3","4","5","6","7","8","9"])

class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.num_tries = 0
        if self.puzzle.dimension == 16:
            self.all_choices = HEX_CHOICES
        else:
            self.all_choices = DEC_CHOICES

    def row_is_valid(self, r, value):
        return value not in self.puzzle.get_row(r)

    def col_is_valid(self, c, value):
        return value not in self.puzzle.get_col(c)

    def box_is_valid(self, r, c, value):
        return value not in self.puzzle.get_box(r, c)
    
    def value_is_valid(self, r, c, value):
        return self.row_is_valid(r, value) and self.col_is_valid(c, value) and self.box_is_valid(r,c,value)

    def get_valid_choices(self, r, c):
        _row = set(self.puzzle.get_row(r))
        _col = set(self.puzzle.get_col(c))
        _box = set(self.puzzle.get_box(r,c))
        _neighbors = _box.union(_row, _col)
        _neighbors.discard("0")
        valid_choices = self.all_choices.difference(_neighbors)
        return list(valid_choices)

    def find_next_empty(self):
        for _r, row in enumerate(self.puzzle.board):
            for _c, val in enumerate(row):
                if val == "0":
                    return (_r, _c)
        return (-1, -1)

    def backtrack(self):
        self.num_tries += 1
        r, c = self.find_next_empty()
        if r == -1:
            return True
        _choices = self.get_valid_choices(r, c)
        shuffle(_choices)
        for choice in _choices:
            if self.value_is_valid(r, c, choice):
                self.puzzle.board[r][c] = choice
                if self.backtrack():
                    return True
            self.puzzle.board[r][c] = "0"
        return False

if __name__ == '__main__':
    sample_code_9 = "070000009510420600080300700008001370023080040400900100962800030000010400700203096"
    # print(len(sample_code_9))
    sample_code_16 = "00FG0B00009000000D08001E0A20B9CG0E020D00F01B00A0B0140090C00062F0000C00630074A00029050C0080060G04000DE07B000G25360000000GE9A0000F0026000070000FD0008907G1003D500C070A00BC00G08E1000CE900A056807G008G00A305100060B00B0G6F2000C0085006F780900000000C000000426800007"
    sample_puzzle = Puzzle(sample_code_9)
    sample_solver = Solver(sample_puzzle)
    sample_solver.backtrack()
    print(sample_puzzle)

    sample_puzzle2 = Puzzle(sample_code_16)
    sample_solver2 = Solver(sample_puzzle2)
    a = sample_solver2.backtrack()
    print(a)
    print(sample_solver2.puzzle)
    print(sample_puzzle2)