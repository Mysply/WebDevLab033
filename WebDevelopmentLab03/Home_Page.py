import streamlit as st

# PAGE CONFIGURATION 
st.set_page_config(page_title="Web Development Lab03", page_icon="🏀", layout="wide")

# PAGE STYLING 
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

#PAGE CONTENT
st.title("Web Development Lab03")
st.header("CS 1301")
st.subheader("Team Maya and William, Web Development - Section B")
st.subheader("🏀William Alvarez, Maya Matthews🏀")

#  LOAD IMAGE 
from PIL import Image
# Display image
try:
    image = Image.open("lebronn.jpeg")
    st.image(image, caption="King James in Action", use_column_width=True)
except FileNotFoundError:
    st.error("Image file 'lebronn.jpeg' not found. Make sure it's in the same folder.")

# INTRODUCTION 
st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **🏀Home Page**: Use this page to navigate to other pages and find descriptions on what the App can do!
2. **🏀Basketball Data Retrieval**: This page retrieves and displays data from the NBA. Just type in a player name and let it work.
3. **🏀Gemini Assisted Data**: Gemini helps in curating functional data based on user inputs.
4. **🏀NBA StatBot**: The StatBot will be able to create responses based on NBA statistics to have a conversation with the user.
""")

# --- USER INPUT ---
favoritePlayer = st.text_input("Who is your favorite NBA player?")
if favoritePlayer:
    st.write(f"Nice choice! {favoritePlayer} is an all-time great!")
