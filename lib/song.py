import ipdb
class Song:
    # create class attribute
    count = 0
    genres = []
    artists = []
    # class attribute genre_count is a dictionary
    # in this dictionary, key is genre, value is count of songs in the genre
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        # setting genre attribute for single instance of Song class
        self.genre = genre
        self.add_song_to_count()
        # adding genre to Song class genres list
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    # define class method-> @classmethod is a decorator that adds
    # functioality to the method add_song_to_count()
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
        # cls keyword regers to the entire class itself, 
        # not an instance of that class
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            # ipdb.set_trace()

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod      
    # has nothing to do with song counts  
    def add_to_genre_count(cls, genre):
        # if dictionary contains genre then add 1 to its value
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
            # ipdb.set_trace()
        # if dictionary doesn't contain that genre then set value to 1
        else:
            cls.genre_count[genre] = 1
            # ipdb.set_trace()
    @classmethod  
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1