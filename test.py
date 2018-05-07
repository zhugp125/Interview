#！/usr/bin/env python3
# _*_ coding: utf-8 _*_

import unittest

class AbsTestCase(unittest.TestCase):
    
    def setUp(self):
        print('set up...')

    def tearDown(self):
        print('tear down...')

    # test_xxx is a test case
    def test_zero(self):
        self.assertEqual(abs(0), 0)

    def test_pos_num(self):
        self.assertEqual(abs(10), 10)

    def test_neg_num(self):
        self.assertEqual(abs(-10.5), 10.5)

    def test_type_error(self):
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()

# command order: python3 -m unittest test
# https://docs.python.org/3/library/unittest.html?highlight=unittest#assert-methods