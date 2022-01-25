from app import app
from special_math import special_math
from unittest import TestCase

app.config['TESTING'] = True

class SpecialMathTestCase (TestCase):
    """ Test Special Math """

    def setUp(self):
        """ Stuff to do before every test. """

        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_special_math(self):
        """ Validate that the function returns the correct result. """

        # Checks that valid inputs return valid results
        self.assertEqual(special_math(7), 79)
        self.assertEqual(special_math(17), 10926)
        self.assertEqual(special_math(90), 19740274219868223074)

        # Checks that negative numbers raise an error
        with self.assertRaises(Exception) as context:
            special_math(-1)
        
        self.assertTrue('Number must be 0 or larger' in str(context.exception))

        # Checks that float numbers raise an error
        with self.assertRaises(Exception) as context:
            special_math(-1.1)
        
        self.assertTrue('Number must be an integer' in str(context.exception))

        # Checks that strings raise an error
        with self.assertRaises(Exception) as context:
            special_math('hello')
        
        self.assertTrue('Number must be an integer' in str(context.exception))
