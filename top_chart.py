import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Authenticate with Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://localhost:8888",
        scope="playlist-read-private playlist-read-collaborative"
    )
)

# Function to fetch playlist tracks
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results.get("items", [])

    song_data = []
    for item in tracks:
        track = item["track"]
        song_data.append({
            "Song": track["name"],
            "Artist": track["artists"][0]["name"],
            "Album": track["album"]["name"],
            "Release Date": track["album"]["release_date"],
            "Popularity": track["popularity"]
        })

    return pd.DataFrame(song_data)


playlist_id = "5ABHKGoOzxkaa28ttQV9sE" 
df = get_playlist_tracks(playlist_id)

# Print the top 10 songs
print(df.head(10))


