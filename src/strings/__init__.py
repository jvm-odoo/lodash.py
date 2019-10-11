"""

    Strings

"""

def camel_case(string):
    string = ''.join(c for c in string.title() if c.isalnum())
    return string[0].lower() + string[1:]

def capitalize(string):
    return ''.join(c for c in string.upper() if c.isalnum() or c.isspace())

def ends_with(string, char, index=None):
    if not index:
        index = len(string)

    return string[index - 1] == char

def escape(string):
    return (string.replace('&', '&amp;')
            .replace('>', '&gt;')
            .replace('<', '&lt;')
            .encode('ascii', 'xmlcharrefreplace'))

def kebab_case(string):
    for i, c in enumerate(string):
        if c.isupper() and i:
            string = string[:i] + '-' + c.lower() + string[i + 1:]

        if c.isspace() and i:
            string = string[:i + 1] + '-' + string[i + 2:]
        elif not c.isalnum() and i:
            string = string[:i + 1] + '-' + string[i + 2:]

    if not string[len(string)-1].isalnum():
        string = string[:len(string)-1]

    return ''.join(
        c for c in string.lower() if c.isalnum() or c == '-'
    )

def lower_case(string):
    for i, c in enumerate(string):
        if c.isupper() and i:
            string = string[:i] + ' ' + c + string[i + 1:]

        if not c.isalnum() and not c.isspace():
            string = string.replace(string[i + 1], ' ')

    return string.lower()

def lower_first(string):
    return string[0].lower() + string[1:]

def pad(string, length, chars):
    computed_length = length - len(string)

    if computed_length <= 0:
        return string

    left_length, right_length = computed_length // 2, -(-computed_length // 2)

    before, after = '', ''

    i = 0
    while i < left_length:
        try:
            before += chars[i]
            i += 1
        except IndexError:
            left_length = left_length - len(chars)
            i = 0

    i = 0
    while i < right_length:
        try:
            after += chars[i]
            i += 1
        except IndexError:
            right_length = right_length - len(chars)
            i = 0

    return before + string + after

def repeat(string, n=1):
    return string * n

def replace(string, pattern, replacement):
    return string.replace(pattern, replacement)

def snake_case(string):
    for i, c in enumerate(string):
        if c.isupper() and i:
            string = string[:i] + '_' + c.lower() + string[i + 1:]

        if c.isspace() and i:
            string = string[:i + 1] + '_' + string[i + 2:]
        elif not c.isalnum() and i:
            string = string[:i + 1] + '_' + string[i + 2:]

    if not string[len(string)-1].isalnum():
        string = string[:len(string)-1]

    return ''.join(c for c in string.lower() if c.isalnum() or c == '_')
