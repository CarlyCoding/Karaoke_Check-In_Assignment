import unittest
from classes.guest import Guest
from classes.rooms import Room 
from classes.songs import Songs

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room One", 20)
        self.room2 = Room("Room Two", 30)
        self.room3 = Room("Room Three", 15)
        self.room4 = Room("Room Four", 40)
        
        

    def test_room_has_name(self):
        self.assertEqual("Room Two", self.room2.name)

    def test_room_has_price(self):
        self.assertEqual(40, self.room4.price)
    
    def test_guests_can_check_in_room(self):
        self.assertEqual (0,len(self.room2.guests))
        self.room2.check_in_guest(Guest("Marge Simpson", 100))
        self.assertEqual (1, len(self.room2.guests))

    def test_guests_can_check_out_of_room(self):
        guest = Guest("Snake", 600)
        self.room3.check_in_guest(guest)
        self.assertEqual (1, len(self.room3.guests))
        self.room3.check_out_guest(guest)
        self.assertEqual (0, len(self.room3.guests))

    def test_songs_can_be_added_to_rooms(self):
        self.room4.add_song_to_room(Songs("Someone like you", "Adele"))
        self.assertEqual (1, len(self.room4.songs))

