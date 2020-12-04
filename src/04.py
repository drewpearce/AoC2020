import re

import jsonschema

from helpers import get_args
from helpers import load_inputs


REQ = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPT = ['cid']
SCHEMA = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'byr': {
            'type': 'string',
            'pattern': r'^(19[2-9][0-9]|200[0-2])$'
        },
        'iyr': {
            'type': 'string',
            'pattern': r'^20(1[0-9]|20)$'
        },
        'eyr': {
            'type': 'string',
            'pattern': r'^20(2[0-9]|30)$'
        },
        'hgt': {
            'type': 'string',
            'pattern': r'(^1([5-8][0-9]|9[0-3])cm$|^(59|6[0-9]|7[0-6])in$)'
        },
        'hcl': {
            'type': 'string',
            'pattern': r'^#[0-9a-f]{6}'
        },
        'ecl': {
            'type': 'string',
            'enum': [
                'amb',
                'blu',
                'brn',
                'gry',
                'grn',
                'hzl',
                'oth'
            ]
        },
        'pid': {
            'type': 'string',
            'pattern': r'^\d{9}$'
        },
        'cid': {'type': 'string'}
    },
    'additionalProperties': False,
    'required': ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
}


def parse_inputs(inputs):
    out = []
    items = inputs.split('\n\n')
    for item in items:
        data = re.split(r'\s', item)
        out.append({d.split(':')[0]: d.split(':')[1] for d in data})

    return out


def validate_1(rec):
    if sum(1 for r in REQ if r not in rec) > 0:
        return False

    if sum(1 for k in rec.keys() if k not in REQ + OPT) > 0:
        return False

    return True


def validate_2(rec):
    try:
        jsonschema.validate(rec, SCHEMA)
        return True
    except jsonschema.exceptions.ValidationError:
        return False


def solve_1(inputs):
    solution = sum(1 for i in inputs if validate_1(i))

    print(f'Solution 1: {solution}')
    return solution


def solve_2(inputs):
    solution = sum(1 for i in inputs if validate_2(i))

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '04'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=False)
    inputs = parse_inputs(inputs)
    if args.solution == '1':
        solution_1 = solve_1(inputs)
    elif args.solution == '2':
        solution_2 = solve_2(inputs)
    elif args.solution == 'both':
        solution_1 = solve_1(inputs)
        solution_2 = solve_2(inputs)
