import re

from helpers import get_args
from helpers import load_inputs


def solve_1(inputs):
    solution = None
    valid = []
    for line in inputs:
        splt = line.split(' ')
        (mn, mx) = (int(n) for n in splt[0].split('-'))
        val = splt[1][:-1]
        matches = re.findall(val, splt[2])
        if len(matches) >= mn and len(matches) <= mx:
            valid.append(splt[2])

    solution = len(valid)

    print(f'Solution 1: {solution}')
    return solution


def solve_2(inputs):
    solution = None
    valid = []
    for line in inputs:
        splt = line.split(' ')
        (mn, mx) = (int(n) for n in splt[0].split('-'))
        val = splt[1][:-1]

        if ((splt[2][mn - 1] == val and splt[2][mx - 1] != val)
                or (splt[2][mn - 1] != val and splt[2][mx - 1] == val)):
            valid.append(splt[2])

    solution = len(valid)

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '02'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=True)
    if args.solution == '1':
        solution_1 = solve_1(inputs)
    elif args.solution == '2':
        solution_2 = solve_2(inputs)
    elif args.solution == 'both':
        solution_1 = solve_1(inputs)
        solution_2 = solve_2(inputs)
