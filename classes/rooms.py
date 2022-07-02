from getpass import getuser
from classes.guest import Guest


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





        


