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

<img width="1710" alt="Screenshot 2025-03-02 at 09 33 35" src="https://github.com/user-attachments/assets/2b63e0aa-9c36-4dac-8d07-f80ef1354e53" />
<img width="1710" alt="Screenshot 2025-03-02 at 09 33 39" src="https://github.com/user-attachments/assets/3041c347-2fdb-4ece-8d31-d2b855916508" />
<img width="1710" alt="Screenshot 2025-03-02 at 09 23 15" src="https://github.com/user-attachments/assets/3725d4f3-66e2-44ed-8dc6-b99114af7074" />

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
