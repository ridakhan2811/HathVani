import os
import uuid
import cv2
import numpy as np
from gtts import gTTS
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .gesture_model.predict import predict_landmarks

import mediapipe as mp

# Marathi translations dictionary
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
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Extract landmarks from image using Mediapipe
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

# Text-to-speech function
def speak_marathi_text(text, filename='output.mp3'):
    tts = gTTS(text=text, lang='mr')
    path = os.path.join(settings.MEDIA_ROOT, filename)
    tts.save(path)
    return settings.MEDIA_URL + filename

# Home page view
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

# API endpoint for AJAX or real-time capture
@csrf_exempt
def predict_api(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(
            np.frombuffer(request.FILES['image'].read(), np.uint8),
            cv2.IMREAD_COLOR
        )
        landmarks = extract_landmarks(img)
        if landmarks is None:
            return JsonResponse({'error': '✋ No hand detected!'}, status=400)

        pred = predict_landmarks(landmarks)
        marathi_translation = SIGN_TO_MARATHI.get(pred, 'माहित नाही')

        # Save audio
        filename = f"{uuid.uuid4()}.mp3"
        tts_path = os.path.join(settings.MEDIA_ROOT, filename)
        tts = gTTS(text=marathi_translation, lang='mr')
        tts.save(tts_path)

        return JsonResponse({
            'prediction': pred,
            'marathi': marathi_translation,
            'audio_file': settings.MEDIA_URL + filename
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
