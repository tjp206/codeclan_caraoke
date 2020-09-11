import unittest
from classes.guest import Guest 
from classes.room import Room 
from classes.song import Song 

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room('Penthouse')
        self.guest = Guest('Ayla', 100.00)
        self.song = Song('Ed Sheeran - Dive')

    def test_guest_count(self):
        self.assertEqual(0, self.room.guest_count())

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, self.room.guest_count())

    def test_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0 ,self.room.guest_count())

    def test_song_count(self):
        self.assertEqual(0, self.room.song_count())

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song)
        self.assertEqual(1, self.room.song_count())

    
