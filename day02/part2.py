import argparse

import pytest

from support.support import timing


def compute(s: str) -> int:
    rows = s.splitlines()
    count = 0
    for row in rows:
        splits = row.split()
        (pos1, pos2), letter, pwd = map(int, splits[0].split('-')), splits[1][0], splits[2]
        valid = (pwd[pos1 - 1] == letter) != (pwd[pos2 - 1] == letter)  # xor
        count += valid

    return count


INPUT_S = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


@pytest.mark.solved
@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            (INPUT_S, 1),
            ),
    )
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
