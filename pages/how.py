import os
import streamlit as st

# Function to resolve image paths dynamically
def get_image_path(filename):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(project_root, 'assets', filename)

def show_how():
    # Injecting custom CSS styles
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .title {
        color: #029975;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Poppins', sans-serif;
    }

    .subtitle {
        color: #029975;
        text-align: center;
        font-size: 28px;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }

    .description {
        color: #029975;
        text-align: left;
        font-size: 18px;
        margin-bottom: 30px;
        font-family: 'Poppins', sans-serif;
    }

    .section-title {
        background-color: #039a75;  /* New background color */
        border-radius: 10px;        /* Rounded corners */
        padding: 10px;              /* Padding */
        margin-bottom: 15px;        /* Margin at the bottom */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Box shadow */
        color: white;               /* Text color */
        font-size: 24px;            /* Smaller section title */
        font-weight: bold;
        text-align: center;
        width: auto;                /* No longer spans full width */
        font-family: 'Poppins', sans-serif;
    }

    .section-title:hover {
        transform: scale(1.03);  /* Increases size on hover */
        cursor: pointer;       /* Changes cursor to pointer */
    }

    .section-text {
        margin: 20px;
        font-family: 'Poppins', sans-serif;
    }

    .color-blue {
        color: blue;
    }

    .color-green {
        color: green;
    }

    .color-red {
        color: red;
    }

    .section-image {
        width: 400px;
        display: block;
        margin: 0 auto;
    }

    ol.description {
        font-size: 18px;
        line-height: 1.6;
        font-family: 'Poppins', sans-serif;
    }

    .image-caption {
        text-align: center;
        font-size: 18px;
        color: #029975;
    }
    
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the page
    st.markdown('<div class="title">How to Play the Spelling Game</div>', unsafe_allow_html=True)

    # Explanation of the game
    st.markdown('<div class="section-title">Game Rules</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])  # Adjusted column ratio for image
    with col1:
        st.markdown("""
            <p class="description">
                This is a fun and interactive spelling game to practice ASL. Here's how it works:
            <ol class="description">
                <li><span class="color-blue">Blue</span> means you have to spell the letter or word.</li>
                <li><span class="color-green">Green</span> means you have spelled the letter or word correctly!</li>
                <li><span class="color-red">Red</span> means you spelled it wrong. Try again!</li>
            </ol>
            </p>
            <p class="description">
                You can select from three difficulty levels:
            
            <ol class="description">
                <li><strong>Easy</strong>: Short words.</li>
                <li><strong>Normal</strong>: Medium-length words or sentences. An extra 'space' input will be required to be signed.</li>
                <li><strong>Advanced</strong>: Longer, more complex words or sentences. An extra 'space' input will be required to be signed.</li>
            </ol>
            </p>
            <p class="description">
                Make sure you hold the sign for 1 second for it to register.
                <br>
                <br>
                If the word or sentence becomes too hard, simply click the "Change Word" button to randomly pick a new word of the same difficulty level.
            </p>
            <p class="description">
                To start playing, choose <strong>Spelling Game</strong> on the navigation bar.
            </p>
        """, unsafe_allow_html=True)
    
    with col2:
        game_image_path = get_image_path('spac.png')  # Ensure this image is in the 'assets' folder
        st.image(game_image_path, width=400)  # Displaying the game image
        st.markdown('<p class="image-caption">Space Sign</p>', unsafe_allow_html=True)  # Caption under the image
