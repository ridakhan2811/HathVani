from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .gesture_model.predict import predict_landmarks
import cv2
import numpy as np
import os

def extract_landmarks(img):
    # TODO: Implement actual landmark extraction logic
    # For now, return a dummy value or raise NotImplementedError
    # Example dummy return:
    return img  # Replace with actual landmark extraction

SIGN_TO_MARATHI = {
    'Hello': 'नमस्कार',
    'Thanks': 'धन्यवाद',
    'Yes': 'हो',
    'No': 'नाही',
    'Please': 'कृपया',
}

def index(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(np.frombuffer(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        landmarks = extract_landmarks(img)  # Stub: implement this
        pred = predict_landmarks(landmarks)
        return render(request, 'index.html', {
            'prediction': pred,
            'marathi': SIGN_TO_MARATHI.get(pred, 'माहित नाही'),
        })
    return render(request, 'index.html')

@csrf_exempt
def predict_api(request):
    if request.method == 'POST' and 'image' in request.FILES:
        img = cv2.imdecode(np.frombuffer(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        landmarks = extract_landmarks(img)  # Stub: implement this
        pred = predict_landmarks(landmarks)
        return JsonResponse({
            'prediction': pred,
            'marathi': SIGN_TO_MARATHI.get(pred, 'माहित नाही')
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)
