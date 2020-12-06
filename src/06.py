from helpers import get_args
from helpers import load_inputs


def solve_1(inputs):
    solution = sum(len(set(i.replace('\n', ''))) for i in inputs)

    print(f'Solution 1: {solution}')
    return solution


def solve_2(inputs):
    solution = sum(
        sum(
            1 for a in set(i.replace('\n', ''))
            if all(a in string for string in i.split('\n'))
        )
        for i in inputs
    )

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '06'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=False)
    inputs = inputs.split('\n\n')
    if args.solution == '1':
        solution_1 = solve_1(inputs)
    elif args.solution == '2':
        solution_2 = solve_2(inputs)
    elif args.solution == 'both':
        solution_1 = solve_1(inputs)
        solution_2 = solve_2(inputs)
