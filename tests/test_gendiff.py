import pytest
import os
from gendiff.module.gen_diff import generate_diff, parse_file


def get_fixture_path(file_name):
  curent_dir = os.path.dirname(os.path.abspath(__file__))
  return os.path.join(curent_dir, 'fixtures', file_name)

def read(file_path):
  with open(file_path, 'r') as f:
    result = f.read()
    return result

def test_parse_file():
  expect = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    "follow": False
  }
  json_result = parse_file('tests/fixtures/json/plain1.json')
  yml_result = parse_file('tests/fixtures/yaml/plain1.yml')

  assert expect == json_result
  assert expect == yml_result
  

plain_expect = read(get_fixture_path('plain.txt'))
nested_expect = read(get_fixture_path('nested.txt'))
plain_data_json = generate_diff('tests/fixtures/json/plain1.json', 'tests/fixtures/json/plain2.json')
plain_data_yml = generate_diff('tests/fixtures/yaml/plain1.yml', 'tests/fixtures/yaml/plain2.yml')


@pytest.mark.parametrize('test_input,expected', [(plain_data_json, plain_expect), (plain_data_yml, plain_expect)])
def test_generate_diff_with_plain(test_input, expected):
  assert test_input == expected


nested_data_json = generate_diff('tests/fixtures/json/nested1.json', 'tests/fixtures/json/nested2.json')
nested_data_yml = generate_diff('tests/fixtures/yaml/nested1.yml', 'tests/fixtures/yaml/nested2.yml')

@pytest.mark.parametrize('test_input,expected', [(nested_data_json, nested_expect), (nested_data_yml, nested_expect)])
def test_gendiff_with_nested(test_input, expected):
  assert test_input == expected