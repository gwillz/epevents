import unittest, threading
from epevents import Event


class Event_test(unittest.TestCase):
    def setUp(self):
        self.event = Event()
    
    def tearDown(self):
        self.event = None
    
    def test_regular(self):
        self.event.add(lambda s, a: a)
        self.event.add(lambda s, b: b)
        
        actual = self.event.fire(self, "a")
        expected = ('a', 'a')
        
        self.assertEqual(actual, expected)
    
    def test_magic(self):
        self.event += lambda s, a: a
        self.event += lambda s, b: b
        
        actual = self.event(self, "a")
        expected = ('a', 'a')
        
        self.assertEqual(actual, expected)
        
    def test_clear(self):
        expected1 = lambda a: a
        expected2 = lambda a: a
        
        self.event += expected1
        self.event += expected2
        
        self.assertTrue(expected1 in self.event)
        self.assertTrue(expected2 in self.event)
        
        self.event.remove(expected1)
        self.assertTrue(expected1 not in self.event)
        self.assertTrue(expected2 in self.event)
        
        self.event.clear()
        self.assertTrue(expected1 not in self.event)
        self.assertTrue(expected2 not in self.event)
        
