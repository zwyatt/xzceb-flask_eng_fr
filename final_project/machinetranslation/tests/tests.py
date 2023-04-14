import unittest

from ibm_watson import ApiException
from translator import english_to_french, french_to_english


class TestTranslationMethods(unittest.TestCase):
    def test_english_to_french(self):
        # Hello -> Bonjour
        expected_output = {
            'translations': [{'translation': 'Bonjour'}],
            'word_count': 1,
            'character_count': 5}
        self.assertEqual(english_to_french('Hello'), expected_output)

        # Null case
        with self.assertRaises(TypeError):
            english_to_french()

        # Empty string case
        with self.assertRaises(ApiException):
            english_to_french('')

    def test_french_to_english(self):
        # Bonjour -> Hello
        expected_output = {
            'translations': [{'translation': 'Hello'}],
            'word_count': 1,
            'character_count': 7}
        self.assertEqual(french_to_english('Bonjour'), expected_output)

        # Null case
        with self.assertRaises(TypeError):
            french_to_english()
        
        # Empty string case
        with self.assertRaises(ApiException):
            english_to_french('')


unittest.main()