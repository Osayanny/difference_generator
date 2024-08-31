import pytest
import os
from gendiff.gen_diff import generate_diff, parse_file


def get_fixture_path(file_name):
    curent_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(curent_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
        return result


simple_json_data_paths =['tests/fixtures/json/simple_1.json', 'tests/fixtures/json/simple_2.json']
nested_json_data_paths =['tests/fixtures/json/nested_1.json', 'tests/fixtures/json/nested_2.json']
simple_yaml_data_paths =['tests/fixtures/yaml/simple_1.yml', 'tests/fixtures/yaml/simple_2.yml']
nested_yaml_data_paths =['tests/fixtures/yaml/nested_1.yml', 'tests/fixtures/yaml/nested_2.yml']


stylish_simple_expect = read(get_fixture_path('stylish_simple.txt'))
stylish_nested_expect = read(get_fixture_path('stylish_nested.txt'))


@pytest.mark.parametrize('test_input,expected', [(simple_json_data_paths, stylish_simple_expect), (simple_yaml_data_paths, stylish_simple_expect), (nested_json_data_paths, stylish_nested_expect), (nested_yaml_data_paths, stylish_nested_expect)])
def test_gendiff_with_stylish(test_input, expected):
    path_1, path_2 = test_input
    result = generate_diff(path_1, path_2, 'stylish')
    assert result == expected


plain_simple_expect = read(get_fixture_path('plain_simple.txt'))
plain_nested_expect = read(get_fixture_path('plain_nested.txt'))


@pytest.mark.parametrize('test_input,expected', [(simple_json_data_paths, plain_simple_expect), (simple_yaml_data_paths, plain_simple_expect), (nested_json_data_paths, plain_nested_expect), (nested_yaml_data_paths, plain_nested_expect)])
def test_generate_diff_with_plain(test_input, expected):
    path_1, path_2 = test_input
    result = generate_diff(path_1, path_2, 'plain')
    assert result == expected


json_simple_expect = read(get_fixture_path('json_simple.txt'))
json_nested_expect = read(get_fixture_path('json_nested.txt'))


@pytest.mark.parametrize('test_input,expected', [(simple_json_data_paths, json_simple_expect), (simple_yaml_data_paths, json_simple_expect), (nested_json_data_paths, json_nested_expect), (nested_yaml_data_paths, json_nested_expect)])
def test_gendiff_with_json(test_input, expected):
    path_1, path_2 = test_input
    result = generate_diff(path_1, path_2, 'json')
    assert result == expected
