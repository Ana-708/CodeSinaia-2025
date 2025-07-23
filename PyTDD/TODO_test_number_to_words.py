import unittest
from TODO_number_to_words import number_to_words

class TestNums(unittest.TestCase):
    
    # ======== Step 1 ======== 
    def test_no_input(self):
        self.assertEqual(number_to_words(None), None)

    # ======== Step 2 ======== 
    def test_no_input(self):
        self.assertEqual(number_to_words('a'), None)

    # ======== Step 3 ======== 
    def test_num_vir(self):
        self.assertEqual(number_to_words(123.4), None)


    # ======== Step 4 ======== 
    def test_range_min(self):
        self.assertEqual(number_to_words(0), None)

    # ======== Step 5 ======== 
    def test_range_max(self):
        self.assertEqual(number_to_words(4000), None)

# class TestOnes(unittest.TestCase):

#     def test_base_1(self):
#         self.assertEqual(number_to_words(1), 'one')

class TestTens(unittest.TestCase):

    def test_base_1000(self):
        self.assertEqual(number_to_words(1000), ' one thousands')

    def test_base_3429(self):
        self.assertEqual(number_to_words(3429), ' three thousands four hundreds twenty nine')

    def test_base_2400(self):
        self.assertEqual(number_to_words(2400), ' two thousands four hundreds')

    def test_base_3000(self):
        self.assertEqual(number_to_words(3000), ' three thousands')