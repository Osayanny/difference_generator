from gendiff.module.stylish import to_str


def formating_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    return to_str(value)


def get_plain(diff, path=''):
    lines = []

    for node in diff:
        name = node['key']

        if 'children' in node.keys():
            line = get_plain(node['children'], path + name + '.')

        elif node['status'] == 'changed':
            format_old = formating_value(node['old_value'])
            format_new = formating_value(node['new_value'])
            first_part = f"Property '{path}{name}' was updated. "
            second_part = f"From {format_old} to {format_new}"
            line = first_part + second_part
            
        elif node['status'] == 'added':
            format_val = formating_value(node['value'])
            line = f"Property '{path}{name}' was added with value: {format_val}"

        elif node['status'] == 'deleted':
            line = f"Property '{path}{name}' was removed"

        else:
            continue

        lines.append(line)

    return '\n'.join(lines)
