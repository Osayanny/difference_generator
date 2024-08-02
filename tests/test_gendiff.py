from gendiff.module.gen_diff import generate_diff, parse_file


def get_expected_string():
  with open('tests/fixtures/expected_string.txt', 'r') as f:
    expect = f.read()
  return expect

def test_parse_file():
  expect = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    "follow": False
  }
  json_result = parse_file('tests/fixtures/file1.json')
  yml_result = parse_file('tests/fixtures/file1.yml')

  assert expect == json_result
  assert expect == yml_result
  

def test_generate_diff_with_json():
  expected = get_expected_string()
  result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
  assert expected == result


def test_gendiff_with_yml():
  expected = get_expected_string()
  result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
  assert expected == result

