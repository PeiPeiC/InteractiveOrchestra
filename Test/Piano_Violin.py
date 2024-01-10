import mediapipe as mp
import cv2
import threading
import time

scales = {'Major': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '51-4B.wav', '52-5C.wav'],
 'Minor': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '48-4G#.wav', '51-4B.wav', '52-5C.wav'],
  'Blues': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '46-4F#.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav'],
   'Minor pentatonic blues': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav', '57-5F.wav'],
    'Major pentatonic': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '47-4G.wav', '49-4A.wav', '52-5C.wav', '54-5D.wav', '56-5E.wav'],
     'Minor Pentatonic': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav', '57-5F.wav'],
      'Melodic Minor': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '51-4B.wav', '52-5C.wav'],
       'Dorian Mode': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '50-4A#.wav', '52-5C.wav'],
        'Mixolydian Mode': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '50-4A#.wav', '52-5C.wav'],
         'Ahava Raba Mode': ['40-4C.wav', '41-4C#.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '48-4G#.wav', '50-4A#.wav', '52-5C.wav'],
         "BlackKeys": ["34-3F#.wav", "36-3G#.wav", "38-3A#.wav", "41-4C#.wav", "43-4D#.wav", "46-4F#.wav", "48-4G#.wav", "50-4A#.wav"],
         "BlackPees": ["42-4D.wav", "44-4E.wav", "46-4F#.wav", "49-4A.wav", "50-4A#.wav", "51-4B.wav", "52-5C.wav", "56-5E.wav"]}

# Import your sound playing function
from Sound_player import play_violin_sound

# Replace with your sound playing function
def play_sound_for_hand(hand_landmarks, hand_label):
    # Implement your sound triggering logic here
    pass

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

last_play_time = time.time()

# Create a list to hold two sound threads and hand labels
sound_threads = [None, None, None]
hand_labels = ["Left Hand", "Right Hand", "Right Hand1"]

insrument = "Piano"

scale = "Major"

beats = 0.5

h=480
w=640

# Coordinates to define regions for drawing borders
border_lines = [(w // 8 * i, 0, w // 8 * i, h//2-20) for i in range(1, 8)]
#make horizontal lines
border_lines.append((0, h//2-20, w, h//2-20))


def sound_thread_func(note):
    play_violin_sound(note, insrument)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5, max_num_hands=3) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip horizontally
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        for x1, y1, x2, y2 in border_lines:
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

        if results.multi_hand_landmarks:
            current_time = time.time()
            if current_time - last_play_time >= beats:
                for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    for i, landmark in enumerate(hand_landmarks.landmark):
                        if i == 7:  # Landmark 8 (0-based index)
                            h, w, _ = image.shape
                            x, y = int(landmark.x * w), int(landmark.y * h)
                            print(f"{hand_labels[hand_index]} - Landmark 8 (x, y): ({x}, {y})")

                            if y < h/2:

                                if x < int(w/8):
                                    a = scales[scale][0]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(a,))
                                    print(f"X: {x}, note: {a}")
                                    sound_thread.start()
                                    last_play_time = current_time

                                elif int(w/8) <= x < int(w/8)*2:
                                    b = scales[scale][1]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time
                                
                                elif int(w/8)*2 <= x < int(w/8)*3:
                                    b = scales[scale][2]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time

                                elif int(w/8)*3 <= x < int(w/8)*4:
                                    b = scales[scale][3]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time
                                
                                elif int(w/8)*4 <= x < int(w/8)*5:
                                    b = scales[scale][4]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time
                                
                                elif int(w/8)*5 <= x < int(w/8)*6:
                                    b = scales[scale][5]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time

                                elif int(w/8)*6 <= x < int(w/8)*7:
                                    b = scales[scale][6]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time

                                else:
                                    b = scales[scale][7]
                                    sound_thread = threading.Thread(target=sound_thread_func, args=(b,))
                                    print(f"X: {x}, note: {b}")
                                    sound_thread.start()
                                    last_play_time = current_time

            # Draw hand landmarks
            for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
