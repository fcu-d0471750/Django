from mutant2 import calculator
import unittest



class CalculatorTestCase(unittest.TestCase):

    def setUp(self):

        self.args = (3, 2)



    def tearDown(self):

        self.args = None



    def test_plus(self):

        expected = 5;

        result = calculator.plus(*self.args);

        self.assertEqual(expected, result);



    def test_minus(self):

        expected = 1;

        result = calculator.minus(*self.args);

        self.assertEqual(expected, result);



if __name__ == '__main__':

    unittest.main(verbosity=2)





    