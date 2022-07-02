import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ned Flanders", 200)
        
    def test_guest_has_name(self):
        self.guest =("Ned Flanders",self.guest.name)

    