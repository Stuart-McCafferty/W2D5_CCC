class Room:
    def __init__(self, _roomID, _maxGuests):
        self.roomID = _roomID
        self.maxGuests = _maxGuests
        self.songPlaying = ""
        self.guestListRoom = []
        self.noGuests = 0

    def add_guest(self, guest):
        if guest.wallet > 10 and self.noGuests < 2:
            self.guestListRoom.append(guest.name)
            guest.wallet -= 5
            self.noGuests += 1

    def remove_guest(self, guest):
        self.guestListRoom.remove(guest.name)
        self.noGuests -= 1
    
    def number_guests_room(self):
        return len(self.guestListRoom)
    
    def add_song(self, song):
        self.songPlaying = ""
        self.songPlaying = song.songName
        return self.songPlaying
    