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
  

plain_data = read(get_fixture_path('plain.txt'))


def test_generate_diff_with_plain_json():
  expected = plain_data
  result = generate_diff('tests/fixtures/json/plain1.json', 'tests/fixtures/json/plain2.json')
  assert expected == result


def test_gendiff_with_plain_yml():
  expected = plain_data
  result = generate_diff('tests/fixtures/yaml/plain1.yml', 'tests/fixtures/yaml/plain2.yml')
  assert expected == result

