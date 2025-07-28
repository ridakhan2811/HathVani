🤝 Hathvani – ISL to Marathi Translator

Hathvani is a real-time system designed to translate Indian Sign Language (ISL) gestures into Marathi text and speech. Built using machine learning, MediaPipe, Django, and Google TTS, it aims to bridge communication gaps for the deaf and hard-of-hearing community in regional language contexts.

🧩 Features

Detect ISL gestures in real-time using webcam

Translate ISL gestures into Marathi text

Convert translated text into Marathi audio output

Simple, browser-based UI using Django + JavaScript

Clean folder structure, modular ML code, and expandable mapping

🧠 Technologies Used

Python (Core ML + Backend)

MediaPipe – Real-time hand tracking

scikit-learn – Classification model for gesture prediction

OpenCV – Webcam feed processing

gTTS – Marathi text-to-speech

Django – Web application backend

HTML + CSS + JS – Frontend logic and UI

Git & GitHub – Version control

📁 Folder Overview

gesture_model/ → Trained ML model & prediction script

gesture_app/ → Views, camera input, dictionary mapping, TTS

templates/ → Frontend HTML

static/ → JS, CSS (if needed)

media/ → Audio output files

requirements.txt → Python dependencies

🛠 Installation & Usage

git clone https://github.com/your-username/hathvani.git
cd hathvani
pip install -r requirements.txt
python manage.py runserver

Visit http://127.0.0.1:8000 in your browser, allow camera access, and try signing!

🔮 Future Scope

Support for dynamic gesture sequences (RNN, LSTM)

Multilingual support: Hindi, Kannada, Gujarati, and more

Mobile-first UI (Progressive Web App)

Offline TTS engine for limited network access

ISL sentence-level translation (combining gesture predictions)

👥 Team Members

Rida Khan 

Ayush Shinde 

⚠️ Disclaimer

This project is made for academic, research, and development purposes. It is not yet verified for use in real-time clinical or public deployments. Further validation and community testing are required.

💼 Mentorship & Vision

Hathvani is envisioned as a real-world accessible tool to empower regional language communication for differently-abled individuals. It may evolve into a mobile and Raspberry Pi-based assistive communication device.

