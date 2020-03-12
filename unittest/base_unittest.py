import unittest

class FooTest(unittest.TestCase):
    """Sample test case"""

    # # preparing to test
    # def setUp(self):
    #     """ Setting up for the test """
    #     print
    #     "FooTest:setUp_:begin"
    #     assert sum([1, 2, 2]) == 6, "Should be 6"
    #     ## do something...
    #     print
    #     "FooTest:setUp_:end"
    #
    # # ending the test
    # def tearDown(self):
    #     """Cleaning up after the test"""
    #     print
    #     "FooTest:tearDown_:begin"
    #     ## do something...
    #     print
    #     "FooTest:tearDown_:end"

    # assertEqual so sanh bang : assertEqual(first, second, msg)
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "should be 6")
    def test_sum_error(self):
        self.assertEqual(sum([1, 2, 1]), 6, "should be 6")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # assertTrue or assertFalse xac minh mot dieu kien : assertTrue(expr, msg)
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # assertRaise() xac minh mot ngoai le duoc dua ra
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    # cung cap giao dien dong lenh cho tap lenh thu nghiem ( run tap lenh thu nghiem)
    unittest.main()