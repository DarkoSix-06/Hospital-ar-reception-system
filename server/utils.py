import cv2
import dlib
import numpy as np

# Load models (must be in your /server folder)
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

def get_face_encoding(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Failed to read image")
        return None

    # ✅ DEBUG SAVE
    debug_path = "debug_frame.jpg"
    cv2.imwrite(debug_path, img)
    print(f"🖼️ Saved debug frame to {debug_path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    print(f"🧠 Found {len(faces)} face(s)")

    if len(faces) == 0:
        return None

    shape = sp(img, faces[0])
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    return np.array(face_descriptor)

def compare_face_to_database(encoding, known_users, threshold=0.6):
    for user in known_users:
        dist = np.linalg.norm(user["face_encoding"] - encoding)
        if dist < threshold:
            return user
    return None
