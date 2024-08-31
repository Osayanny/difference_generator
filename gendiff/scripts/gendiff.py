#!/usr/bin/env python3

import parser
import gen_diff


def main():
    parse = parser.make_parser()
    path1, path2, format = parser.parse_args(parse)
    print(gen_diff.generate_diff(path1, path2, format))


if __name__ == '__main__':
    main()
