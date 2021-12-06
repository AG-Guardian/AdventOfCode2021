class Board:
    def __init__(self):
        self.rows = [[None, None, None, None, None] for i in range(5)]
        self.cols = [[None, None, None, None, None] for i in range(5)]
        self.sum = 0

    def set_cell(self, x: int, y: int, val):
        if type(val) is int:
            self.sum += val
        elif type(self.get_cell(x, y)) is int:
            self.sum -= self.get_cell(x, y)
        self.rows[x][y] = val
        self.cols[y][x] = val

    def get_cell(self, x: int, y: int):
        return self.rows[x][y]

    def check_num(self, num: int):
        for x in range(5):
            for y in range(5):
                if self.get_cell(x, y) == num:
                    self.set_cell(x, y, 'x')

    def check_win(self) -> bool:
        if ['x', 'x', 'x', 'x', 'x'] in self.rows or ['x', 'x', 'x', 'x', 'x'] in self.cols:
            return True
        return False


with open('in.txt', 'r') as file:
    order = file.readline()
    boards = []

    row = 0
    for line in file.readlines():
        if line == '\n':
            boards.append(Board())
            row = 0
        else:
            vals = line.split()
            col = 0
            for val in vals:
                boards[-1].set_cell(row, col, int(val))
                col += 1
            row += 1

winner = False
for call in order.split(','):
    index = 0
    for board in boards:
        board.check_num(int(call))
        if board.check_win():
            print(f"Board {str(index)} won! Score is: {board.sum * int(call)}")
            winner = True
            break
        index += 1
    if winner:
        break
