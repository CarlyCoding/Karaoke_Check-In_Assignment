import unittest
from classes.rooms import Rooms

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Rooms("Room One", 20)
        self.room2 = Rooms("Room Two", 30)
        self.room3 = Rooms("Room Three", 15)
        self.room4 = Rooms("Room Four", 40)

    


