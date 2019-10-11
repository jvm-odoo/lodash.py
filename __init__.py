import src

_ = lodash = src

"""

    Demo

"""

if __name__ == '__main__':
    print('=========================================')
    print('                 Arrays                  ')
    print('=========================================')
    print(
        'some([1, 2, 3, 4], lambda x: x == 3): ',
        _.some([1, 2, 3, 4], lambda x: x == 3),
        '\n'
    )

    print(
        'every([3, 3, 3, 3], lambda x: x == 3): ',
        _.every([3, 3, 3, 3], lambda x: x == 3),
        '\n'
    )

    print(
        'filtered([1, 2, 3, 4], lambda x: x == 3): ',
        _.filtered([1, 2, 3, 4], lambda x: x == 3),
        '\n'
    )

    print(
        'pull([1, 2, 3, 4, 4], 2, 4): ',
        _.pull([1, 2, 3, 4, 4], 2, 4),
        '\n'
    )

    print(
        'flatten([[1, 2], [[[3]]], 4]): ',
        _.flatten([[1, 2], [[[3]]], 4]),
        '\n'
    )

    print(
        'diff([1, 2, 3, 4, 5], [5]): ',
        _.diff([1, 2, 3, 4, 5], [5]),
        '\n'
    )

    print(
        'compact([1, False, 2, 0, 3, None, 4]): ',
        _.compact([1, False, 2, 0, 3, None, 4]),
        '\n'
    )

    print(
        'chunk([1, 2, 3, 4], 3): ',
        _.chunk([1, 2, 3, 4], 3),
        '\n'
    )

    print(
        'concat([1, 2], [3, 4]): ',
        _.concat([1, 2], [3, 4]),
        '\n'
    )

    print(
        'intersection([1, 2, 3, 4], [1, 2]): ',
        _.intersection([1, 2, 3, 4], [1, 2]),
        '\n'
    )

    print(
        'xor([1, 2, 3, 4], [1, 2], [4]): ',
        _.xor([1, 2, 3, 4], [1, 2], [4]),
        '\n'
    )

    print(
        'without([1, 2, 3, 4], 1, 4): ',
        _.without([1, 2, 3, 4], 1, 4),
        '\n'
    )

    print(
        'drop([1, 2, 3, 4], 2):',
        _.drop([1, 2, 3, 4], 2),
        '\n'
    )

    print(
        'dropRight([1, 2, 3, 4], 2):',
        _.drop_right([1, 2, 3, 4], 2),
        '\n'
    )

    print(
        'dropWhile([0, 0, 1, 0, 0], lambda x: x == 0):',
        _.drop_while([0, 0, 1, 0, 0], lambda x: x == 0),
        '\n'
    )

    print(
        'dropWhileRight([0, 0, 1, 0, 0], lambda x: x == 0):',
        _.drop_right_while([0, 0, 1, 0, 0], lambda x: x == 0),
        '\n'
    )

    print(
        'fill([1, 2, 3, 4], \'*\', 1, 3):',
        _.fill([1, 2, 3, 4], '*', 1, 3),
        '\n'
    )

    print(
        'findIndex([1, 2, 3, 4], lambda x: x == 3, 2):',
        _.find_index([1, 2, 3, 4], lambda x: x == 3, 2),
        '\n'
    )

    print(
        'findLastIndex([1, 2, 3, 4], lambda x: x == 3, 2):',
        _.find_last_index([1, 2, 3, 4], lambda x: x == 3, 2),
        '\n'
    )

    print(
        'head([1, 2, 3 ,4]) or first([1, 2, 3, 4]):',
        _.head([1, 2, 3, 4]),
        '\n'
    )

    print('=========================================')
    print('                 Strings                 ')
    print('=========================================')

    print(
        'camel_case(\' Hello or hi world! \'):',
        _.camel_case(' Hello or hi world! '),
        '\n'
    )

    print(
        'capitalize(\'Hello World!\'):',
        _.capitalize('Hello World!'),
        '\n'
    )

    print(
        'ends_with(\'Hello\', \'l\', index=4):',
        _.ends_with('Hello', 'l', index=4),
        '\n'
    )

    print(
        'escape(\'<p>Hello & Welcome</p>\'):',
        _.escape('<p>Hello & Welcome</p>'),
        '\n'
    )

    print(
        'kebab_case(\'HelloOr hi_world!\'):',
        _.kebab_case('HelloOr hi_world!'),
        '\n'
    )

    print(
        'lower_case(\'HelloOr hi-world!\'):',
        _.lower_case('HelloOr hi-world!'),
        '\n'
    )

    print(
        'lower_first(\'Hello\'):',
        _.lower_first('Hello'),
        '\n'
    )

    print(
        'pad(\'hello\', 10, \'_-\'):',
        _.pad('hello', 10, '_-'),
        '\n'
    )

    print(
        'repeat(\'hello\', 2):',
        _.repeat('hello', 2),
        '\n'
    )

    print(
        'replace(\'Hello nobody!\', \'nobody\', \'world\'):',
        _.replace('Hello nobody!', 'nobody', 'world'),
        '\n'
    )

    print(
        'snake_case(\'HelloOr hi-world!\'):',
        _.snake_case('HelloOr hi-world!'),
        '\n'
    )
