import unittest

class TestCalculator(unittest.TestCase):
    #setup
    def setUp(self):
        print("Start")

    #tests
    def test_sum(self):
        self.assertEqual(1+1, 2)

    #tests
    def test_sub(self):
        self.assertEqual(2-1, 1)

    #tear down
    def tearDown(self):
        print("End")

if __name__ == '__main__':
    unittest.main()