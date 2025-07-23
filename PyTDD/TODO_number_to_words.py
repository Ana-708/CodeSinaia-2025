def number_to_words(n):

    if not isinstance(n, int):
        return None
    
    if n >= 4000 or n <= 0:
        return None
    
    out = ''

    VALUES_1 = [
        (1000, 'thousands'),
        (100, 'hundreds'),
        (50, 'fifty'),
        (40, 'forty'),
        (30, 'thirty'),
        (20, 'twenty'),
        (0, 'ty'),
        (12, 'twelve'),
        (11, 'eleven'),
        (10, 'ten'),
        (9, 'nine'),
        (8, 'eight'),
        (7, 'seven'),
        (6, 'six'),
        (5, 'five'),
        (4, 'four'),
        (3, 'three'),
        (2, 'two'),
        (1, 'one')
    ]

    def get_symbol(value):
        for v, s in VALUES_1:
            if v == value:
                return s.strip()
        return ''

    num = 0

    for value, symbol in VALUES_1:
        if value >= 100:
            count = n // value
            if count != 0:
                out += ' ' + get_symbol(count) + ' ' + get_symbol(value)
            n -= value * count

        # elif value >= 60:
        #     count = value / 10
        #     if count == n / 10:
        #         out += ' ' + get_symbol(count) + get_symbol(0)

        elif value >= 20:
            count = value / 10
            if count == n / 10:
                out += ' ' + get_symbol(value) + ' ' + get_symbol(n % 10)

    return out


# 3479 = 3 thousands, 4 hundreds, 7 tens, 9 ones