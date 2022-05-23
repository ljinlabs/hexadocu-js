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
        
        