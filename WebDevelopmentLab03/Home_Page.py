import streamlit as st



# --- Page Config ---
st.set_page_config(page_title="🏀 NBA Stats Hub", layout="centered")

# --- Header ---
st.title("🏀 Web Development Lab 03: NBA Team & Player Info")
st.markdown("**Powered by [BallDontLie API](https://www.balldontlie.io/)** (Free Tier)")

# --- Team Info ---
st.markdown("""
### 📚 CS 1301 – Team XX, Section X  
**Team Members:**  
- Team Member 1  
- Team Member 2
""")

# --- What This App Does ---
st.markdown("""
### 📌 What This App Can Do

Welcome to our NBA Stats App! Use the sidebar to explore:

- 🏀 **Player & Team Info**
  - Search for an NBA player (like **Curry** or **Luka**)
  - See their **current team**, **height**, and **position**
  - View **recent games played by their team**

⚠️ **Note:** This app uses the free tier of the BallDontLie API, so game stats are **team-based**, not player-specific.
""")

# --- Season Info ---
st.markdown("""
### 📅 Season Info

This app displays games and stats from the **2022–2023 NBA season** only.

> 🗓️ **Why only 2022–2023?**  
We're using the **free tier** of the BallDon'tLie API, which only provides data up to the **22–23 season**.  
Live or future data (like 2024–25 stats) requires a premium API or another source.
""")

# --- How To Use It ---
st.markdown("""
### 🧠 How To Use It

1. Start typing a player's name in the search bar (e.g. `"tatum"`, `"morant"`)
2. Select a player and view their info
3. Scroll to see the **5 most recent games** played by their team  
4. Use the sidebar on the left to get started →
""")

# Optional button
if st.button("Go to Player Search"):
    st.info("Use the sidebar to click into the 'NBA Stats Viewer' page.")
