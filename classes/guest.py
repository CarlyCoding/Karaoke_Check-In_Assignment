from getpass import getuser
from classes.caraoke import Caraoke

class Guest: 
    def __init__(self, _name, _wallet):
        self.name = _name
        self.wallet = _wallet
        

    def can_guest_pay_entry_fee(self):
        if self.wallet >= 20:
            return True
        else:
            return False
# In hindsight..could have used a variable from Caraoke class with the entry fee of 20 to make this nicer...!

