import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from spotify import * #contact me to know about the packages and libs i built behind this code.
# Spotify credentials and scope
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''
SCOPE = ''

# Authentication and Spotify client instance
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# Customization
user_id = sp.current_user()['id']
playlist_name = 'New_Playlist'
playlist_description = 'Playlist created using Songs from your Given Youtube Playlist ID in YouTube_Data_Pull.py'

#Uncomment this if you want to create a new playlist
playlist = sp.user_playlist_create(user_id, playlist_name, description=playlist_description)
playlist_id = playlist['id']

# If you already have an existing playlist ID, use it
# playlist_id = ''



#You could have used this (below) cod itself but remember there is a rate limit of 10 additions per second by Spotify
# try:
#     sp.playlist_add_items(playlist_id, track_uri)
#     print("Tracks added to the playlist successfully!")
# except spotipy.exceptions.SpotifyException as e:
#     print(f"Spotify API error: {e}")


# Function to add tracks in batches of 10 to avoid rate limits
def add_tracks_in_batches(playlist_id, track_uri, batch_size=10, delay=1):
    for i in range(0, len(track_uri), batch_size):
        batch = track_uri[i:i + batch_size]
        try:
            sp.playlist_add_items(playlist_id, batch)
            print(f"Successfully added tracks to the playlist.")
        except spotipy.exceptions.SpotifyException as e:
            print(f"Spotify API error: {e}")
        # Pause to avoid exceeding the rate limit (10 requests per second)
        time.sleep(delay)


add_tracks_in_batches(playlist_id, track_uri)

# User information and final print statements
user_info = sp.current_user()

print(f"Your Name is: {user_info['display_name']}")
print(f"Tracks added to playlist '{playlist_name}' with playlist ID {playlist_id}.")
