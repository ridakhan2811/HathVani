from gtts import gTTS
from playsound import playsound
import uuid
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .gesture_model.predict import predict_landmarks
import cv2
import numpy as np
import mediapipe as mp

# Marathi translations
SIGN_TO_MARATHI = {
    'Cancel': 'रद्द करा',
    'Come': 'या',
    'Go': 'जा',
    'Good Evening': 'शुभ संध्या',
    'Good Morning': 'शुभ प्रभात',
    'Hello': 'नमस्कार',
    'Hungry': 'भूक लागली आहे',
    'Meet': 'भेटा',
    'Namaste': 'नमस्ते',
    'Need': 'गरज आहे',
    'Please': 'कृपया',
    'Secret': 'गुपित',
    'Sin': 'पाप',
    'Thankyou': 'धन्यवाद',
    'Water': 'पाणी'
}


# Mediapipe Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Extract 63 hand landmark points
def extract_landmarks(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            row = []
            for lm in hand_landmarks.landmark:
                row.extend([lm.x, lm.y, lm.z])
            return row
    return None

# Home page (with prediction via webcam upload)
from django.conf import settings

def index(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(np.frombuffer(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        landmarks = extract_landmarks(img)
        pred = predict_landmarks(landmarks)
        marathi_text = SIGN_TO_MARATHI.get(pred, 'माहित नाही')

        # 👇 Text-to-Speech (TTS)
        tts = gTTS(text=marathi_text, lang='mr')
        filename = f"{uuid.uuid4()}.mp3"
        audio_path = os.path.join(settings.BASE_DIR, 'media', filename)
        tts.save(audio_path)
        playsound(audio_path)

        return render(request, 'index.html', {
            'prediction': pred,
            'marathi': marathi_text,
        })
    return render(request, 'index.html')


# API for AJAX POST request
@csrf_exempt
def predict_api(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(np.frombuffer(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        landmarks = extract_landmarks(img)
        pred = predict_landmarks(landmarks)
        marathi = SIGN_TO_MARATHI.get(pred, 'माहित नाही')
        return JsonResponse({
            'prediction': pred,
            'marathi': marathi
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
