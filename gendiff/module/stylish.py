import itertools


_SPACECOUNT = 4
_IDENT = 2


def to_str(value):
    pass


def stylish(diff):
    lines = []
    for node in diff:
        ident_size = node['depth'] * _SPACECOUNT - _IDENT
        curent_ident = ' ' * ident_size

        if 'children' in node.keys():
            lines.append(f'{curent_ident}  {node['key']}: {stylish(node['children'])}')
        else:

            if node['status'] == 'unchanged':
                lines.append(f'{curent_ident}  {node['key']}: {node['value']}')
            elif node['status'] == 'changed':
                lines.append(f'{curent_ident}- {node['key']}: {node['old_value']}')
                lines.append(f'{curent_ident}+ {node['key']}: {node['new_value']}')
            elif node['status'] == 'added':
                lines.append(f'{curent_ident}+ {node['key']}: {node['value']}')
            elif node['status'] == 'deleted':
                lines.append(f'{curent_ident}- {node['key']}: {node['value']}')
                print(type(node['value']))
    result = itertools.chain('{', lines, [curent_ident + '}'])
    return '\n'.join(result)
            
