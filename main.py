import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import secret_infos

scope = 'playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secret_infos['client_id'],client_secret=secret_infos['client_secret'],redirect_uri=secret_infos['redirect_uri'],scope=scope))

discover = "https://open.spotify.com/playlist/37i9dQZEVXcSpwmpHTE7Ct?si=6e3c3293fdad4f30"
main = "https://open.spotify.com/playlist/2gtjFGha9y83eEB6AakD3X?si=95a3d65a196c41c5"


tracks = sp.playlist_tracks(discover)
lista_tracks = []
for track in tracks['items']:
    print(track['track']['uri'])
    lista_tracks.append(track['track']['uri'])
#print(lista_tracks)


print('Iniciando a transferência')
sp.playlist_add_items(main, lista_tracks)
print('Transferência Feita!')