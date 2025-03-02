import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8888"

# Authenticate with Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-library-read"
    )
)

# Streamlit App
st.title("🎤 Spotify Artist Analyzer")

# Get artist input from user
artist_name = st.text_input("Enter Artist Name:", "The Weeknd")

if artist_name:
    results = sp.search(q=artist_name, type="artist", limit=1)
    if results["artists"]["items"]:
        artist = results["artists"]["items"][0]
        artist_id = artist["id"]
        st.subheader(f"🎶 {artist['name']}")
        st.image(artist["images"][0]["url"], width=300)
        st.write(f"**Genres:** {', '.join(artist['genres'])}")
        st.write(f"**Followers:** {artist['followers']['total']}")
        st.write(f"**Popularity Score:** {artist['popularity']}")

        # Fetch top tracks
        top_tracks = sp.artist_top_tracks(artist_id)
        track_data = []
        for track in top_tracks['tracks']:
            track_data.append({
                "Name": track["name"],
                "Popularity": track["popularity"],
                "Album": track["album"]["name"],
                "Release Date": track["album"]["release_date"]
            })
        df = pd.DataFrame(track_data)
        
        # Popularity trend visualization
        st.subheader("📊 Top 10 Songs Popularity")
        fig, ax = plt.subplots()
        df.sort_values(by="Popularity", ascending=True).plot(kind="barh", x="Name", y="Popularity", ax=ax, color="skyblue")
        st.pyplot(fig)
        
        # Album distribution visualization
        st.subheader("📀 Album Distribution")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(y=df["Album"], order=df["Album"].value_counts().index, palette="coolwarm", ax=ax)
        ax.set_xlabel("Number of Songs")
        ax.set_ylabel("Album")
        ax.set_title("Distribution of Top Songs Across Albums")
        st.pyplot(fig)
        
        # Release Date Timeline
        st.subheader("⏳ Release Date Timeline")
        df["Release Date"] = pd.to_datetime(df["Release Date"], errors='coerce')
        df = df.dropna(subset=["Release Date"])
        df = df.sort_values(by="Release Date")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.lineplot(x=df["Release Date"], y=df["Popularity"], marker="o", ax=ax)
        ax.set_xlabel("Release Date")
        ax.set_ylabel("Popularity")
        ax.set_title("Popularity Trend Over Time")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.error("Artist not found. Try another name!")
