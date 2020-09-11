import unittest
from classes.guest import Guest 
from classes.room import Room 
from classes.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.room = Room('Penthouse')
        self.guest = Guest('Ayla')
        self.song = Song('Ed Sheeran - Dive')
    
    