import unittest
from classes.songs import Songs

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Songs("Immigrant Song", "Led Zeppelin")
        self.song2 = Songs("Song 2", "Blur")
        self.song3 = Songs("Lola", "The Kinks")
        self.song4 = Songs("Someone like you", "Adele")
        self.song5 = Songs("Girl all the bad guys want", "Bowling for Soup")
        self.song6 = Songs("Don't tell me", "Madonna")
        self.song7 = Songs("Tribute", "Tenacious D")
