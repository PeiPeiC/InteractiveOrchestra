import mediapipe as mp
import cv2
import threading
import time

from Player2 import play_violin_sound

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

last_play_time = time.time()
sound_thread = None  # Initialize sound_thread

def sound_thread_func(note):
    play_violin_sound(note)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            current_time = time.time()
            if current_time - last_play_time >= 0.1:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i, landmark in enumerate(hand_landmarks.landmark):
                        if i == 7:  # Landmark 8 (0-based index)
                            h, w, _ = image.shape
                            x, y = int(landmark.x * w), int(landmark.y * h)
                            print(f"Landmark 8 (x, y): ({x}, {y})")

                            if x < 100:
                                a = "51-4D.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(a,))
                                print(f"X: {x}, note: {a}")
                                sound_thread.start()
                                last_play_time = current_time

                            elif 100 <= x < 200:
                                b ="53-4E.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                print(f"X: {x}, note: {b}")
                                sound_thread.start()
                                last_play_time = current_time
                            
                            elif 200 <= x < 300:
                                b ="54-4F.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                print(f"X: {x}, note: {b}")
                                sound_thread.start()
                                last_play_time = current_time

                            elif 300 <= x < 400:
                                b ="56-4G.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                print(f"X: {x}, note: {b}")
                                sound_thread.start()
                                last_play_time = current_time
                            
                            elif 400 <= x < 500:
                                b ="58-4A.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                print(f"X: {x}, note: {b}")
                                sound_thread.start()
                                last_play_time = current_time
                            
                            elif 500 <= x < 600:
                                b ="60-4B.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                print(f"X: {x}, note: {b}")
                                sound_thread.start()
                                last_play_time = current_time

                            else:
                                b ="61-5C.wav"
                                sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                print(f"X: {x}, note: {b}")
                                sound_thread.start()
                                last_play_time = current_time

            # Draw hand landmarks
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                      mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()




