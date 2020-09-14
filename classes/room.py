class Room:
    
    def __init__(self, name, price, capacity, entry_fee):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []
           
    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):  # add guest function
        self.guests.append(guest)

    def check_out_guest(self, guest):  # remove guest function
        self.guests.remove(guest)

    def song_count(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)
    
    def check_capacity(self):
        if self.guest_count > 3:
            return True
        return False
    