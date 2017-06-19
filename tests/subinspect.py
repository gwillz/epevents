import unittest
from functools import wraps
from epevents.utils import unwrap, argspec

def decorate(fn):
    @wraps(fn)
    def inner(*args):
        return fn(*reversed(args))
    return inner

def decorate_again(fn):
    @wraps(fn)
    def inner(*args):
        return fn('extra', *args)
    return inner

@decorate
@decorate_again
def extra_decorated_args(one, two, three):
    return one, two, three

def variable_args(one, *args):
    return args

def no_args():
    return 'no-args'

class subinspect_test(unittest.TestCase):
    def test_unwrap(self):
        "Find the wrapped function under layers of decorators"
        fn = unwrap(extra_decorated_args)
        actual = fn(1, 2, 3)
        expected = 1, 2, 3
        self.assertEqual(actual, expected)
    
    
    def test_argspec(self):
        actual = argspec(variable_args)
        expected = 1, True
        self.assertEqual(actual, expected)
    
    def test_argspec_empty(self):
        actual = argspec(no_args)
        expected = 0, False
        self.assertEqual(actual, expected)
        
