"""
Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.
"""
from life import Life


def test_life():
    input = Life(9, 9)
    print('input:')
    print(input)
    output = input.run_life()
    print('output:')
    print(output)
    sizex, sizey = input.size()
    for i in range(sizex):
        for j in range(sizey):
            curr_prev_cell = input.get(i, j)
            curr_new_cell = output.get(i, j)
            # check survivors: Any live cell with two or three live neighbours survives.
            # check live: Any dead cell with three live neighbours becomes a live cell.
            if curr_new_cell:
                assert \
                    (curr_prev_cell and input.live_neighbors(i, j) in [2, 3]) or \
                    ((not curr_prev_cell) and input.live_neighbors(i, j) == 3)
            # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            else:
                assert not curr_new_cell, "cell should not be alive"


def test_life_neighbors():
    input = Life(3, 3, [[False, False, False], [False, True, True], [False, True, True]])
    assert input._live_neighbors[1][1] == 3
