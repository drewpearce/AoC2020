import argparse
import os


DIR = os.path.abspath(os.path.dirname(__file__))


def load_inputs(day, test=None, split_lines=True, data_type=None):
    if test is True:
        f_name = f'{day}_test.txt'
    else:
        f_name = f'{day}.txt'

    with open(os.path.join(DIR, 'inputs', f_name)) as f:
        data = f.read()

    if split_lines is True:
        if data_type:
            data = [data_type(line) for line in data.splitlines()]
        else:
            data = data.splitlines()

    return data


def get_args(day):
    parser = argparse.ArgumentParser(
        prog=f'Day {day}',
        description=f'Run solution for Day {day}'
    )
    parser.add_argument(
        '-t',
        '--test',
        action='store_true',
        help='Run the test cases. Defaults to false.'
    )
    parser.add_argument(
        '-s',
        '--solution',
        type=str,
        help='Which solution to run. Defaults to both.',
        choices=['1', '2', 'both'],
        default='both'
    )

    return parser.parse_args()
