import unittest, types
from epevents.utils import ensure_fire

class ensure_fire_test(unittest.TestCase):
    def test(self):
        handlers = [
            lambda a, b, c: (a, b),
            lambda a, b, c: (b, c)
        ]
        args = (1, 2, 3)
        
        actual = ensure_fire(handlers, args)
        expected = [
            (1, 2),
            (2, 3)
        ]
        
        self.assertTrue(isinstance(actual, types.GeneratorType))
        
        for result in actual:
            self.assertTrue(result in expected, "{} not expected".format(result))
    
    
    def test_wrap(self):
        def wrap_this(handler, *args):
            return handler("additional", *args)
        
        handler = lambda a, b, c: (a, b, c)
        args = (1, 2)
        
        actual, = ensure_fire([handler], args, wrap=wrap_this)
        expected = ("additional", 1, 2)
        
        self.assertEqual(actual, expected)
    
    
    def test_raise(self):
        def throw_here(a):
            raise KeyError(a)
        
        handlers = [
            lambda a: a,
            throw_here,
            lambda a: a+a
        ]
        args = ('aye',)
        
        actual = ensure_fire(handlers, args)
        expected = [
            'aye',
            'ayeaye'
        ]
        
        raised, results = None, []
        try:
            for r in actual:
                results.append(r)
            
        except KeyError as e:
            raised = e
        
        self.assertTrue(isinstance(raised, KeyError), "Exception should have been raised")
        self.assertEqual(results, expected)
        
        # self.assertRaises(ensure_fire(lambda a: raise KeyError('lol'), ('one',)), KeyError)
    
