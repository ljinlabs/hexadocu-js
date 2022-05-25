_BOARD_DIMENSION = (16,16)
_VALID_SETS = set(['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'])
class Solver:
    def __init__(self):
        self.board = self.get_board()

    def get_board(self, board) -> list[list]:
        try:
            if self.check_board(board):
                return board
        except ValueError as e:
            print(e)
        
    def check_board(self, board) -> bool:
        if (num_rows:=len(board) == _BOARD_DIMENSION[0]) and (num_cols := len(board[0]) == _BOARD_DIMENSION[1]):
            return True
        raise ValueError(f"The dimensions are incorrect.\nCurrent dimension: {num_rows}x{num_cols}")

    def get_nth_row(self, n) -> list:
        if n < 0 or n > _BOARD_DIMENSION[0]:
            raise ValueError(f"n must be between [0,16)\nn = {n}")
        return self.board[n]

    def get_nth_col(self, n) -> list:
        """
        returns the nth column as a list
        """
        if n < 0 or n > _BOARD_DIMENSION[0]:
            raise ValueError(f"n must be between [0,16)\nn = {n}")
        _cols = [(val for idx, val in enumerate(row) if idx == n) for row in self.board]
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
        for i in range(row_start, (row_start + 4)):
            for j in range(col_start, (col_start + 4)):
                _box.append(self.board[i][j])
        return _box
        
    def check_row(self, r, value):
        return value in self.get_nth_row(r)

    def check_col(self, c, value):
        return value in self.get_nth_col(c)
        
    def check_box(self, r, c, value):
        return value in self.get_nth_box(r,c)

    def find_next_empty(self):
        for row_idx, row in enumerate(self.board):
            for col_idx, val in enumerate(row):
                if val == "0":
                    return row_idx, col_idx
        return 999, 999

    def is_valid(self, r, c, value):
        return self.check_box(r,c,value) or \
            self.check_row(r, value) or \
                self.check_col(c, value)

    def get_choices(self, r, c):
        

    def backtrack(self, candidate=None):
        if not candidate:
            candidate = self.board
        next_empty = self.find_next_empty()
        if next_empty == (999, 999):
            return self.board