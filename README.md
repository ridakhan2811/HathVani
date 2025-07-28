# 🤝 Hathvani – ISL to Marathi Translator

**Hathvani** is a real-time system designed to translate Indian Sign Language (ISL) gestures into Marathi text and speech.
Built using machine learning, MediaPipe, Django, and Google TTS, it aims to bridge communication gaps for the deaf and hard-of-hearing community in regional language contexts.

---

## 🧩 Features

* 🎥 Detect ISL gestures in **real-time** using webcam
* 📝 Translate gestures into **Marathi text**
* 🔊 Convert translated text into **Marathi speech** using gTTS
* 🌐 Simple, browser-based UI using **Django + JavaScript**
* 🗃️ Clean folder structure and **modular ML pipeline**

---

## 🧠 Technologies Used

* 🐍 Python – Core ML + backend scripting
* 🖐️ MediaPipe – Real-time hand tracking
* 🧮 scikit-learn – Gesture classification model
* 🎥 OpenCV – Webcam feed capture and processing
* 🗣️ gTTS – Marathi text-to-speech conversion
* 🛠️ Django – Web backend framework
* 🌐 HTML + CSS + JS – UI and frontend logic
* 🗃️ Git & GitHub – Version control and collaboration

---

## 📁 Folder Overview

```
hathvani/
├── gesture_model/       → Trained ML model & prediction logic
├── gesture_app/         → Django views, camera input, dictionary mapping, TTS
├── templates/           → HTML frontend
├── static/              → Optional: JavaScript, CSS
├── media/               → Output audio files
├── requirements.txt     → Python dependencies
└── manage.py
```

---

## 🛠️ Installation & Usage

```bash
git clone https://github.com/ridakhan2811/hathvani.git
cd hathvani
pip install -r requirements.txt
python manage.py runserver
```

🖥 Open browser and visit: `http://127.0.0.1:8000`
📷 Allow webcam access and perform ISL gestures like “Hello” or “Thank you”

---

## 🔮 Future Scope

* 🔁 Support for dynamic gesture sequences (using RNN/LSTM)
* 🌐 Multilingual expansion: Marathi, English, Hindi, Kannada, Gujarati, etc.
* 📱 Mobile-first UI using Progressive Web App (PWA) features
* 📦 Offline TTS support for limited connectivity environments
* 🧩 ISL sentence-level translation (via gesture sequence combinations)

---

## 👥 Team Members

* **Rida Khan** – ML model development, backend integration, TTS, documentation
* **Ayush Shinde** – Django setup, frontend (HTML/CSS/JS), webcam logic

---

## ⚠️ Disclaimer

This project is developed for academic, research, and accessibility purposes.
It is not yet clinically certified for real-world deployment. Further validation is needed.

---

## 💼 Mentorship & Vision

Hathvani is envisioned as a real-world assistive tool for regional language accessibility, enabling communication for the deaf and hard-of-hearing community.
With future extensions, it may be deployed as a mobile app or Raspberry Pi-based embedded device.

---

## 📽️ Demo

🎥 A short demo video will be added here showcasing live gesture translation.
