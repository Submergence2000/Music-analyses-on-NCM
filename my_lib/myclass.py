class Craw_obj():
    """Some values of the object you are crawling"""

    def __init__(self):
        self.site = None
        self.url = None
        self.type = None
        self.id = None
    
    def is_incomplete(self):
        if self.site and self.url and self.type and self.id :
            return 0
        else:
            return 1

    def print_info(self):
        info = "Site: " + self.site + ",\nUrl: " + self.url + ",\nType: " + self.type \
            + ",\nID: " + self.id
        print(info)

class User():
    """Save the information of a NetEase user"""

    def __init__(self, name, usr_id):
        self.name = name
        self.usr_id = usr_id
        self.songs = list()
    
    def print_info(self):
        id_msg = self.usr_id + ": " + self.name
        print(id_msg)
        for index in range(0, len(self.songs)):
            temp_str = self.songs[index].name + " : " + str(self.songs[index].id)
            print(temp_str)
    

class Song():
    """Save the information of a song"""

    def __init__(self, name, music_id):
        self.name = name
        self.id = music_id

    def print_info(self):
        temp_str = self.name + " " + str(self.id)
        print(temp_str)

class Artist():
    """Save the information of the artist"""

    def __init__(self, name):
        self.name = name
        self.songs = []

    def print_songs(self):
        for index in range(0, len(self.songs)):
            temp_str = self.songs[index].name + " : " + str(self.songs[index].id)
            print(temp_str)

class Album(Artist):
    """Save the information of an album"""

    def __init__(self, name, artist):
        super().__init__(name)
        self.artist = artist