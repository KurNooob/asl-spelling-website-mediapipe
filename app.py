import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg  # Ensure this points to the folder with your page scripts

# Configure the app
st.set_page_config(initial_sidebar_state="collapsed", layout='wide')

# Define the pages and their corresponding functions
pages = ["Home", "Gallery", "How to Play", "Free Spelling", "Spelling Game", "About"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "assets", "hand.svg")
urls = {}

# Get the selected page to set the active style
selected_page = st.session_state.get("selected_page", "Home")

# Custom navbar styles
styles = {
    "nav": {
        "background-color": "#dbf9e3",
        "justify-content": "center",  # Center the navbar items
        "align-items": "center",      # Ensure the items are vertically centered
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "black",
        "padding": "14px",
        "font-weight": "bold",  # Make text bold
    },
    "active": {
        "background-color": "#d3f2eb",  # Use hover color for the active item
        "color": "black",  # Ensure text color is black for active item
        "font-weight": "bold",  # Ensure active page text is also bold
        "padding": "14px",
    },
    "hover": {
        "background-color": "#d3f2eb",  # Change background color to #d3f2eb on hover
        "cursor": "pointer",  # Add cursor pointer for hover
    }
}

options = {
    "show_menu": True,
    "show_sidebar": False,
}

# Add the navbar and get the selected page
page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

# Set the selected page in session state
if page != selected_page:
    st.session_state["selected_page"] = page

# Map navbar options to functions
functions = {
    "Home": pg.show_home,
    "Gallery": pg.show_gallery,
    "How to Play": pg.show_how,
    "Free Spelling": pg.show_recog,
    "Spelling Game": pg.show_spell,
    "About": pg.show_about,
    #"Github": pg.show_github,
}

# Call the function associated with the selected page
go_to = functions.get(page)

if go_to:
    go_to()