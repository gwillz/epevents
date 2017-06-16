import unittest, types
from epevents.utils import ensure_fire, ArgsError

class ensure_fire_test(unittest.TestCase):
    def test(self):
        args = (1, 2, 3)
        handlers = [
            lambda a, b, c: (a, b),
            lambda a, b, c: (b, c)
        ]
        
        with ensure_fire(handlers, args) as actual: pass
        expected = [
            (1, 2),
            (2, 3)
        ]
        
        self.assertEqual(actual, expected)
    
    def test_wrap(self):
        def wrap_this(handler, *args):
            return handler("additional", *args)
        
        args = (1, 2)
        handlers = [lambda a, b, c: (a, b, c)]
        
        with ensure_fire(handlers, args, wrap=wrap_this) as actual: pass
        expected = [("additional", 1, 2)]
        
        self.assertEqual(actual, expected)
    
    
    def test_raise(self):
        class AnError(Exception):
            pass
        
        def throw_here(a):
            raise AnError(a)
        
        args = ('aye',)
        handlers = [
            lambda a: a,
            throw_here,
            lambda a: a+a
        ]
        
        self.actual = []
        expected = [
            'aye',
            'ayeaye'
        ]
        
        def will_raise():
            with ensure_fire(handlers, args) as actual:
                self.actual = actual
        
        self.assertRaises(AnError, will_raise)
        self.assertEqual(expected, self.actual)
    
