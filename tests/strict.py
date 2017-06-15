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
        self.assertRaises(ArgsError, lambda: Event('one', 'one', 'three'))
