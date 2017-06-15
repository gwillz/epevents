import unittest
from epevents.utils import fire_me

def two_args(one, two):
    return one, two

def no_args():
    return 'no-args'

class method_args(object):
    def args(self, one, two):
        return one, two

class FireMe_test(unittest.TestCase):
    
    def test_none(self):
        actual = fire_me(two_args)
        expected = None, None
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = fire_me(two_args, 'hello', 'world')
        expected = 'hello', 'world'
        self.assertEqual(actual, expected)
    
    def test_many(self):
        actual = fire_me(two_args, 'hello', 'world', '!', '!')
        expected = 'hello', 'world'
        self.assertEqual(actual, expected)
    
    def test_missing(self):
        actual = fire_me(no_args, 'hello', 'world')
        expected = 'no-args'
        self.assertEqual(actual, expected)
    
    def test_method(self):
        actual = fire_me(method_args().args, 'hello')
        expected = 'hello', None
        self.assertEqual(actual, expected)
