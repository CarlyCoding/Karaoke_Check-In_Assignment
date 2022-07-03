from getpass import getuser
from classes.guest import Guest
from classes.songs import Songs


class Room:
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def is_room_full(self):
        if len(self.guests) >= 1:
            return True
        else:
            return False



