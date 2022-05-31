class Puzzle:
    def __init__(self, code=None):
        if not code:
            self.code = "0" * (9 * 9)
        else:
            self.code = code
        
        if len(self.code) == (9 * 9):
            self.dimension = 9
        elif len(self.code) == (16 * 16):
            self.dimension = 16
        else:
            raise ValueError(f"The code does not have the correct length.\nLength: {len(self.code)})")

        self.lim = int(self.dimension ** (1/2))
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
        row_start = (r // self.lim) * self.lim
        row_end = row_start + self.lim if row_start + self.lim < self.dimension else self.dimension
        col_start = (c // self.lim) * self.lim
        col_end = col_start + self.lim if col_start + self.lim < self.dimension else self.dimension

        box = []
        for _r in range(row_start, row_end):
            for _c in range(col_start, col_end):
                box.append(self.board[_r][_c])
        assert len(box) == self.dimension
        return box

    def place_at_pos(self, pos, value):
        self.code = self.code[:pos] + value + self.code[pos + 1:]
        self.board = self.code_to_board(self.code)
        return 1

    def __str__(self):
        _str = ""
        for r, row in enumerate(self.board):
            if r % self.lim == 0 and r != 0:
                _str += "-" * (self.dimension * 2) + ("-" * (self.dimension // 2)) + "\n"
            for c, val in enumerate(row):
                if c % self.lim == 0 and c != 0:
                    _str += "| "
                _str += val + " "
            _str += "\n"
        return _str