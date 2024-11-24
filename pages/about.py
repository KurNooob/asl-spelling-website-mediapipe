import streamlit as st

def show_about():
    # Injecting custom CSS styles
    st.markdown("""
    <style>
    .stApp {
        background-color: #F9F9F9;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    .section {
        padding: 25px;
        width: 100%; /* Ensures the section spans the full screen width */
        margin: 0; /* Removes any default margins */
        background: none; /* Removes background color */
        box-shadow: none; /* Removes card-like shadow */
        border-radius: 0; /* Removes rounded corners */
    }
    .section:hover {
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2);
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
        text-align: center;
    }
    .section-title:hover {
        transform: scale(1.03);  /* Increases size on hover */
        cursor: pointer;       /* Changes cursor to pointer */
    }
    .section-content {
        font-size: 16px;
        color: #4B5563;
        line-height: 1.8;
        font-family: 'Poppins', sans-serif;
        text-align: justify;
    }
    .developer-card {
        text-align: center;
        margin-top: 20px;
        max-width: 600px; /* Limits card width */
        margin-left: auto;
        margin-right: auto; /* Centers the card */
        padding: 20px;
        border: 1px solid #E5E7EB; /* Optional border for card */
        border-radius: 12px;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
        background-color: #FFFFFF;
    }
    .developer-card img {
        border-radius: 50%;
        width: 130px;
        height: 130px;
        margin-bottom: 15px;
        object-fit: cover;
        border: 3px solid #1E3A8A;
    }
    .developer-name {
        font-size: 24px;
        font-weight: bold;
        color: #1E40AF;
    }
    .developer-role {
        font-size: 16px;
        color: #6B7280;
        font-style: italic;
        margin-bottom: 10px;
    }
    .icon-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 15px;
    }
    .social-icon {
        display: inline-block;
        width: 35px;
        height: 35px;
        background-size: cover;
        transition: transform 0.3s;
    }
    .social-icon.linkedin {
        background-image: url('https://cdn-icons-png.flaticon.com/512/174/174857.png');
    }
    .social-icon.instagram {
        background-image: url('https://cdn-icons-png.flaticon.com/512/2111/2111463.png');
    }
    .social-icon.email {
        background-image: url('https://cdn-icons-png.flaticon.com/512/732/732200.png');
    }
    .social-icon:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Web & Model Information Section
    st.markdown("""
    <div class="section">
        <h2 class="section-title">Web & Model Information</h2>
        <p class="section-content">
            This platform is developed with <strong>Streamlit</strong>, a Python framework for rapid web application development. 
            It incorporates modern <strong>CSS</strong> for enhanced visuals and user experience. 
            We plan to transition this project to <strong>Flask</strong> in the near future to support advanced features and scalability.
        </p>
        <p class="section-content">
            Our model leverages a <strong>Random Forest Classifier</strong>, which is known for its robust performance in machine learning tasks. 
            This model is specifically designed for American Sign Language (ASL) recognition, offering high accuracy and resilience even with noisy datasets.
        </p>
        <p class="section-content">
            The application uses <strong>MediaPipe</strong> to detect and track hand landmarks in real-time. MediaPipe's robust hand-tracking model provides the necessary 21 hand key points to identify various gestures. 
            These key points are then converted into numerical features, such as distances and angles between points, which serve as inputs to our Random Forest Classifier. By combining MediaPipe’s real-time landmark detection capabilities with the Random Forest Classifier’s predictive power, the system can reliably interpret ASL gestures. 
            This integration enables smooth and efficient recognition, making it an excellent tool for improving communication accessibility.
        </p>
        <div class="image-container">
            <img src="https://mediapipe.dev/images/mobile/hand_landmarks.png" alt="MediaPipe Hand Landmarks">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Developer Card Section with Social Icons
    st.markdown("""
    <div class="developer-card">
        <img src="https://pbs.twimg.com/media/Fmcibe-aMAApljr.jpg" alt="Developer Picture">
        <p class="developer-name">Brandon Likurniawan</p>
        <p class="developer-role">Sleep Enthusiast</p>
        <p class="section-content" style="text-align: center; color: #4B5563;">
            Help me, I am lost in a world full of accidents.
        </p>
        <div class="icon-container">
            <a href="mailto:brandonlikurniawan2003@gmail.com" class="social-icon email" aria-label="Email"></a>
            <a href="https://www.linkedin.com/in/brandon-likurniawan/" target="_blank" class="social-icon linkedin" aria-label="LinkedIn"></a>
            <a href="https://www.instagram.com/brandlikoer/" target="_blank" class="social-icon instagram" aria-label="Instagram"></a>
        </div>
    </div>
    """, unsafe_allow_html=True)
