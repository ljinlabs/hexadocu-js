class Puzzle:
    def __init__(self, code=None):
        if code:
            self.code = code
        else:
            # defaults to a regular sudoku puzzle
            self.code = "0" * (9 * 9)
        
        if (length:= len(self.code)) == (9 * 9):
            self.dimension = 9
        elif length == (16 * 16):
            self.dimension = 16
        else:
            raise ValueError(f"The code does not have the correct length.\nLength: {length})")
        
        self.board = self.code_to_board(self.code)

    def code_to_board(self, code) -> list:
        """
        returns the board version of the code
        """
        board = []
        row = []
        for idx, val in enumerate(code):
            if idx % self.dimension == 0 and idx != 0:
                board.append(row)
                row = []
            row.append(val)
        board.append(row)
        return board

    def get_row(self, r) -> list:
        return self.board[r]

    def get_col(self, c) -> list:
        return [row[c] for row in self.board]
    
    def get_box(self, r, c) -> list:
        lim = 3 if self.dimension == 9 else 4
        row_start = r // lim
        row_end = row_start + lim if row_start + lim < self.dimension else self.dimension
        col_start = c // lim
        col_end = col_start + lim if col_start + lim < self.dimension else self.dimension

        box = []
        for _r in range(row_start, row_end):
            for _c in range(col_start, col_end):
                box.append(self.board[_r][_c])
        assert len(box) == self.dimension
        return box

    