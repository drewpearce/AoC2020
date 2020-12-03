from collections import deque
from math import prod

from helpers import get_args
from helpers import load_inputs


def inputs_to_grid(inputs):
    return [deque(line) for line in inputs]


def move(current, movement, grid):
    for queue in grid:
        queue.rotate(-1 * movement[0])

    current[0] += movement[1]
    grid = mark_grid(current, grid)
    return current, grid


def mark_grid(pos, grid):
    if grid[pos[0]][0] == '#':
        grid[pos[0]][0] = 'X'
    elif grid[pos[0]][0] == '.':
        grid[pos[0]][0] = 'O'

    return grid


def loop_slopes(grid, movement):
    pos = [0, 0]
    grid = mark_grid(pos, grid)

    while pos[0] < len(grid) - 1:
        pos, grid = move(pos, movement, grid)

    return grid


def count_crashes(grid):
    sums = []
    for line in grid:
        sums.append(sum(1 for ln in line if ln == 'X'))

    return sum(sums)


def print_grid(grid):
    lines = []
    for line in grid:
        lines.append(''.join(ln for ln in line))

    out = '\n'.join(lines)
    print(f'\n{out}\n')


def solve_1(inputs):
    grid = inputs_to_grid(inputs)
    grid = loop_slopes(grid, (3, 1))
    solution = count_crashes(grid)

    # print_grid(grid)

    print(f'Solution 1: {solution}')
    return solution


def solve_2(inputs):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    crashes = []
    for slope in slopes:
        grid = inputs_to_grid(inputs)
        grid = loop_slopes(grid, slope)
        crashes.append(count_crashes(grid))

    solution = prod(crashes)

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '03'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=True)
    if args.solution == '1':
        solution_1 = solve_1(inputs)
    elif args.solution == '2':
        solution_2 = solve_2(inputs)
    elif args.solution == 'both':
        solution_1 = solve_1(inputs)
        solution_2 = solve_2(inputs)
