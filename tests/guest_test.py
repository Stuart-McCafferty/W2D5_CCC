import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Stuart", 50)
        self.guest2 = Guest("Martina", 100)
        self.guest3 = Guest("Ben", 25)

    def test_guest_has_name(self):
        self.assertEqual("Stuart", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)