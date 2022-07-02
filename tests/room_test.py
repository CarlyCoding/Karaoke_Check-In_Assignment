import unittest
from classes.rooms import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room One", 20)
        self.room2 = Room("Room Two", 30)
        self.room3 = Room("Room Three", 15)
        self.room4 = Room("Room Four", 40)


