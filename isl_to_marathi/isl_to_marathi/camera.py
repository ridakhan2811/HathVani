
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

def extract_landmarks(frame):
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1) as hands:
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                landmarks = []
                for lm in hand.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])
                return landmarks
    return None
