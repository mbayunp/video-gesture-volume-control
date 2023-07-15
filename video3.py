import cv2
import mediapipe as mp
import math
import numpy as np
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Menginisialisasi OpenCV VideoCapture
cap = cv2.VideoCapture(0)

# Mengatur ukuran jendela tampilan
cv2.namedWindow("Gesture Volume Control", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Gesture Volume Control", 800, 600)

# Mendeteksi tangan
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Gagal membaca frame video")
            break

        # Membalikkan citra
        image = cv2.flip(image, 1)

        # Konversi citra BGR ke RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Mendeteksi tangan pada citra
        results = hands.process(image_rgb)

        # Menggambar landmark dan garis tangan
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),
                )

                # Mendapatkan posisi landmark untuk ibu jari dan telunjuk
                thumb_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Mengubah posisi landmark menjadi koordinat piksel
                thumb_x, thumb_y = int(thumb_landmark.x * image.shape[1]), int(thumb_landmark.y * image.shape[0])
                index_finger_x, index_finger_y = int(index_finger_landmark.x * image.shape[1]), int(
                    index_finger_landmark.y * image.shape[0])

                # Menggambar garis antara ibu jari dan telunjuk
                cv2.line(image, (thumb_x, thumb_y), (index_finger_x, index_finger_y), (255, 0, 0), 2)

                # Menghitung jarak antara ibu jari dan telunjuk
                distance = math.sqrt(
                    (thumb_x - index_finger_x) ** 2 + (thumb_y - index_finger_y) ** 2
                )

                # Mengontrol volume berdasarkan jarak antara ibu jari dan telunjuk
                volume = np.interp(distance, [0, 300], [0, 100])
                pyautogui.press("volumedown") if volume < 25 else None
                pyautogui.press("volumeup") if volume > 75 else None

        # Menampilkan citra dengan landmark dan garis tangan
        cv2.imshow("Gesture Volume Control", image)

        # Menghentikan program dengan menekan tombol 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Membersihkan
cap.release()
cv2.destroyAllWindows()
