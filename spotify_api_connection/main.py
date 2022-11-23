import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser



CLIENT_ID = "8e8557def4d04133b5292c5838ec0716"
CLIENT_SECRET = "a1b6bc5c9d594bc1ad9ead96898797e4"

token = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
cache_token = token.get_access_token()
sp = spotipy.Spotify(cache_token)
spotify = spotipy.Spotify(auth_manager=token)




def get_data(songName:str, outputType:str = 'songList' ,inputType:str = 'artist'):

    results = spotify.search(q=f'{inputType}:' + songName, type=inputType)
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]
        url = artist['external_urls']['spotify']

        webbrowser.open(url, new=2)






get_data("Kendrick Lamar")
#get_song_data(input("Artists name?"))



