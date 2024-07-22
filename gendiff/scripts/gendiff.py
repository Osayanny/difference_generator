#!/usr/bin/env python3

import argparse
from gendiff.module import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first file')
    parser.add_argument('second file')
    args = vars(parser.parse_args())
    path_to_file1 = args.get('first file')
    path_to_file2 = args.get('second file')
    print(generate_diff(path_to_file1, path_to_file2))


if __name__ == '__main__':
    main()
