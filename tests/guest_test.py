import unittest
from classes.guest import Guest 
from classes.room import Room 
from classes.song import Song 

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest('TJ', 100.00)
        self.room = Room('Smooth Room', 50.00, 3, 5.00)

    def test_check_guest_name(self):
        self.assertEqual('TJ', self.guest.name)

    def test_check_guest_cash(self):
        self.assertEqual(100.00, self.guest.cash)

    def test_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.room)
        self.assertEqual(95.00, self.guest.cash)

        

