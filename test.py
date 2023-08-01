from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class FlaskTests(TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_index_page(self):
        """Test if the index page renders successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<table id="board">', response.data)

    def test_check_word_valid_word(self):
        """Test check_word with a valid word."""
        with app.test_client() as client:
            boggle_game = Boggle()
            board = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["I", "J", "K", "L"], ["M", "N", "O", "P"]]
            with client.session_transaction() as session:
                session['board'] = board

            response = client.get('/check-word?word=ABCD')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['result']['valid_word_result'])
            self.assertEqual(data['result']['points'], 4)

def test_check_word_invalid_word(self):
    with app.test_client() as client:
        response = client.get('/check-word?word=XYZ')
        data = response.get_json()

        print("Received response data:", data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(data['result']['valid_word_result'])
        self.assertEqual(data['result']['points'], 3)  # Length of the word 'XYZ'


def test_check_word_invalid_request(self):
    with app.test_client() as client:
        response = client.get('/check-word')
        data = response.get_json()

        print("Received response data:", data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)





