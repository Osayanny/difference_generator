import itertools


_SPACECOUNT = 4
_IDENT = 2
_CHAR = ' '


def to_str(value, ident_size):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif not isinstance(value, dict):
        return str(value)

    lines = []
    ident = _CHAR * (ident_size + _SPACECOUNT)
    brackets_ident = _CHAR * ident_size

    for key in value.keys():
        str_value = to_str(value[key], ident_size + _SPACECOUNT)
        lines.append(f'{ident}{key}: {str_value}')
    result = itertools.chain('{', lines, [brackets_ident + '}'])
    return '\n'.join(result)


def stylish(diff):
    lines = []
    for node in diff:
        name = node['key']
        ident_size = node['depth'] * _SPACECOUNT
        deep_ident = _CHAR * (ident_size + _IDENT)
        curent_ident = _CHAR * ident_size

        if 'children' in node.keys():
            line = f'{deep_ident}  {name}: {stylish(node['children'])}'
            lines.append(line)
        else:
            deep_ident_size = ident_size + _SPACECOUNT
            if node['status'] == 'unchanged':
                str_value = to_str(node['value'], deep_ident_size)
                line = f'{deep_ident}  {name}: {str_value}'
                lines.append(line)

            elif node['status'] == 'changed':
                old_str_value = to_str(node['old_value'], deep_ident_size)
                new_str_value = to_str(node['new_value'], deep_ident_size)
                old_line = (f'{deep_ident}- {name}: {old_str_value}')
                new_line = (f'{deep_ident}+ {name}: {new_str_value}')
                lines.extend([old_line, new_line])

            elif node['status'] == 'added':
                str_value = to_str(node['value'], deep_ident_size)
                line = f'{deep_ident}+ {name}: {str_value}'
                lines.append(line)

            elif node['status'] == 'deleted':
                str_value = to_str(node['value'], deep_ident_size)
                line = f'{deep_ident}- {name}: {str_value}'
                lines.append(line)
    result = itertools.chain('{', lines, [curent_ident + '}'])
    return '\n'.join(result)
