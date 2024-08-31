from gendiff.parser import make_parser


def test_make_parser():
    parser = make_parser()
    parsed = parser.parse_args([
        'tests/fixtures/json/plain1.json',
        'tests/fixtures/json/plain2.json'])
    assert parsed.first_file == 'tests/fixtures/json/plain1.json'
    assert parsed.second_file == 'tests/fixtures/json/plain2.json'
