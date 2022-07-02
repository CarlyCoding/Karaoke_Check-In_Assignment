import unittest
from classes.caraoke import Caraoke

class TestCaraoke(unittest.TestCase):

    def setUp(self):
        self.caraoke = Caraoke("Be Sharps", 6500)
        
    def test_caraoke_has_name(self):
        self.assertEqual("Be Sharps", self.caraoke.name)

    def test_caraoke_has_till(self):
        self.assertEqual(6500, self.caraoke.till)

    
        
