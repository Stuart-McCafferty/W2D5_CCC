import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("In my mind", "Gino", "blah blah blah")

    def test_song_has_name(self):
        self.assertEqual("In my mind", self.song.songName)

    def test_song_has_artist(self):
        self.assertEqual("Gino", self.song.songArtist)
    
    def test_song_has_lyrics(self):
        self.assertEqual("blah blah blah", self.song.songLyrics)