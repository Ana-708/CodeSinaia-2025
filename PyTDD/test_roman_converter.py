import unittest
from roman_converter import roman_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)


    # ======== Step 2 ======== 
    def test_num_str(self):
        self.assertEqual(roman_converter('a'), None)

    # ======== Step 3 ======== 
    def test_num_vir(self):
        self.assertEqual(roman_converter(123.4), None)


    # ======== Step 4 ======== 
    def test_range_min(self):
        self.assertEqual(roman_converter(0), None)

    # ======== Step 5 ======== 
    def test_range_max(self):
        self.assertEqual(roman_converter(4000), None)

class TestOnes(unittest.TestCase):
    # ======== Step 6 ========
    def test_base_1(self):
        self.assertEqual(roman_converter(1), 'I')

    # ======== Step 7 ========
    def test_two(self):
        self.assertEqual(roman_converter(2), 'II')

    # ======== Step 8 ========
    def test_three(self):
        self.assertEqual(roman_converter(3), 'III')

    # ======== Step 9 ========
    def test_four(self):
        self.assertEqual(roman_converter(4), 'IV')

    # ======== Step 10 ========
    def test_base_5(self):
        self.assertEqual(roman_converter(5), 'V')

    # ======== Step 11 ========
    def test_six(self):
        self.assertEqual(roman_converter(6), 'VI')

    # ======== Step 12 ========
    def test_nine(self):
        self.assertEqual(roman_converter(9), 'IX')

class TestTens(unittest.TestCase):
    # ======== Step 13 ========
    def test_base_10(self):
        self.assertEqual(roman_converter(10), 'X')

    # ======== Step 14 ========
    def test_14(self):
        self.assertEqual(roman_converter(14), 'XIV')

    # ======== Step 15 ========
    def test_25(self):
        self.assertEqual(roman_converter(25), 'XXV')

    # ======== Step 16 ========
    def test_49(self):
        self.assertEqual(roman_converter(49), 'XLIX')

    # ======== Step 17 ========
    def test_99(self):
        self.assertEqual(roman_converter(99), 'XCIX')


class TestHundreds(unittest.TestCase):

    def test_base_100(self):
        self.assertEqual(roman_converter(100), 'C')

    def test_499(self):
        self.assertEqual(roman_converter(499), 'CDXCIX')

class TestFHundreds(unittest.TestCase):

    def test_base_500(self):
        self.assertEqual(roman_converter(500), 'D')

    def test_999(self):
        self.assertEqual(roman_converter(999), 'CMXCIX')

class TestThousands(unittest.TestCase):

    def test_base_1000(self):
        self.assertEqual(roman_converter(1000), 'M')

    def test_2500(self):
        self.assertEqual(roman_converter(2555), 'MMDLV')

    def test_3999(self):
        self.assertEqual(roman_converter(3999), 'MMMCMXCIX')