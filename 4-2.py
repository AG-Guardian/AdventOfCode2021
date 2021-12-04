class Board:
    def __init__(self, id: int):
        self.rows = [[None, None, None, None, None] for i in range(5)]
        self.cols = [[None, None, None, None, None] for i in range(5)]
        self.sum = 0
        self.id = id
        self.score = 0
        self.won = False

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
        if not self.won:
            for x in range(5):
                for y in range(5):
                    if self.get_cell(x, y) == num:
                        self.set_cell(x, y, 'x')

    def check_win(self, num: int) -> bool:
        if not self.won:
            if ['x', 'x', 'x', 'x', 'x'] in self.rows or ['x', 'x', 'x', 'x', 'x'] in self.cols:
                self.won = True
                self.score = self.sum * num
        return self.won


input = open('in.txt', 'r')
order = input.readline().strip()
boards = []

# Build the boards from input
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

# Mark numbers and keep track of winners as they appear
winners = []
for num in order.split(','):
    for board in boards:
        board.mark_num(int(num))
        if board.check_win(int(num)) and board not in winners:
            winners.append(board)

print(winners[-1].score)