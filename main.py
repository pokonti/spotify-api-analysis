import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import os

from dotenv import load_dotenv  # Load environment variables from .env file
load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:8888'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-read-collaborative"
    )
)

# user_info = sp.current_user()
# print("Logged in as:", user_info["display_name"])

# saved_tracks = sp.current_user_saved_tracks(limit=10)

# for item in saved_tracks["items"]:
#     track = item["track"]
#     print(track["name"], "-", track["artists"][0]["name"])


# recently_played = sp.current_user_recently_played(limit=10)
# tracks = recently_played["items"]

# for track in tracks:
#     print(track["track"]["name"], "-", track["track"]["artists"][0]["name"])

# Function to get playlist songs
def get_playlist_tracks(playlist_id):
    try:
        results = sp.playlist_tracks(playlist_id)
        if not results or 'items' not in results:
            st.warning("⚠️ No tracks found! The playlist may be unavailable.")
            return None

        tracks = results['items']
        song_data = []
        for item in tracks:
            track = item['track']
            song_data.append({
                "Song": track['name'],
                "Artist": track['artists'][0]['name'],
                "Album": track['album']['name'],
                "Release Date": track['album']['release_date'],
                "Popularity": track['popularity']
            })
        
        return pd.DataFrame(song_data)

    except spotipy.exceptions.SpotifyException as e:
        st.error(f"Spotify API Error: {e}")
        return None

# Get user's playlists
playlists = sp.current_user_playlists()

# Print playlists
# for playlist in playlists['items']:
#     print(f"🎵 {playlist['name']} (ID: {playlist['id']})")

playlist_options = {playlist['name']: playlist['id'] for playlist in playlists['items']}

st.title("🎵 Spotify Playlist Explorer")

# Get user info
user_info = sp.current_user()
st.write(f"Logged in as: **{user_info['display_name']}**")

# Playlist selection dropdown
selected_playlist = st.selectbox("Select a Playlist", list(playlist_options.keys()))

if selected_playlist:
    playlist_id = playlist_options[selected_playlist]
    st.subheader(f"📜 Songs in '{selected_playlist}'")
    df = get_playlist_tracks(playlist_id)
    
    if df is not None:
        st.dataframe(df)

        # Visualization: Popularity Bar Chart
        st.subheader("🔥 Song Popularity Chart")
        st.bar_chart(df.set_index("Song")["Popularity"])

       # Most Frequent Artists - Horizontal Bar Chart
        st.subheader("🎤 Top Artists in the Playlist")

        artist_counts = df["Artist"].value_counts().head(10)  # Top 10 artists
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(y=artist_counts.index, x=artist_counts.values, palette="coolwarm", ax=ax)
        ax.set_xlabel("Number of Songs")
        ax.set_ylabel("Artist")
        ax.set_title("Top Artists in Playlist")
        st.pyplot(fig)

        # Album Distribution - Bar Chart
        st.subheader("💿 Album Distribution")

        album_counts = df["Album"].value_counts().head(10)  # Top 10 albums
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=album_counts.index, y=album_counts.values, palette="viridis", ax=ax)
        ax.set_xlabel("Album")
        ax.set_ylabel("Number of Songs")
        ax.set_title("Top Albums in Playlist")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")  # Rotate for better readability
        st.pyplot(fig)

        # Popularity vs. Release Year Scatter Plot
        st.subheader("📅 Popularity vs. Release Year")

        # Convert Release Date column to datetime (handling different formats)
        df["Release Year"] = pd.to_datetime(df["Release Date"], format="mixed", errors="coerce").dt.year


        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x=df["Release Year"], y=df["Popularity"], color="purple", alpha=0.6, ax=ax)
        ax.set_xlabel("Release Year")
        ax.set_ylabel("Popularity Score")
        ax.set_title("Popularity of Songs Over Time")
        st.pyplot(fig)
