
class Song:
    '''counts the total number of Song objects.'''
    count = 0
    '''keeps track of all Song genres.'''
    genres = []
    '''keeps track of all Song artists.'''
    artists = []
    '''keeps count of Songs for each genre.'''
    genre_count = {}
    '''keeps count of Songs for each artist.'''
    artist_count = {}

    '''instantiates with a name, artist, and genre.'''
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre


        '''counts the total number of Song objects.'''
        Song.add_song_to_count() 
        '''keeps track of all Song genres.'''
        Song.update_genres(self.genre)
        '''keeps track of all Song artists.'''
        Song.update_artists(self.artist)
        '''keeps count of Songs for each artist.'''
        Song.update_artist_count(self.artist)
        '''keeps count of Songs for each genre.'''
        Song.update_genre_count(self.genre)
        

    '''counts the total number of Song objects.'''
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    '''keeps track of all Song genres.'''
    @classmethod
    def update_genres(cls, genre):
        if genre not in cls.genres: 
            cls.genres.append(genre)

    '''keeps track of all Song artists.'''    
    @classmethod
    def update_artists(cls, artist):
        if artist not in cls.artists: 
            cls.artists.append(artist)
        
    
    '''keeps count of Songs for each artist.'''
    @classmethod
    def update_artist_count(cls, artist, increment=1):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + increment


    '''keeps count of Songs for each genre.'''
    @classmethod
    def update_genre_count(cls, genre, increment=1):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + increment
       

    def __str__(self):
        return f"Song: {self.name} | Artist: {self.artist} | Genre: {self.genre}"


    
    


# song1 = Song("99 Problems", "Jay-Z", "Rap")
# # print(song1.name)
# # print(song1.artist)
# # print(song1.genre)
# print(song1)

# song2 = Song("Mountain", "Roads", "Country")
# # print(song2.name)
# # print(song2.artist)
# # print(song2.genre)
# print(song2)


# print(Song.count)
# print(Song.genres)
# print(Song.artists)

# print(Song.genre_count["Rap"])
# print(Song.artist_count["Jay-Z"])

