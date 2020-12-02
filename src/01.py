from helpers import get_args
from helpers import load_inputs


def solve_1(inputs):
    solution = None
    items = [(i, 2020 - i) for i in inputs if 2020 - i in inputs]
    if items:
        solution = items[0][0] * items[0][1]

    print(f'Solution 1: {solution}')
    return solution


def solve_2(inputs):
    solution = None
    for i in inputs:
        remainder = 2020 - i
        items = [
            (d, remainder - d)
            for d in inputs
            if d != i
            and remainder - d in inputs
        ]
        if items:
            solution = i * items[0][0] * items[0][1]
            break

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '01'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=True, data_type=int)
    if args.solution == '1':
        solution_1 = solve_1(inputs)
    elif args.solution == '2':
        solution_2 = solve_2(inputs)
    elif args.solution == 'both':
        solution_1 = solve_1(inputs)
        solution_2 = solve_2(inputs)
