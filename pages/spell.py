import pickle
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import random
import streamlit as st
import time

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

# Load the CSV file containing words for different difficulty levels
word_df = pd.read_csv('data/words.csv')

# Difficulty selection (this will be used for the Word Spelling Game)
difficulty_map = {"Easy": "easy", "Normal": "normal", "Advanced": "advanced"}

# Function to pick a new word based on the selected difficulty
def get_new_word(difficulty):
    selected_difficulty_column = difficulty_map[difficulty]
    return random.choice(word_df[selected_difficulty_column])

# Function to display word progress
def display_word_status(target, index, is_wrong):
    styled_word = ""
    for i, char in enumerate(target):
        if i < index:  # Correctly spelled letters
            styled_word += f"<span style='color: green;'>{char}</span>"
        elif i == index:  # Current letter being spelled
            color = "red" if is_wrong else "blue"
            styled_word += f"<span style='color: {color};'>{char}</span>"
        else:  # Remaining letters
            styled_word += f"<span style='color: black;'>{char}</span>"
    return f"<h2>{styled_word}</h2>"

# Main function for the ASL Word Spelling Game
def show_spell():
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
    
    # Real-Time ASL Word Spelling Game
    st.title("Real-Time ASL Word Spelling Game")
    st.write("Spell the target word using ASL gestures.")

    # Difficulty selection
    difficulty = st.selectbox("Select Difficulty", ["Easy", "Normal", "Advanced"])

    # Variables to store current state
    current_index = 0  # Current letter index in the target word
    time_detected = 0  # Timer for detecting a stable letter
    last_detected_letter = None
    frame_placeholder = st.empty()
    output_placeholder = st.empty()
    status_placeholder = st.empty()
    timer_placeholder = st.empty()

    # Create a two-column layout
    col1, col2 = st.columns(2)

    # Left column: Word display and buttons
    with col1:
        st.markdown("### Word to Spell")
        status_placeholder = st.empty()
        timer_placeholder = st.empty()

        # Add the "Change Word" button
        change_word_button = st.button("Change Word")

        # If the button is clicked, reset the game state and pick a new word
        if change_word_button:
            target_word = get_new_word(difficulty)
            current_index = 0
            time_detected = 0
            last_detected_letter = None
            # Reset the word status display with the new word
            status_placeholder.markdown(display_word_status(target_word, current_index, False), unsafe_allow_html=True)

    # Right column: Camera feed
    with col2:
        st.markdown("### Camera Feed")
        frame_placeholder = st.empty()

    # Initial target word display
    target_word = get_new_word(difficulty)
    status_placeholder.markdown(display_word_status(target_word, current_index, False), unsafe_allow_html=True)

    # Initialize video capture
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    # Detection variables
    detection_timer = 30  # Frames to confirm a letter (e.g., 1 second at 30 FPS)

    # Game loop
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Initialize is_wrong for the current loop iteration
        is_wrong = False

        # Convert frame to RGB for MediaPipe
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

                # Check for letter stability
                if predicted_character == last_detected_letter:
                    time_detected += 1
                else:
                    last_detected_letter = predicted_character
                    time_detected = 0

                # Confirm letter detection after stability
                if time_detected >= detection_timer:
                    current_letter = target_word[current_index].upper()

                    if predicted_character == 'space':
                        predicted_character = ' '  # Change 'space' to a space character

                    if predicted_character == current_letter:
                        # Correct letter
                        current_index += 1
                        time_detected = 0
                        last_detected_letter = None

                        if current_index == len(target_word):
                            # Word completed
                            status_placeholder.markdown("<h2 style='color: green;'>🎉 Word Completed! 🎉</h2>", unsafe_allow_html=True)
                            st.balloons()
                            break
                    else:
                        # Incorrect letter
                        is_wrong = True

                    # Update word status display
                    status_placeholder.markdown(display_word_status(target_word, current_index, is_wrong), unsafe_allow_html=True)

                # Update the timer display
                timer_placeholder.text(f"Counting... {time_detected / 30:.1f} seconds")

                # Draw bounding box and character on frame
                H, W, _ = frame.shape
                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10
                x2 = int(max(x_) * W) + 10
                y2 = int(max(y_) * H) + 10
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)

        # Display the video feed to the user
        frame_placeholder.image(frame, channels="BGR", use_column_width=True)

        # Check if the word is fully spelled
        if current_index >= len(target_word):
            st.success(f"Congratulations! You spelled the word correctly.")
            break  # End the game if the word is completed

    cap.release()
