from random import shuffle, sample

from enum import Enum

_BOARD_DIMENSION = (16,16)
_VALID_SETS = set(['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G'])

class Difficulty(Enum):
    EZPZ = 1
    EASY = 2
    REGULAR = 3
    HARD = 4
    BRUH = 5

class Solver:
    def __init__(self):
        self.board = None
        self.is_solved = False

    def get_board(self, board) -> list:
        try:
            if self.check_board(board):
                return board
        except ValueError as e:
            print(e)
        
    def check_board(self, board) -> bool:
        """
        checks the board for DIMENSIONS
        """
        if (num_rows:=len(board) == _BOARD_DIMENSION[0]) and (num_cols := len(board[0]) == _BOARD_DIMENSION[1]):
            return True
        raise ValueError(f"The dimensions are incorrect.\nCurrent dimension: {num_rows}x{num_cols}")

    def get_nth_row(self, n) -> list:
        """
        returns the nth row as a list
        """
        if n < 0 or n > _BOARD_DIMENSION[0] - 1:
            raise ValueError(f"n must be between [0,16)\nn = {n}")
        return self.board[n]

    def get_nth_col(self, n) -> list:
        """
        returns the nth column as a list
        """
        if n < 0 or n > _BOARD_DIMENSION[0] - 1:
            raise ValueError(f"n must be between [0,16)\nn = {n}")
        _cols = [[val for idx, val in enumerate(row) if idx == n] for row in self.board]
        _cols = [_cols[i][0] for i in range(_BOARD_DIMENSION[0])]
        # print(_cols)
        return _cols
    
    def get_nth_box(self, row, col) -> list:
        """
        0 | 1 | 2 | 3
        -------------
        4 | 5 | 6 | 7
        -------------
        8 | 9 | 10| 11
        -------------
        12| 13| 14| 15
        :returns the current box as a 1d list
        """
        _box = []
        row_start = (row // 4) * 4
        col_start = (col // 4) * 4
        row_end = row_start + 4 if row_start + 4 < 16 else 15
        col_end = col_start + 4 if col_start + 4 < 16 else 15
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                _box.append(self.board[i][j])
        return _box
        
    def check_row(self, r, value):
        return value not in self.get_nth_row(r)

    def check_col(self, c, value):
        return value not in self.get_nth_col(c)
        
    def check_box(self, r, c, value):
        return value not in self.get_nth_box(r,c)

    def find_next_empty(self):
        for row_idx, row in enumerate(self.board):
            for col_idx, val in enumerate(row):
                if val == "0":
                    return row_idx, col_idx
        return "999","999"

    def is_valid(self, r, c, value):
        row_valid = self.check_row(r, value)
        col_valid = self.check_col(c, value)
        box_valid = self.check_box(r, c, value)
        return row_valid and col_valid and box_valid

    def get_choices(self, r, c):
        row = set(self.get_nth_row(r))
        col = self.get_nth_col(c)
        box = self.get_nth_box(r,c)
        already = row.union(col, box)
        left = _VALID_SETS.difference(already)
        if "0" in left:
            left.remove("0")
        return list(left)

    def backtrack(self):
        r, c = self.find_next_empty()
        if r == "999":
            return self.board
        _choices = self.get_choices(r,c)
        shuffle(_choices)
        for _choice in _choices:
            if self.is_valid(r,c,_choice):
                self.board[r][c] = _choice
                print(self)
                if self.backtrack():
                    return True
            self.board[r][c] = "0"
        return False

    def code_to_board(self, code) -> bool:
        if (length := len(code)) != (correct := _BOARD_DIMENSION[0] * _BOARD_DIMENSION[1]):
            raise ValueError(f"The dimension does not match\nCurrent length: {length}\nSupposed to be: {correct}")
        board = []
        row = []
        self.code = code
        for idx, val in enumerate(code):
            if idx % 16 == 0 and idx != 0:
                board.append(row)
                row = []
            row.append(val)
        board.append(row)
        self.board = board
        return True

    def board_is_valid(self):
        for r, row in enumerate(self.board):
            for c, val in enumerate(row):
                if val != "0":
                    if not self.is_valid(r, c, val):
                        return False
        return True

    @property
    def board_to_code(self) -> str:
        """
        :returns str code
        """
        code = ""
        for row in self.board:
            for val in row:
                code += val
        return code

    def __str__(self):
        _str = ""
        for row in self.board:
            for val in row:
                _str += val + " "
            _str += "\n"
        return _str

class Builder:
    def __init__(self):
        self.code = "0" * 256
        self.solver = Solver()
        
    def pos_to_coords(self, pos) -> tuple:
        row = pos // _BOARD_DIMENSION[0]
        col = pos % _BOARD_DIMENSION[1]
        return (row, col)

    def insert_data(self, num_points=40):
        self.solver.code_to_board(("0" * 16 * 16))
        positions = sample([i for i in range(_BOARD_DIMENSION[0] * _BOARD_DIMENSION[1])], num_points)
        print(positions)
        for pos in positions:
            r, c = self.pos_to_coords(pos)
            choices = self.solver.get_choices(r, c)
            shuffle(choices)
            try:
                elem = choices.pop()
                self.code = self.code[:pos] + elem + self.code[pos + 1:]
                self.solver.code_to_board(self.code)
                print(self.code)
            except IndexError:
                print(f"no choices left for this cell\npos: {pos[0]}, {pos[1]}\n")
        return True

    def build(self, difficulty: Difficulty = Difficulty.EZPZ):
        if difficulty == Difficulty.EZPZ:
            pass
        self.solver.code_to_board(("0" * (16 * 16)))
        self.insert_data()
        print(self.solver)
        self.solver.backtrack()
        print(self.solver)            
         
        
if __name__ == '__main__':
    b = Builder()
    b.build()
    