# collect_data.py
import cv2
import mediapipe as mp
import pandas as pd
import os

# Create save directory
save_dir = "collected_csvs"
os.makedirs(save_dir, exist_ok=True)

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture from webcam
cap = cv2.VideoCapture(0)

gesture_label = input("✋ Enter gesture label (e.g., Hello): ")
print(f"[INFO] Starting data collection for '{gesture_label}'...")

max_samples = 100
count = 0
data = []

while cap.isOpened() and count < max_samples:
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Capture 63 values
            row = []
            for lm in hand_landmarks.landmark:
                row.extend([lm.x, lm.y, lm.z])

            row.append(gesture_label)
            data.append(row)
            count += 1
            print(f"[{count}/{max_samples}] samples collected", end='\r')

    cv2.imshow("Hathvani - Gesture Recorder", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(f"\n✅ Finished collecting {count} samples for '{gesture_label}'.")

# Save CSV
columns = [f'{axis}{i}' for i in range(21) for axis in ['x', 'y', 'z']] + ['label']
df = pd.DataFrame(data, columns=columns)
csv_path = os.path.join(save_dir, f"gesture_{gesture_label}.csv")
df.to_csv(csv_path, index=False)
print(f"📁 Data saved to {csv_path}")

cap.release()
cv2.destroyAllWindows()
