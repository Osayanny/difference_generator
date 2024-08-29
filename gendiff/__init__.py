from .module.gen_diff import generate_diff, parse_file
from .module.parser import make_parser, parse_args
from .module.stylish import get_stylish

__all__ = (
    'make_parser',
    'parse_args',
    'generate_diff',
    'parse_file',
    'get_stylish',
    'get_plain'
)
