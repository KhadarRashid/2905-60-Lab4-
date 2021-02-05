import unittest
from unittest import TestCase
import camelCase

class TestCamelCase(TestCase):
    # Testing whether the list is joining correctly
    def test_join_list(self):
        sentence_example = ['This', 'Is', 'A', 'List']
        expected_result = 'ThisIsAList'

        self.assertEqual(expected_result, camelCase.join_list(sentence_example))       

    def test_camel_case_working(self):
        #testing if the function turns the sentence into camelCase
        sentence_example = 'ILikeBread'
        expected_result = 'iLikeBread'

        self.assertEqual(expected_result, camelCase.camel_case(sentence_example))

    def test_turn_sentence_into_word_list(self):
        # testing to see if the sentence gets turned into a list
        sentence_example = 'make this a list'
        expected_result = ['make', 'this', 'a', 'list']
        self.assertEqual(expected_result, camelCase.make_list(sentence_example))


if __name__ == '__main__':
    unittest.main()