import unittest
from epevents.utils import check_missing, ArgsError

class check_missing_test(unittest.TestCase):
    
    def test(self):
        args = ['a','b','c']
        verify = [1,2,3]
        self.assertTrue(check_missing(args, verify) is None)
    
    
    def test_missing(self):
        args = ['one', 'two', 'three']
        verify = [1, 2]
        
        self.assertRaises(ArgsError, lambda: check_missing(args, verify))
        
        actual = ""
        try:
            check_missing(args, verify)
        except ArgsError as e:
            actual = str(e)
        
        self.assertTrue("three" in actual, "missing arg not reported")
    
    
    def test_extra(self):
        args = ['one', 'two', 'three']
        verify = [1, 2, 3, 4]
        
        self.assertRaises(ArgsError, lambda: check_missing(args, verify))
        
        actual = ""
        try:
            check_missing(args, verify)
        except ArgsError as e:
            actual = str(e)
        
        self.assertTrue("4" in actual, "excessive arg not reported")
