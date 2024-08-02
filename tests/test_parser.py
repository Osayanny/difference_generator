from gendiff.module.parser import make_parser, parse_args


def test_make_parser():
    parser = make_parser()
    parsed = parser.parse_args([
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'])
    assert parsed.first_file == 'tests/fixtures/file1.json'
    assert parsed.second_file == 'tests/fixtures/file2.json'
