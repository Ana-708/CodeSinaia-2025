def roman_converter(num):

    if not isinstance(num, int):
        return None
    
    if num >= 4000 or num <= 0:
        return None
    
    out = ''

    ROMAN_VALUES = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    for (value, symbol) in ROMAN_VALUES:
        while num >= value:
              out += symbol
              num -= value

    return out