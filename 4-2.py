class Board:
    def __init__(self, id: int):
        self.rows = [[None, None, None, None, None] for i in range(5)]
        self.cols = [[None, None, None, None, None] for i in range(5)]
        self.sum = 0
        self.id = id
        self.score = 0

    def set_cell(self, x: int, y: int, val):
        if type(val) is int:
            self.sum += val
        elif type(self.get_cell(x, y)) is int:
            self.sum -= self.get_cell(x, y)
        self.rows[x][y] = val
        self.cols[y][x] = val

    def get_cell(self, x: int, y: int):
        return self.rows[x][y]

    def mark_num(self, num: int):
        for x in range(5):
            for y in range(5):
                if self.get_cell(x, y) == num:
                    self.set_cell(x, y, 'x')

    def check_win(self) -> bool:
        if ['x', 'x', 'x', 'x', 'x'] in self.rows or ['x', 'x', 'x', 'x', 'x'] in self.cols:
            return True
        return False


input = open('in.txt', 'r')
order = input.readline().strip()
boards = []

row = 0
for line in input.readlines():
    if line == '\n':
        boards.append(Board(len(boards)))
        row = 0
    else:
        vals = line.split()
        col = 0
        for val in vals:
            boards[-1].set_cell(row, col, int(val))
            col += 1
        row += 1

for call in order.split(','):
    for board in boards:
        board.mark_num(int(call))
        if board.check_win():
            board.score = board.sum * int(call)
            print(f"Board {board.id} won! Score is: {board.score}")
            boards.remove(board)
