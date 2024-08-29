#!/usr/bin/env python3

from gendiff.module.gen_diff import generate_diff
from gendiff.module import parser


def main():
    parse = parser.make_parser()
    path1, path2, format = parser.parse_args(parse)
    print(generate_diff(path1, path2, format))


if __name__ == '__main__':
    main()
