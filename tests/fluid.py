import unittest
from epevents import Fluid as Event

class Fluid_test(unittest.TestCase):
    def test(self):
        e = Event()
        e += lambda one, two, three: (three, two, one)
        e += lambda one, two, three, four: (three, four)
        
        actual = list(e(1, 2, 3, 4, 5, 6))
        expected = [
            (3, 2, 1),
            (3, 4)
        ]
        
        self.assertEqual(actual, expected)
        
