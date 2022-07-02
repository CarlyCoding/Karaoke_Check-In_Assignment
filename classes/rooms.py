from classes.guest import Guest


class Room:
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price
        self.guests = []

    def check_in_guest(self, guest):
        self.guests.append(guest)



        


