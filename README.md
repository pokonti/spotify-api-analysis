# 🎵 Spotify Artist & Playlist Analyzer

## Overview

This project is a Spotify data analysis tool built with Python and Streamlit, using the Spotify Web API. It provides insights into an artist's popularity, top tracks, and allows playlist exploration with advanced visualizations.

## Features

* 🔍 Artist Analysis: Fetches artist details, top tracks, genres, popularity score, and follower count.

* 📊 Advanced Visualizations:

  * Bar chart showing song popularity.

  * Word cloud for song titles.

* 🎼 Playlist Explorer: Retrieves songs from a selected playlist.

* 🏆 Top Charts Analysis: Displays popular songs from global charts.

## Installation

### Prerequisites

Ensure you have Python installed and set up a Spotify Developer account to obtain API credentials.

### Setup
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/spotify-analyzer.git
   cd spotify-analyzer
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a .env file and add your Spotify API credentials:
   ```
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    REDIRECT_URI=http://localhost:your_host
   ```
4. Run the application:
   ```
   streamlit run main.py
   ```

## Technologies Used

* Python
* Spotipy (Spotify API wrapper)
* Streamlit (Web UI)
* Pandas
* Matplotlib
* Seaborn 
