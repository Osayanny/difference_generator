import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser


def parse_args(parser):
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    return path_to_file1, path_to_file2
