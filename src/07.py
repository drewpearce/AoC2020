import re

from helpers import get_args
from helpers import load_inputs


def parse_inputs(inputs):
    rules = {}
    for line in inputs:
        (bag, rule) = line.split(' bags contain ')
        if bag not in rules:
            rules[bag] = []

        for match in re.finditer(r'(\d+)\s([a-z]+\s[a-z]+)', rule):
            rules[bag].append({'color': match.group(2), 'q': int(
                match.group(1))})

    return rules


def reverse_rules(rules):
    out = {}

    for parent, rule in rules.items():
        for child in rule:
            if child['color'] not in out:
                out[child['color']] = set()

            out[child['color']].add(parent)

    return out


def solve_1(rules):
    rules = reverse_rules(rules)
    mine = 'shiny gold'

    parents = set()
    check = [mine]

    while check:
        item = check.pop()
        if item != mine and item not in parents:
            parents.add(item)

        for color in rules.get(item, []):
            if color != mine and color not in parents:
                check.append(color)

    solution = len(parents)

    print(f'Solution 1: {solution}')
    return solution


def count_bags(total, color, rules):
    for rule in rules.get(color, []):
        total += rule['q']
        total += rule['q'] * count_bags(0, rule['color'], rules)

    return total


def solve_2(rules):
    solution = count_bags(0, 'shiny gold', rules)

    print(f'Solution 2: {solution}')
    return solution


if __name__ == '__main__':
    day = '07'
    args = get_args(day)
    inputs = load_inputs(day, test=args.test, split_lines=True)
    rules = parse_inputs(inputs)
    if args.solution == '1':
        solution_1 = solve_1(rules)
    elif args.solution == '2':
        solution_2 = solve_2(rules)
    elif args.solution == 'both':
        solution_1 = solve_1(rules)
        solution_2 = solve_2(rules)
