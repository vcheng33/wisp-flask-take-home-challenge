from app import app
from unittest import TestCase

app.config['TESTING'] = True

class SpecialMathAppTestCase (TestCase):
    """ Test flask app of Special Math. """

    def setUp(self):
        """ Stuff to do before every test. """

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_special_math_page(self):
        """ Tests that the function shows the correct page and with the correct
            page sections if the inputs are invalid/valid.
        """
        # Check for Floats and strings as inputs 

        # Testing situation where the input is valid
        with self.client as client:

            response = client.get('/specialmath/7') 
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('"result": 79', html)

        # Testing situation where there is a large, valid input
        with self.client as client:

            response = client.get('/specialmath/1000') 
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('"result": 29792421850814336', html)
        
        # Testing situation where there is an invalid input (negative number)
        with self.client as client:

            response = client.get('/specialmath/-1') 
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 404)
            self.assertIn('<h1>Not Found</h1>', html)
            self.assertIn('The requested URL was not found on the server.', html)

        # Testing situation where there is an invalid input (float number)
        with self.client as client:

            response = client.get('/specialmath/7.0') 
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 404)
            self.assertIn('<h1>Not Found</h1>', html)
            self.assertIn('The requested URL was not found on the server.', html)

        # Testing situation where there is an invalid input (string)
        with self.client as client:

            response = client.get('/specialmath/hello') 
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 404)
            self.assertIn('<h1>Not Found</h1>', html)
            self.assertIn('The requested URL was not found on the server.', html)