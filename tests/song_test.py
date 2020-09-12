import unittest
from classes.guest import Guest 
from classes.room import Room 
from classes.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song('Ed Sheeran - Dive')
        self.room = Room('Smooth Room', 50.00, 3, 5.00)
        self.guest = Guest('TJ', 100.00)
        
    
    