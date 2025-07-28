import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
model = joblib.load(MODEL_PATH)

def predict_landmarks(landmark_list):
    input_data = np.array(landmark_list).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]
