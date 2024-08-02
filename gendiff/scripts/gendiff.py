#!/usr/bin/env python3

from gendiff.module import gen_diff
from gendiff.module import parser


def main():
    parse = parser.make_parser()
    path1, path2 = parser.parse_args(parse)
    print(gen_diff.generate_diff(path1, path2))


if __name__ == '__main__':
    main()
