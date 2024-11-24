import os
import streamlit as st

def show_gallery():
    # Injecting custom CSS styles
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    .title {
        color: #4A628A;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Poppins', sans-serif;
    }

    .subtitle {
        color: #4A628A;
        text-align: center;
        font-size: 28px;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }

    .description {
        color: #4A628A;
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
        font-family: 'Poppins', sans-serif;
    }

    .section-title {
        color: #4A628A;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }

    .image-container {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    image_path = os.path.join(project_root, 'assets', 'asl.png')
    
    image_path2 = os.path.join(project_root, 'assets', 'alph.jpg')
    
    # Title: ASL Alphabet Gallery
    st.markdown('<div class="title">ASL Alphabet Gallery</div>', unsafe_allow_html=True)
    
    st.image(image_path, use_column_width=True)
    
    # Subtitle: Developer Information
    st.markdown('<div class="section-title">Our Developers Are Working Hard</div>', unsafe_allow_html=True)
    
    # Description for developers working on the project
    st.markdown('<div class="description">Our developers are continuously improving and adding new features to the ASL learning experience. Stay tuned for more updates!</div>', unsafe_allow_html=True)
    
    st.image(image_path2, use_column_width=True)
