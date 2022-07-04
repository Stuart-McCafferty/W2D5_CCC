import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1,2)
        self.guest = Guest("Stuart", 50)
        self.guest2 = Guest("Martina", 2)
        self.guest3 = Guest("Ben", 25)
        self.guest4 = Guest("Irene", 25)

        self.song = Song("In my mind", "Gino", "blah blah blah")


    
    def test_room_has_ID(self):
        self.assertEqual(1, self.room.roomID)
    
    def test_room_has_maxGuests(self):
        self.assertEqual(2, self.room.maxGuests)
    
    def test_room_has_song_playing(self):
        self.assertEqual("", self.room.songPlaying)
    
    def test_room_has_empty_guest_list(self):
        self.assertEqual([], self.room.guestListRoom)
    
    def test_can_add_customer_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, self.room.number_guests_room())
        self.assertEqual(1, self.room.noGuests)
    
    def test_can_remove_customer_to_room(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, self.room.number_guests_room())

    def test_can_add_song_to_room(self):
        self.assertEqual("In my mind", self.room.add_song(self.song))
    
    def test_guest_cannot_afford_room(self):
        self.room.add_guest(self.guest2)
        self.assertEqual(0, self.room.number_guests_room())
    
    def test_room_is_full(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest3)
        self.room.add_guest(self.guest4)
        self.assertEqual(2, self.room.number_guests_room())
    
    def test_wallet_is_reduced(self):
        self.room.add_guest(self.guest)
        self.assertEqual(45, self.guest.wallet)


