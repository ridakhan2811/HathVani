import os
import uuid
import cv2
import numpy as np
from gtts import gTTS
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import mediapipe as mp

from .gesture_model.predict import predict_landmarks

# Marathi translations
SIGN_TO_MARATHI = {
    'Hello': 'नमस्कार',
    'Thankyou': 'धन्यवाद',
    'Yes': 'हो',
    'No': 'नाही',
    'Please': 'कृपया',
    'Sorry': 'माफ करा',
    'Water': 'पाणी',
    'Food': 'अन्न',
    'Hungry': 'भूक',
    'Name': 'नाव',
    'Need': 'गरज',
    'Go': 'जा',
    'Come': 'या',
    'Doctor': 'डॉक्टर',
    'Sit': 'बस',
    'Cancel': 'रद्द करा',
    'Wait': 'थांबा',
    'Sin': 'पाप',
    'Good Morning': 'शुभ सकाळ',
    'Good Evening': 'शुभ संध्या',
    'Goodbye': 'निरोप',
    'Meet': 'भेटा',
    'Fine': 'ठीक आहे',
    'Namaste': 'नमस्ते',
    'Secret': 'गुप्त',
}

# Mediapipe Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

# Extract landmarks using Mediapipe
def extract_landmarks(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    if results.multi_hand_landmarks:
        landmarks = []
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
        return landmarks
    return None

# Convert Marathi text to speech (gTTS) and return audio path
import os
from gtts import gTTS
from django.conf import settings

def speak_marathi_text(text, filename='output.mp3'):
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)  # ensures 'media/' exists

    path = os.path.join(settings.MEDIA_ROOT, filename)
    tts = gTTS(text=text, lang='mr')
    tts.save(path)  # save mp3 to correct full path

    return settings.MEDIA_URL + filename  # returns /media/output.mp3


# Home page view for testing (POST via form)
def index(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(
            np.frombuffer(request.FILES['image'].read(), np.uint8),
            cv2.IMREAD_COLOR
        )
        landmarks = extract_landmarks(img)
        if landmarks is None:
            return render(request, 'index.html', {'error': '✋ No hand detected!'})

        pred = predict_landmarks(landmarks)
        marathi = SIGN_TO_MARATHI.get(pred, 'माहित नाही')
        audio_path = speak_marathi_text(marathi)

        return render(request, 'index.html', {
            'prediction': pred,
            'marathi': marathi,
            'audio_file': audio_path
        })

    return render(request, 'index.html')

# Real-time prediction API (called by JS every 2 seconds)
@csrf_exempt
def predict_api(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(
            np.frombuffer(request.FILES['image'].read(), np.uint8),
            cv2.IMREAD_COLOR
        )
        landmarks = extract_landmarks(img)
        if landmarks is None:
            return JsonResponse({'error': 'No hand detected'}, status=400)

        pred = predict_landmarks(landmarks)
        marathi = SIGN_TO_MARATHI.get(pred, 'माहित नाही')

        # Generate unique audio filename to prevent browser caching
        filename = f"{uuid.uuid4()}.mp3"
        audio_url = speak_marathi_text(marathi, filename)

        return JsonResponse({
            'prediction': pred,
            'marathi': marathi,
            'audio_url': audio_url
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
