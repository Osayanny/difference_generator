import json
import yaml
from gendiff.module.stylish import stylish


def parse_file(path):
    if path.endswith('.json'):
        return json.load(open(path))
    elif path.endswith('.yml', '.yaml'):
        return yaml.safe_load(open(path))


def make_diff(first_data, second_data):

    def walk(first_data, second_data, depth):
        result = []

        keys = first_data.keys() | second_data.keys()

        for key in sorted(keys):
            if type(first_data.get(key)) == dict and type(second_data.get(key)) == dict:
                diff = {'status': 'nested',
                        'key': key,
                        'depth': depth,
                        'children': walk(first_data[key], second_data[key], depth + 1)   
                }
                result.append(diff)
            else:
                if key in first_data and key in second_data:
                    if first_data[key] == second_data[key]:
                        diff = {'status': 'unchanged',
                                'key': key,
                                'depth': depth,
                                'value': first_data[key]
                        }        
                        result.append(diff)

                    else:
                        diff = {'status': 'changed',
                                'key': key,
                                'depth': depth,
                                'old_value': first_data[key],
                                'new_value': second_data[key],
                                }
                        result.append(diff)

                elif key in first_data:
                    diff = {'status': 'deleted',
                            'key': key,
                            'depth': depth,
                            'value': first_data[key]
                            }

                    result.append(diff)

                elif key in second_data:
                    diff = {'status': 'added',
                            'key': key,
                            'depth': depth,
                            'value': second_data[key]
                            }

                    result.append(diff)

        return result
    return walk(first_data, second_data, 1)
                

    
def generate_diff(first_path, second_path, format='stylish'):
    first_data = parse_file(first_path)
    second_data = parse_file(second_path)

    diff = make_diff(first_data, second_data)
    if format == 'stylish':
        return stylish(diff)
