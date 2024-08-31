import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        dest="format",
                        default='stylish',
                        help='set format of output')
    return parser


def parse_args(parser):
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    format = args.format
    return path_to_file1, path_to_file2, format
