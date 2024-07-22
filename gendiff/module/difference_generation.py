import json


def open_json(file):
    file_data = json.load(open(file))
    return file_data


def generate_diff(file1, file2):
    first_file_data = open_json(file1)
    second_file_data = open_json(file2)
    result = []

    keys = first_file_data.keys() | second_file_data.keys()

    result.append('{')
    for key in sorted(keys):
        if key not in first_file_data:
            result.append(f'+ {key}: {second_file_data[key]}')
        elif key not in second_file_data:
            result.append(f'- {key}: {first_file_data[key]}')
        elif first_file_data[key] == second_file_data[key]:
            result.append(f'  {key}: {first_file_data[key]}')
        else:
            result.append(f'- {key}: {first_file_data[key]}')
            result.append(f'+ {key}: {second_file_data[key]}')
    result.append('}')

    return '\n'.join(result)
