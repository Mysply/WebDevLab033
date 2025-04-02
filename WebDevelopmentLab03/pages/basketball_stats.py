import streamlit as st
import requests
from datetime import date

# --- Page Setup ---
st.set_page_config(page_title="🏀 NBA Player & Team Info", layout="wide")

# --- Sidebar ---
st.sidebar.title("🔍 Player Search")
player_name = st.sidebar.text_input("Search a Player (e.g. Stephen Curry, Luka Doncic):", "Stephen Curry").strip().lower()

# --- API Setup ---
API_KEY = "832b9662-fac0-4dbf-878d-f7299f3b3a58"
HEADERS = {
    "Authorization": API_KEY
}

st.title("🏀 NBA Player & Team Info")

if player_name:
    url = f"https://api.balldontlie.io/v1/players?search={player_name}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json().get("data", [])
        if data:
            # Find most likely match (check full name match)
            player = next((p for p in data if f"{p['first_name']} {p['last_name']}".lower() == player_name), data[0])
            full_name = f"{player['first_name']} {player['last_name']}"
            team = player['team']['full_name']
            team_id = player['team']['id']

            # --- Player Info ---
            st.subheader(full_name)
            st.write("🏀 Team:", team)
            st.write("📍 Position:", player['position'] or "N/A")

            # --- Height ---
            feet = player.get('height_feet')
            inches = player.get('height_inches')
            if feet is not None and inches is not None:
                st.write("📏 Height:", f"{feet}' {inches}\"")
            else:
                st.write("📏 Height:", "N/A")

            # --- Weight ---
            weight = player.get('weight_pounds')
            st.write("⚖️ Weight:", f"{weight} lbs" if weight is not None else "N/A")

            # --- Recent Team Games ---
            st.subheader("📅 Recent Team Games")
            st.caption("Games by the team — not necessarily the player.")

            start_date = "2023-10-01"
            end_date = date.today().isoformat()
            games_url = f"https://api.balldontlie.io/v1/games?team_ids[]={team_id}&start_date={start_date}&end_date={end_date}&per_page=5"
            games_response = requests.get(games_url, headers=HEADERS)
            games = games_response.json().get("data", [])

            if games:
                for g in games:
                    game_date = g['date'].split("T")[0]
                    home = g['home_team']
                    visitor = g['visitor_team']
                    st.markdown(f"**{game_date}** — {home['full_name']} {g['home_team_score']} vs {visitor['full_name']} {g['visitor_team_score']}")
            else:
                st.warning("No recent games found.")
        else:
            st.warning("No players found with that name.")
    else:
        st.error("API error. Check your key or try again later.")
