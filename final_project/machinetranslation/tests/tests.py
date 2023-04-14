import unittest

from ibm_watson import ApiException
from translator import english_to_french, french_to_english


class TestTranslationMethods(unittest.TestCase):
    def test_english_to_french(self):
        # Hello -> Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

        # Null case
        self.assertNotEqual(english_to_french('Goodbye'), None)
        self.assertNotEqual(english_to_french('Goodbye'), '')

        # Empty args case
        with self.assertRaises(TypeError):
            english_to_french()

        # Empty string case
        with self.assertRaises(ApiException):
            english_to_french('')

    def test_french_to_english(self):
        # Bonjour -> Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

        # Null case
        self.assertNotEqual(french_to_english('Au revoir'), None)
        self.assertNotEqual(french_to_english('Au revoir'), '')
        
        # Empty args case
        with self.assertRaises(TypeError):
            french_to_english()
        
        # Empty string case
        with self.assertRaises(ApiException):
            english_to_french('')


unittest.main()
