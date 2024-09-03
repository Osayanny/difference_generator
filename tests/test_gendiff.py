import pytest
import os
from gendiff.gen_diff import generate_diff


def get_fixture_path(file_name):
    curent_dir = os.path.dirname(os.path.abspath(__file__))
    name, ext = os.path.splitext(file_name)
    if ext == '.txt':
        return os.path.join(curent_dir, 'fixtures', name + ext)
    elif ext == '.json':
        return os.path.join(curent_dir, 'fixtures', 'json', name + ext)
    else:
        return os.path.join(curent_dir, 'fixtures', 'yaml', name + ext)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize('test_input,expected',
                         [
                             (['simple_1.json', 'simple_2.json', 'stylish'], 'stylish_simple.txt'),
                             (['simple_1.json', 'simple_2.json', 'plain'], 'plain_simple.txt'),
                             (['simple_1.json', 'simple_2.json', 'json'], 'json_simple.txt'),
                             (['nested_1.json', 'nested_2.json', 'stylish'], 'stylish_nested.txt'),
                             (['nested_1.json', 'nested_2.json', 'plain'], 'plain_nested.txt'),
                             (['nested_1.json', 'nested_2.json', 'json'], 'json_nested.txt'),
                             (['simple_1.yml', 'simple_2.yml', 'stylish'], 'stylish_simple.txt'),
                             (['simple_1.yml', 'simple_2.yml', 'plain'], 'plain_simple.txt'),
                             (['simple_1.yml', 'simple_2.yml', 'json'], 'json_simple.txt'),
                             (['nested_1.yml', 'nested_2.yml', 'stylish'], 'stylish_nested.txt'),
                             (['nested_1.yml', 'nested_2.yml', 'plain'], 'plain_nested.txt'),
                             (['nested_1.yml', 'nested_2.yml', 'json'], 'json_nested.txt')
                         ])
def test_gendiff(test_input, expected):
    file_name_1, file_name_2, format = test_input
    path_1 = get_fixture_path(file_name_1)
    path_2 = get_fixture_path(file_name_2)
    expect = read(get_fixture_path(expected))
    result = generate_diff(path_1, path_2, format)
    assert result == expect



