import unittest
from epevents import Strict as Event, ArgsError

class Strict_test(unittest.TestCase):
    def test(self):
        e = Event('one', 'two', 'three')
        
        e += lambda one, two, three: (one, two, three)
        e += lambda one, two, three: (three, one)
        
        actual = list(e(1, 2, 3))
        expected = [
            (1, 2, 3),
            (3, 1)
        ]
        self.assertEqual(actual, expected)
    
    def test_init_err(self):
        "Init should throw because of 'one' and 'one' being the same"
        self.assertRaises(ArgsError, lambda: Event('one', 'one', 'three'))
    
    def test_local_vars(self):
        """ Determine args from locals
        
        previously 'three' would throw an ArgsError because it was believed
        to be an argument and therefore not matching the strict args requirement
        """
        e = Event('one', 'two')
        
        def has_locals(one, two):
            three = 3
            return one, three
        
        e += has_locals
        
        actual = list(e(1, 2))
        expected = [
            (1, 3)
        ]
        self.assertEqual(actual, expected)
    
    def test_method(self):
        "Methods add an extra arg 'self' and should not be counted"
        e = Event("one", "two")
        
        class target(object):
            def callme(self, a, b):
                return self, a, b
        
        o = target()
        e += o.callme
        
        actual = list(e(1, 2))
        expected = [
            (o, 1, 2)
        ]
        self.assertEqual(actual, expected)
