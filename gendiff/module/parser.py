import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first file')
    parser.add_argument('second file')
    return parser


def parse_args(parser):
    args = vars(parser.parse_args())
    path_to_file1 = args.get('first file')
    path_to_file2 = args.get('second file')
    return path_to_file1, path_to_file2
