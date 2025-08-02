# test_oneinchdex.py
"""
Tests for OneInchDex module.
"""

import unittest
from oneinchdex import OneInchDex

class TestOneInchDex(unittest.TestCase):
    """Test cases for OneInchDex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OneInchDex()
        self.assertIsInstance(instance, OneInchDex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OneInchDex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
