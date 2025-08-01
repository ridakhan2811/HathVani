import joblib
import numpy as np
import os

# Load model once at the top (so it's not reloaded every time)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(MODEL_PATH)

def predict_landmarks(landmarks):
    """
    landmarks: a list or numpy array of shape (63,) representing x,y,z of 21 hand points
    returns: predicted label (e.g., 'Hello', 'Thankyou')
    """
    if isinstance(landmarks, list):
        landmarks = np.array(landmarks).reshape(1, -1)
    elif isinstance(landmarks, np.ndarray):
        landmarks = landmarks.reshape(1, -1)
    else:
        raise ValueError("Landmarks must be list or numpy array of shape (63,)")

    prediction = model.predict(landmarks)[0]
    return prediction
