import json
import yaml


def parse_file(path):
    if path.endswith('.json'):
        return json.load(open(path))
    elif path.endswith('.yml'):
        return yaml.safe_load(open(path))


def generate_diff(firts_path, second_path):
    first_file_data = parse_file(firts_path)
    second_file_data = parse_file(second_path)

    result = []

    keys = first_file_data.keys() | second_file_data.keys()

    result.append('{')
    for key in sorted(keys):
        if key not in first_file_data:
            result.append(f'  + {key}: {second_file_data[key]}')
        elif key not in second_file_data:
            result.append(f'  - {key}: {first_file_data[key]}')
        elif first_file_data[key] == second_file_data[key]:
            result.append(f'    {key}: {first_file_data[key]}')
        else:
            result.append(f'  - {key}: {first_file_data[key]}')
            result.append(f'  + {key}: {second_file_data[key]}')
    result.append('}')

    result = list(map(str.lower, result))

    return '\n'.join(result)
