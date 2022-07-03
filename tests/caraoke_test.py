import unittest
from classes.caraoke import Caraoke
from classes.guest import Guest

class TestCaraoke(unittest.TestCase):

    def setUp(self):
        self.caraoke = Caraoke("Be Sharps", 6500, 20)
        
    def test_caraoke_has_name(self):
        self.assertEqual("Be Sharps", self.caraoke.name)

    def test_caraoke_has_till(self):
        self.assertEqual(6500, self.caraoke.till)

    def test_entry_fee(self):
        self.assertEqual(20, self.caraoke.entry_fee)

    