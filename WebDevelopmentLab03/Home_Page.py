import streamlit as st

# Title of App
st.title("Web Development Lab03")

# Assignment Data
# TODO: Fill out your team number, section, and team members

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

st.header("CS 1301")
st.subheader("Team Maya and William, Web Development - Section B")
st.subheader("🏀William Alvarez, Maya Matthews🏀")

st.image("images/lebron.jpg")

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **🏀Home Page**: Use this page to navigate to other pages and find descriptions on what the App can do!
2. **🏀Basketball Data Retrieval**: This page retrieves and displays data from the NBA. Just type in a player name and let it work.
3. **🏀Gemini Assisted Data**: Gemini helps in curating functional data based on user inputs.
4. **🏀NBA StatBot**: The StatBot will be able to created responses based on NBA statistics to have a conversation with the user.

""")

favoritePlayer = st.text_input("Who is your favorite NBA player?")
if favoritePlayer:
    st.write(f"Nice choice! {favoritePlayer} is an all time great!")


