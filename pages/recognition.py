import pickle
import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

# Load model
model_dict = pickle.load(open('model/model.p', 'rb'))
model = model_dict['model']

# MediaPipe Hand Detection Setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3, min_tracking_confidence=0.3)

labels_dict = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
    20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z',
    26: 'space', 27: 'ILY', 28: 'yes'
}

def show_recog():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.title("Real-Time ASL Gesture Recognition")
    st.write("Use your webcam to show ASL gestures.")

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Left column: Reset button and detected word display
    with col1:
        st.markdown("### Controls")
        word_placeholder = st.empty()  # Display the word being spelled
        output_placeholder = st.empty()  # Display detected letters

        # Function to reset the detected word
        def reset_word():
            nonlocal detected_word
            detected_word = ""  # Reset the word
            word_placeholder.empty()  # Clear the word display

        # Add Reset button to the UI
        if st.button("Reset Word"):
            reset_word()

    # Right column: Camera feed
    with col2:
        st.markdown("### Camera Feed")
        frame_placeholder = st.empty()  # Display the camera feed
        timer_placeholder = st.empty()  # Show the timer

    # Initialize video capture and detection variables
    cap = cv2.VideoCapture(2)
    detected_word = ""
    last_detected_letter = None
    time_detected = 0

    # Webcam loop for gesture recognition
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Display the word being spelled in the left column
        with col1:
            word_placeholder.markdown(f"### Spelling: {detected_word}")

        # Process the frame with MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        data_aux, x_, y_ = [], [], []

        # If hand landmarks are detected, process them
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                for i in range(21):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(21):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            # Ensure that only 42 features are passed to the model
            if len(data_aux) == 42:
                prediction = model.predict([np.asarray(data_aux)])
                predicted_character = labels_dict[int(prediction[0])]

                # Check for repeated letters
                if predicted_character == last_detected_letter:
                    time_detected += 1
                else:
                    last_detected_letter = predicted_character
                    time_detected = 0

                # Detect letter after stability
                if time_detected >= 30:  # ~1 second
                    if predicted_character == 'space':
                        detected_word += " "
                    elif predicted_character == 'ILY':
                        detected_word += "❤️"
                        st.balloons()
                    else:
                        detected_word += predicted_character

                    # Display the detected character
                    with col1:
                        output_placeholder.write(f"Spelled Word: {predicted_character}")
                    time_detected = 0  # Reset the timer

                # Draw bounding box and character on the frame
                H, W, _ = frame.shape
                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10
                x2 = int(max(x_) * W) + 10
                y2 = int(max(y_) * H) + 10
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

        # Display the video feed in the right column
        with col2:
            frame_placeholder.image(frame, channels="BGR", use_column_width=True)
            timer_placeholder.text(f"Counting... {time_detected / 30:.1f} seconds")

    cap.release()
