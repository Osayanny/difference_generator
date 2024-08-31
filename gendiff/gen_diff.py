import json
import yaml
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def parse_file(path):
    if path.endswith('.json'):
        return json.load(open(path))
    elif path.endswith('.yml') or path.endswith('.yaml'):
        return yaml.safe_load(open(path))


def get_node_diff(status, key, depth, **kwargs):
    node_diff = {
        'status': status,
        'key': key,
        'depth': depth}
    node_diff.update(**kwargs)
    return node_diff


def make_diff(first_data, second_data, depth): # noqa

    result = []

    keys = first_data.keys() | second_data.keys()

    for key in sorted(keys):
        first_value = first_data.get(key)
        second_value = second_data.get(key)

        if isinstance(first_value, dict) and \
                isinstance(second_value, dict):
            child_diff = make_diff(first_value, second_value, depth + 1)
            diff = get_node_diff('nested', key, depth, children=child_diff)

        elif key in first_data and key in second_data:
            if first_data[key] == second_data[key]:
                diff = get_node_diff('unchanged', key, depth, value=first_value)

            else:
                diff = get_node_diff('changed',
                                     key,
                                     depth,
                                     old_value=first_value,
                                     new_value=second_value)

        elif key in first_data:
            diff = get_node_diff('deleted', key, depth, value=first_value)

        elif key in second_data:
            diff = get_node_diff('added', key, depth, value=second_value)

        result.append(diff)
    return result


def generate_diff(first_path, second_path, format='stylish'):
    first_data = parse_file(first_path)
    second_data = parse_file(second_path)

    diff = make_diff(first_data, second_data, 0)
    if format == 'stylish':
        return get_stylish(diff)
    elif format == 'plain':
        return get_plain(diff)
    elif format == 'json':
        return get_json(diff)
