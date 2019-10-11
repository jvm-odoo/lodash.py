"""

    Arrays

"""

def every(arr, fun, i=0):
    if not arr or len(arr) == 0:
        return False

    return True if fun(arr[i]) and i == len(arr) - 1 else False if not fun(arr[i]) and i == len(arr) - 1 else every(arr, fun, i + 1)

def some(arr, fun, i=0):
    if not arr or len(arr) == 0:
        return False

    return True if fun(arr[i]) \
        else False if not fun(arr[i]) and i == len(arr) - 1 \
        else some(arr, fun, i + 1)

def filtered(arr, fun):
    return [item for item in arr if fun(item)]

def pull(arr, *args):
    for arg in args:
        arr = [item for item in arr if item != arg]

    return arr

def flatten(arr):
    next_arr = []

    for i in arr:
        if isinstance(i, list):
            next_arr += i
        else:
            next_arr.append(i)

    for i in next_arr:
        if isinstance(i, list):
            return flatten(next_arr)

    return next_arr

def diff(a, b):
    return [i for i in a if i not in b]

def compact(arr):
    return list(filter(None, arr))

def chunk(arr, size=1):
    return [arr[i:i + size] for i in range(0, len(arr), size)]

def concat(arr, *args):
    return flatten(arr + [i for i in args])

def intersection(a, b):
    return [i for i in a if i in b]

def xor(arr, *args):
    return diff(arr, flatten(list(args)))

def without(arr, *args):
    return [i for i in arr if i not in args]

def drop(arr, n=1):
    return arr[n:]

def dropRight(arr, n=1):
    return arr[:n]

def dropWhile(arr, fun):
    for item in arr:
        if not fun(item):
            break
        else:
            arr = arr[1:]

    return arr

def dropWhileRight(arr, fun):
    for item in arr:
        if not fun(item):
            break
        else:
            arr = arr[:-1]

    return arr

def fill(arr, value, start=0, end=-1):
    end = len(arr) if end == -1 else end

    for i in range(0, end):
        if i >= start:
            arr[i] = value

    return arr

def findIndex(arr, arg, fromIndex=0):
    for i in range(fromIndex, len(arr)):
        if arg(arr[i]):
            return i
    return -1

def findLastIndex(arr, arg, fromIndex=0):
    for i in reversed(range(0 + fromIndex, len(arr))):
        if arg(arr[i]):
            return i
    return -1

def head(arr):
    return arr[0]

def first(arr):
    return head(arr)

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

"""

    Demo

"""

if __name__ == '__main__':
    print('=========================================')
    print('                 Arrays                  ')
    print('=========================================')
    print(
        'some([1, 2, 3, 4], lambda x: x == 3): ',
        some([1, 2, 3, 4], lambda x: x == 3),
        '\n'
    )

    print(
        'every([3, 3, 3, 3], lambda x: x == 3): ',
        every([3, 3, 3, 3], lambda x: x == 3),
        '\n'
    )

    print(
        'filtered([1, 2, 3, 4], lambda x: x == 3): ',
        filtered([1, 2, 3, 4], lambda x: x == 3),
        '\n'
    )

    print(
        'pull([1, 2, 3, 4, 4], 2, 4): ',
        pull([1, 2, 3, 4, 4], 2, 4),
        '\n'
    )

    print(
        'flatten([[1, 2], [[[3]]], 4]): ',
        flatten([[1, 2], [[[3]]], 4]),
        '\n'
    )

    print(
        'diff([1, 2, 3, 4, 5], [5]): ',
        diff([1, 2, 3, 4, 5], [5]),
        '\n'
    )

    print(
        'compact([1, False, 2, 0, 3, None, 4]): ',
        compact([1, False, 2, 0, 3, None, 4]),
        '\n'
    )

    print(
        'chunk([1, 2, 3, 4], 3): ',
        chunk([1, 2, 3, 4], 3),
        '\n'
    )

    print(
        'concat([1, 2], [3, 4]): ',
        concat([1, 2], [3, 4]),
        '\n'
    )

    print(
        'intersection([1, 2, 3, 4], [1, 2]): ',
        intersection([1, 2, 3, 4], [1, 2]),
        '\n'
    )

    print(
        'xor([1, 2, 3, 4], [1, 2], [4]): ',
        xor([1, 2, 3, 4], [1, 2], [4]),
        '\n'
    )

    print(
        'without([1, 2, 3, 4], 1, 4): ',
        without([1, 2, 3, 4], 1, 4),
        '\n'
    )

    print(
        'drop([1, 2, 3, 4], 2):',
        drop([1, 2, 3, 4], 2),
        '\n'
    )

    print(
        'dropRight([1, 2, 3, 4], 2):',
        dropRight([1, 2, 3, 4], 2),
        '\n'
    )

    print(
        'dropWhile([0, 0, 1, 0, 0], lambda x: x == 0):',
        dropWhile([0, 0, 1, 0, 0], lambda x: x == 0),
        '\n'
    )

    print(
        'dropWhileRight([0, 0, 1, 0, 0], lambda x: x == 0):',
        dropWhileRight([0, 0, 1, 0, 0], lambda x: x == 0),
        '\n'
    )

    print(
        'fill([1, 2, 3, 4], \'*\', 1, 3):',
        fill([1, 2, 3, 4], '*', 1, 3),
        '\n'
    )

    print(
        'findIndex([1, 2, 3, 4], lambda x: x == 3, 2):',
        findIndex([1, 2, 3, 4], lambda x: x == 3, 2),
        '\n'
    )

    print(
        'findLastIndex([1, 2, 3, 4], lambda x: x == 3, 2):',
        findLastIndex([1, 2, 3, 4], lambda x: x == 3, 2),
        '\n'
    )

    print(
        'head([1, 2, 3 ,4]) or first([1, 2, 3, 4]):',
        head([1, 2, 3, 4]),
        '\n'
    )

    print('=========================================')
    print('                 Strings                 ')
    print('=========================================')

    print(
        'camel_case(\' Hello or hi world! \'):',
        camel_case(' Hello or hi world! '),
        '\n'
    )

    print(
        'capitalize(\'Hello World!\'):',
        capitalize('Hello World!'),
        '\n'
    )

    print(
        'ends_with(\'Hello\', \'l\', index=4):',
        ends_with('Hello', 'l', index=4),
        '\n'
    )

    print(
        'escape(\'<p>Hello & Welcome</p>\'):',
        escape('<p>Hello & Welcome</p>'),
        '\n'
    )

    print(
        'kebab_case(\'HelloOr hi_world!\'):',
        kebab_case('HelloOr hi_world!'),
        '\n'
    )

    print(
        'lower_case(\'HelloOr hi-world!\'):',
        lower_case('HelloOr hi-world!'),
        '\n'
    )

    print(
        'lower_first(\'Hello\'):',
        lower_first('Hello'),
        '\n'
    )

    print(
        'pad(\'hello\', 10, \'_-\'):',
        pad('hello', 10, '_-'),
        '\n'
    )

    print(
        'repeat(\'hello\', 2):',
        repeat('hello', 2),
        '\n'
    )

    print(
        'replace(\'Hello nobody!\', \'nobody\', \'world\'):',
        replace('Hello nobody!', 'nobody', 'world'),
        '\n'
    )

    print(
        'snake_case(\'HelloOr hi-world!\'):',
        snake_case('HelloOr hi-world!'),
        '\n'
    )
