import mediapipe as mp
import cv2
import threading
import time

from Player2 import play_violin_sound

#from Pygame_playsound import play_violin_sound1


scales = {'Major': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '51-4B.wav', '52-5C.wav'],
 'Minor': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '48-4G#.wav', '51-4B.wav', '52-5C.wav'],
  'Blues': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '46-4F#.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav'],
   'Minor pentatonic blues': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav', '57-5F.wav'],
    'Major pentatonic': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '47-4G.wav', '49-4A.wav', '52-5C.wav', '54-5D.wav', '56-5E.wav'],
     'Minor Pentatonic': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav', '57-5F.wav'],
      'Melodic Minor': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '51-4B.wav', '52-5C.wav'],
       'Dorian Mode': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '50-4A#.wav', '52-5C.wav'],
        'Mixolydian Mode': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '50-4A#.wav', '52-5C.wav'],
         'Ahava Raba Mode': ['40-4C.wav', '41-4C#.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '48-4G#.wav', '50-4A#.wav', '52-5C.wav']}

# Settings for piano, want to make every half second so line 50 >= 0.5



mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

last_play_time = time.time()
sound_thread = None  # Initialize sound_thread


insrument = "Minions"

def sound_thread_func(note):
    play_violin_sound(note, insrument)

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
            if current_time - last_play_time >= 0.5:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i, landmark in enumerate(hand_landmarks.landmark):
                        if i == 7:  # Landmark 8 (0-based index)
                            h, w, _ = image.shape
                            x, y = int(landmark.x * w), int(landmark.y * h)
                            print(f"Landmark 8 (x, y): ({x}, {y})")

                            if y < h/2:

                                if x < int(w/3):
                                    a = "BaBaBanana.mp3"
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(a,))
                                    print(f"X: {x}, note: {a}")
                                    sound_thread.start()
                                    last_play_time = current_time

                                elif int(w/3) <= x < int(w/3)*2:
                                    b = "Potato.wav"
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time
                                
                                elif int(w/3)*2 <= x < int(w/3)*3:
                                    b = "Yabaya.wav"
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




