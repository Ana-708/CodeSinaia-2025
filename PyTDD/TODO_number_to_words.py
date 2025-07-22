def number_to_words(n):

    if not isinstance(n, int):
        return None
    
    if n >= 4000 or n <= 0:
        return None
    
    out = ''

    VALUES_1 = [
        (1000, ' thousands'),
        (100, ' hundreds'),
        (10, 'ty'),
        (50, 'fifty'),
        (40, 'forty'),
        (30, 'thirty'),
        (20, 'twenty'),
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

    # for (value, symbol) in VALUES_1:
    #     # while n >= value:
    #     #       num += 1
    #     #       n -= value
    #     if n / value != 0:
    #         # out += str(n / value) + symbol
    #         out += symbol(n / value) + symbol 
    #     n -= value * ( n / value )


    for value, symbol in VALUES_1:
        count = n // value
        if count != 0:
            out += get_symbol(count) + ' ' + get_symbol(value)
        n -= value * ( n / value )
        

    return out


# 5479 = 5 thousands, 4 hundreds, 7 tens, 9 ones