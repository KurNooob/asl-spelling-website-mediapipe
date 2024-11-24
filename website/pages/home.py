import os
import streamlit as st

# Function to resolve image paths dynamically
def get_image_path(filename):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(project_root, 'assets', filename)

def show_home():
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
        text-align: center; /* Center-align the text */
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Poppins', sans-serif;
    }


    .subtitle {
        color: #029975;
        text-align: left;
        font-size: 28px;
        margin-bottom: 15px;
        font-family: 'Poppins', sans-serif;
    }

    .description {
        color: #029975;
        text-align: left;
        font-size: 20px;
        margin-bottom: 30px;
        font-family: 'Poppins', sans-serif;
    }

    .section-title {
        background-color: #039a75;  /* New background color */
        border-radius: 10px;        /* Rounded corners */
        padding: 15px;              /* Padding */
        margin-bottom: 15px;        /* Margin at the bottom */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); /* Box shadow */
        color: white;               /* Text color */
        font-size: 30px;
        font-weight: bold;
        transition: transform 0.3s ease; /* Smooth transition */
        width: 100%;
        font-family: 'Poppins', sans-serif;
    }

    .section-title:hover {
        transform: scale(1.03);  /* Increases size on hover */
        cursor: pointer;       /* Changes cursor to pointer */
    }

    .section-text {
        flex: 1;
        margin: 20px;
        font-family: 'Poppins', sans-serif;
    }

    .section-image {
        width: 300px;  /* Resize the images to 300px */
    }

    .right-image {
        display: flex;
        justify-content: flex-end;
    }
    
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the page
    st.markdown('<div class="title">Welcome to Our ASL Website</div>', unsafe_allow_html=True)

    # Section 1: What is ASL? (Image on the left)
    st.markdown('<div class="section-title">What is ASL?</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 1, 3])  # Adjusted column ratio
    with col1:
        st.markdown("""
            <p class="description">
                Start by defining what ASL is. American Sign Language is a visual language used primarily by the Deaf and Hard of Hearing community in the United States and parts of Canada. Unlike spoken languages, ASL uses hand shapes, facial expressions, body movements, and spatial relationships to convey meaning. It has its own grammar and structure, distinct from English, and is a vital tool for communication in the Deaf community.
            </p>
        """, unsafe_allow_html=True)
    with col3:
        st.image(get_image_path('home_sign.jpg'), width=400)  # Use specific image

    # Section 2: Why Learn ASL? (Image on the right)
    st.markdown('<div class="section-title">Why Learn ASL?</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 7])  # Adjusted column ratio
    with col1:
        st.image(get_image_path('home_talk.jpg'), width=400)  # Use specific image
    with col2:
        st.markdown("""
            <p class="description">
                Learning ASL opens up opportunities to connect with a vibrant and diverse community. For hearing individuals, it helps break down communication barriers with Deaf and Hard of Hearing people. It's also a great skill for personal, professional, and social growth, making workplaces, schools, and communities more inclusive. Furthermore, it can be a fulfilling personal challenge to learn a new language with a different mode of communication.
            </p>
        """, unsafe_allow_html=True)

    # Section 3: The Importance of ASL (Image on the left)
    st.markdown('<div class="section-title">The Importance of ASL</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 1, 3])  # Adjusted column ratio
    with col1:
        st.markdown("""
            <p class="description">
                ASL is crucial for ensuring equal access to communication and opportunities for the Deaf and Hard of Hearing population. Without ASL, many would face isolation and limitations in education, employment, healthcare, and social interaction. Its importance extends beyond just a means of communication; it's also a cultural cornerstone for the Deaf community, preserving its unique history, values, and identity.
            </p>
        """, unsafe_allow_html=True)
    with col3:
        st.image(get_image_path('home_why.jpg'), width=400)  # Use specific image

    # Section 4: The Growing Global Challenge of Hearing Loss (Image on the right)
    st.markdown('<div class="section-title">The Growing Global Challenge of Hearing Loss</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 7])  # Adjusted column ratio
    with col1:
        st.image(get_image_path('home_data.jpg'), width=400)  # Use specific image
    with col2:
        st.markdown("""
            <p class="description">
                By 2050, nearly 2.5 billion people are projected to have some degree of hearing loss, with 700 million requiring hearing rehabilitation. According to the World Health Organization (WHO), over 5% of the world’s population, or 430 million people, live with disabling hearing loss, including 34 million children. Disabling hearing loss, defined as a loss greater than 35 decibels (dB) in the better ear, is especially prevalent in low- and middle-income countries, where nearly 80% of those affected reside.
            </p>
        """, unsafe_allow_html=True)

    # Section 5: Our Goals (Image on the left)
    st.markdown('<div class="section-title">Our Goals</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 1, 3])  # Adjusted column ratio
    with col1:
        st.markdown("""
            <p class="description">
                The website's primary mission is to provide accessible, accurate resources for learning ASL and to promote awareness about its importance. Our goals include increasing the understanding of ASL among hearing individuals, fostering inclusion, and empowering the Deaf community. We strive to ensure that Deaf, Hard of Hearing, and all disabled individuals are treated equally, accepted, and provided with equal opportunities in all aspects of life.
            </p>
        """, unsafe_allow_html=True)
    with col3:
        st.image(get_image_path('home_cause.jpg'), width=400)  # Use specific image