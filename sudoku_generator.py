_BOARD_DIMENSION = (12,12)
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
        if n < 0 or n > _BOARD_DIMENSION[0]:
            raise ValueError(f"n must be between [0,12)\nn = {n}")
        return self.board[n]

    def get_nth_col(self, n) -> list:
        """
        returns the nth column as a list
        """
        if n < 0 or n > _BOARD_DIMENSION[0]:
            raise ValueError(f"n must be between [0,12)\nn = {n}")
        _cols = [(val for idx, val in enumerate(row) if idx == n) for row in self.board]
        return _cols
    
    def get_nth_box(self, row, col) -> list:
        """
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        :returns the current box as a 1d list
        """
        _box = []
        _row_start = (row // 4) * 4
        _col_start = (col // 4) * 4
        for _row in self.board[_row_start : _row_start + 4]:
            for val in _row[_col_start : _col_start + 4]:
                _box.append(val)
        return _box

    def is_empty(self, r, c) -> bool:
        """
        returns true if the cell is empty
        returns false otherwise
        """
        return self.board[r][c] == "0"

    def find_next_empty(self) -> tuple(int,int):
        for ridx, row in enumerate(self.board):
            for cidx, val in enumerate(row):
                if self.is_empty(ridx, cidx):
                    return ridx, cidx
        return 999, 999

    def check_row(self, r, value):
        """
        returns true if the value at board[r][c] is repeated in the same row
        returns false otherwise
        """
        return value in self.get_nth_row(r)

    def check_col(self, c, value):
        """
        returns true if the value at board[r][c] is repeated in the same col
        returns false otherwise
        """
        return value in self.get_nth_col(c)

    def check_box(self, r, c, value):
        """
        returns true if the value at board[r][c] is repeated in the same box
        returns false otherwise
        """
        return value in self.get_nth_box(r,c)

    def is_valid(self, r, c, value):
        """
        returns true if the cell is valid
        """
        if self.check_box(r, c, value) or \
            self.check_row(r, value) or \
            self.check_col(c, value):
            return False
        return True
    
    def solve(self):
