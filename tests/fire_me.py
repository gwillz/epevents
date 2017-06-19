import unittest
from functools import wraps
from epevents.utils import fire_me

def two_args(one, two):
    return one, two

def no_args():
    return 'no-args'

def decorate(fn):
    @wraps(fn)
    def inner(*args):
        return fn(*reversed(args))
    return inner

@decorate
def decorated_args(one, two, three):
    return one, two, three

class method_args(object):
    def args(self, one, two):
        return one, two

class FireMe_test(unittest.TestCase):
    
    def test_none(self):
        "Missing args are filled with 'None'"
        actual = fire_me(two_args)
        expected = None, None
        self.assertEqual(actual, expected)
    
    def test_two(self):
        "Just the right amount of args is okay too"
        actual = fire_me(two_args, 'hello', 'world')
        expected = 'hello', 'world'
        self.assertEqual(actual, expected)
    
    def test_many(self):
        "We can fire a function with too many args - they just get dropped"
        actual = fire_me(two_args, 'hello', 'world', '!', '!')
        expected = 'hello', 'world'
        self.assertEqual(actual, expected)
    
    def test_missing(self):
        "Some functions don't take args at all"
        actual = fire_me(no_args, 'hello', 'world')
        expected = 'no-args'
        self.assertEqual(actual, expected)
    
    def test_method(self):
        "Methods include a extra 'self' arg that shouldn't be counted"
        actual = fire_me(method_args().args, 'hello')
        expected = 'hello', None
        self.assertEqual(actual, expected)
    
    def test_decorator(self):
        "Decorated functions don't always have the same argcount"
        actual = fire_me(decorated_args, 1, 2, 3)
        expected = 3, 2, 1
        self.assertEqual(actual, expected)
