import random
from pprint import pprint, pformat


class Life:
    def __init__(self, sizex, sizey, init_state=None):
        self.sizex = sizex
        self.sizey = sizey
        self._live_neighbors = None
        if not init_state:
            self._life_board = self._init_empty()
        else:
            self._life_board = init_state
        self.compute_live_neighbors()

    def __repr__(self):
        return '\n'.join([
            pformat(self._life_board),
            pformat(self._live_neighbors)
        ])

    def size(self):
        return self.sizex, self.sizey

    def get(self, x, y):
        return self._life_board[x][y]

    def set(self, x, y, value):
        self._life_board[x][y] = value

    def live_neighbors(self, x, y):
        return self._live_neighbors[x][y]

    def _init_empty(self):
        return [[random.choice([0, 1]) for i in range(self.sizex)] for j in range(self.sizey)]

    def compute_live_neighbors(self):
        self._live_neighbors = self._init_empty()
        for i in range(self.sizex):
            for j in range(self.sizey):
                neighbors = [
                    self._life_board[i - 1][j - 1], self._life_board[i - 1][j], self._life_board[i - 1][(j + 1) % self.sizey],
                    self._life_board[i][j - 1], self._life_board[i][(j + 1) % self.sizey],
                    self._life_board[(i + 1) % self.sizex][j - 1], self._life_board[(i + 1) % self.sizex][j], self._life_board[(i + 1) % self.sizex][(j + 1) % self.sizey],
                ]
                self._live_neighbors[i][j] = neighbors.count(True)

    def run_life(self):
        """
        Any live cell with two or three live neighbours survives.
        Any dead cell with three live neighbours becomes a live cell.
        All other live cells die in the next generation. Similarly, all other dead cells stay dead.
        """
        output = Life(self.sizex, self.sizey, self._life_board)
        for i in range(self.sizex):
            for j in range(self.sizey):
                curr_cell = output.get(i, j)
                if curr_cell and output.live_neighbors(i, j) in [2, 3]:
                    output.set(i, j, 0)
                elif output.live_neighbors(i, j) == 3:
                    output.set(i, j, 1)
                else:
                    output.set(i, j, 0)
        return output


if __name__ == '__main__':

    life = Life(5, 5)
    pprint(life._life_board)
