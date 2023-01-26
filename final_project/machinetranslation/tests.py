'''
Unit testing for translation functions
'''

import unittest
from translator.py import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''
    This class includes both tests for English to French and vice versa
    '''
    def test_english_to_french (self):
        '''
        Unit testing for English to French function
        '''
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')

    def test_french_to_english (self):
        '''
        Unit testing for French to English function
        '''
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodbye')

if __name__ == '__main__':
    unittest.main()
