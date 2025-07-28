
from gtts import gTTS
import os

def generate_audio(text, path='media/output.mp3'):
    tts = gTTS(text=text, lang='mr')
    tts.save(path)
    return path
