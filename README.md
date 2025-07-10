# 🧠 Hospital AR Face Recognition Reception System

A futuristic AI + AR powered web application that uses **real-time face recognition** and **3D augmented reality overlays** to identify patients at a hospital reception and display their medical info (Name, ID, Reason, Last Seen, Disabilities). If the patient is not recognized, a registration form appears via AR. Includes a full **admin panel** for staff to **view, edit, and search** patients by name or ID
## 📸 Live Demo Flow
![ChatGPT Image Jul 7, 2025, 10_33_35 PM](https://github.com/user-attachments/assets/8d87b83e-9369-4763-8b0f-980030f83dac)
![ChatGPT Image Jul 10, 2025, 03_21_18 PM](https://github.com/user-attachments/assets/34752afa-88cd-4575-a67a-68e87c110d57)

> ✅ Patient enters → 📷 Webcam detects face →  
> 🧠 AR overlays show patient name, ID, reason, etc.  
> ❌ Not recognized? → 🆕 Registration overlay appears  
> 👩‍⚕️ Admin can edit or search for any patient manually

---
![ChatGPT Image Jul 10, 2025, 03_05_18 PM](https://github.com/user-attachments/assets/1a877a9d-cfc2-4f7e-9fbe-551ed7552b97)

## ✨ Key Features

- 👁️ Real-time **Face Recognition** using Flask + OpenCV
- 🧠 3D **AR overlays** for patient info using **MindAR + Three.js**
- 🆕 New patient? ➜ **AR Registration Panel**
- 👨‍⚕️ **Admin Panel** to view/update/delete patients
- 🔎 **Manual Search** by Name or Patient ID
- 🧾 MongoDB backend to store patient data + visit history
- 📢 Optional **Text-to-Speech** voice feedback
- 🎨 Stylish, animated **AR HUD interface**

---

## 📊 Patient Info Displayed

- Name  
- Patient ID  
- Reason for Visit  
- Last Seen  
- Disabilities (e.g., Fever, Hearing Impaired)

---

## 🧰 Tech Stack

| Layer        | Tech Used                             |
|--------------|----------------------------------------|
| Frontend     | HTML, CSS, JavaScript, Three.js, MindAR |
| Backend      | Python, Flask, OpenCV, face_recognition |
| Database     | MongoDB (Atlas or Localhost)          |
| AR Engine    | MindAR (Face Tracking) + Three.js     |
| Voice (TTS)  | Web Speech API (Browser)              |

---

## 📂 Folder Structure

```bash
hospital-ar-reception-system/
│
├── frontend/
│   ├── index.html            # AR-based webcam UI
│   ├── script.js             # MindAR + overlay logic
│   ├── style.css             # Custom styles
│   ├── admin.html            # Admin patient management
│   └── register.html         # New patient registration form
│
├── backend/
│   ├── app.py                # Flask API
│   ├── recognize.py          # Face recognition logic
│   ├── register.py           # Handles new registrations
│   ├── database.py           # MongoDB operations
│   └── models/
│       └── encodings.pkl     # Facial encodings
│
├── static/                   # Optional images, fonts, etc               
├── requirements.txt          # Python dependencies
└── README.md                 # Full documentation

1️⃣ Backend (Flask + MongoDB + Recognition)
# Install dependencies
pip install flask face_recognition opencv-python pymongo

# Start server
cd backend
python app.py

2️⃣ Frontend (MindAR AR Interface)
Open frontend/index.html in a browser (Chrome recommended)
Allow webcam permissions
System will:
Scan your face
Match with database
Show patient info in AR if recognized
Show registration panel if not recognized

🔐 Admin Panel
URL: frontend/admin.html
View all registered patients
Edit/update existing info
Search by name or ID
Optionally delete patients

👨‍⚕️ Author
Darko Six_Nimesh Tharaka
AI Engineer | Data Science | Exploring AI, Machine Learning, and Big Data
📧 Gmail-bandaranayakanimesh@gmail.com
🌐 Portfolio-
🔗 LinkedIn-www.linkedin.com/in/nimesh-bandaranayake-0a2912304




