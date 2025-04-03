import streamlit as st

# page config
st.set_page_config(page_title="Web Development Lab03", page_icon="🏀", layout="wide")

# page styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #FFE599;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# pages
st.title("🏀 Web Development Lab03: NBA Team & Player Info")
st.header("📚 CS 1301 – Group 14, Section B")
st.subheader("Team Members: William Alvarez & Maya Matthews")

# intro
st.markdown("""
### 📌 What This App Can Do
Welcome to our NBA Stats App! Use the sidebar to explore:

- 🏀 **Player & Team Info**  
  Search for an NBA player (like Curry or Luka)  
  See their current team, height, and position  
  View recent games played by their team !  

- ⚠️ _Side Note_: This app uses the free tier of the BallDontLie API, which includes **team-based game data only up to the 2022–2023 season**. Player stats are not available with this tier.

---

### 🧠 How To Use It
1. Start typing a player's name in the search bar (e.g. `tatum`, `morant`)
2. Select a player and view their info
3. Scroll to see the 5 most recent games played by their team
""")

#pages
st.markdown("""
### 🗂️ Pages Breakdown

1. **🏠 Home Page** – You're here! This is the welcome page with project info and navigation guidance.
2. **📊 Basketball Data Retrieval** – Search a player and see their current team and team’s recent games.
3. **🤖 Gemini Assisted Data** – Uses AI to give suggestions or generate player content based on input.
4. **🧠 NBA StatBot** – A chatbot-style page that answers NBA-related questions using basic logic and stats.
""")

# user interaction
favoritePlayer = st.text_input("Who's your favorite NBA player?")
if favoritePlayer:
    st.success(f"Nice choice! {favoritePlayer} is a legend. 🏀🔥")
