

def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def get_plain(diff): # noqa

    def inner(diff, path=''):
        lines = []
        for node in diff:
            name = node['key']

            if 'children' in node.keys():
                line = inner(node['children'], path + name + '.')

            elif node['status'] == 'changed':
                format_old = to_str(node['old_value'])
                format_new = to_str(node['new_value'])
                status = f"Property '{path}{name}' was updated. "
                value = f"From {format_old} to {format_new}"
                line = status + value

            elif node['status'] == 'added':
                format_val = to_str(node['value'])
                status = f"Property '{path}{name}' was added with value: "
                line = status + format_val

            elif node['status'] == 'deleted':
                line = f"Property '{path}{name}' was removed"

            else:
                continue

            lines.append(line)

        return '\n'.join(lines)
    return inner(diff, '')
