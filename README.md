🙌 Hathvani

Hathvani is a real-time Indian Sign Language (ISL) to Marathi text and speech converter built with Django, MediaPipe, and machine learning. It captures gestures via webcam, translates them to Marathi using a trained model, and speaks them aloud using TTS — bridging the communication gap between the deaf community and Marathi speakers.

✨ Features

🎥 Real-time hand gesture recognition via webcam

✋ ISL gesture classification using MediaPipe + ML model

📝 Marathi translation of recognized gestures

🔊 Marathi voice output using Google Text-to-Speech (gTTS)

🌐 Django-powered web interface (internal HTML, CSS, JS)

🧰 Tech Stack

🐍 Python 3.10+

🌍 Django – Full-stack web framework

👁️ OpenCV – Webcam frame capture

🤚 MediaPipe – Hand landmark detection

🧠 scikit-learn – Gesture classification model

🔈 gTTS – Marathi text-to-speech

🧾 JavaScript + HTML + CSS – Webcam access, UI

📁 Folder Structure

hathvani/
├── gesture_model/
│   ├── model.pkl              # Trained ML model
│   └── predict.py             # Model inference logic
├── gesture_app/
│   ├── views.py
│   ├── camera.py              # OpenCV + MediaPipe logic
│   ├── mapping.py             # ISL to Marathi dictionary
│   ├── tts.py                 # gTTS integration
│   └── urls.py
├── templates/
│   └── index.html             # UI Template
├── static/
│   └── (Optional static files like JS/CSS)
├── media/
│   └── output.mp3             # Audio file playback
├── manage.py
└── requirements.txt

⚙️ Installation

git clone https://github.com/your-username/hathvani.git
cd hathvani
pip install -r requirements.txt
python manage.py runserver

Ensure:

✅ Your system has a webcam.

🌐 Internet access is enabled for gTTS audio generation.

🗂️ media/ folder is writable for saving MP3s.

🚀 Usage

Open the web app in your browser.

Allow camera access.

Perform an ISL gesture (e.g., Hello, Thank You).

The system will:

🧠 Detect the gesture

📝 Display the Marathi translation

🔊 Speak the word using TTS

👩‍💻 Team

Rida Khan – ML Model, Backend Integration, Mapping, Documentation

Ayush Shinde – Django Setup, Frontend (HTML/CSS/JS), Webcam Logic

🔮 Future Enhancements

🎬 Dynamic (video-sequence) gesture recognition

🧩 Support for additional ISL gestures

🌍 Language expansion beyond Marathi (Hindi, Kannada, Gujarati, etc.)

🧱 Sentence-level construction using gesture combinations

📱 Mobile-friendly UI with progressive web support

📴 Offline TTS integration (for limited connectivity areas)

💡 Purpose

Hathvani is more than a project. It's a step toward inclusive communication — enabling the deaf and hard-of-hearing community to speak in Marathi, through signs and gestures.

🪪 License

MIT License – feel free to fork, use, and contribute.

📹 Demo

A short demo video will be added to showcase the live usage of Hathvani.

