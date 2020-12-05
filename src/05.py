from helpers import get_args
from helpers import load_inputs


def get_seat_id(code):
    code = code.replace('F', '0').replace('B', '1').replace(
        'L', '0').replace('R', '1')
    row = int(code[:7], 2)
    col = int(code[7:], 2)

    return (row * 8) + col


def solve_1(inputs):
    ids = {get_seat_id(i) for i in inputs}
    solution = max(ids)
    # fill out solution

    print(f'Solution 1: {solution}')
    return solution


def solve_2(inputs):
    seats = {get_seat_id(i) for i in inputs}
    all_seats = range(8, (126 * 8) + 9)
    missing = {a for a in all_seats if a not in seats}
    my_seat = [
        m for m in missing
        if m - 1 not in missing
        and m + 1 not in missing
    ]
    solution = my_seat[0] if my_seat else None

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '05'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=True)
    if args.solution == '1':
        solution_1 = solve_1(inputs)
    elif args.solution == '2':
        solution_2 = solve_2(inputs)
    elif args.solution == 'both':
        solution_1 = solve_1(inputs)
        solution_2 = solve_2(inputs)
