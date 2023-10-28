from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import mediapipe as mp

# Create your views here.

def home(request):
    return render(request,'webcam_app/home.html')

def violin(request):
    return render(request,'webcam_app/violin.html')

# yourappname/views.py
@gzip.gzip_page
def hand_tracking_camera(request):
    # Your OpenCV camera capture code here
    camera = cv2.VideoCapture(0)

    def generate():
        while True:
            success, frame = camera.read()
            if not success:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return StreamingHttpResponse(generate(), content_type="multipart/x-mixed-replace;boundary=frame")


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

@gzip.gzip_page
def hand_tracking_camera(request):
    cap = cv2.VideoCapture(0)

    def generate_frames():
        with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = cv2.flip(image, 1)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        for i, landmark in enumerate(hand_landmarks.landmark):
                            if i == 7:
                                h, w, _ = image.shape
                                x, y = int(landmark.x * w), int(landmark.y * h)
                                print(f"Landmark 8 (x, y): ({x}, {y})")

                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                            mp_drawing.DrawingSpec(
                                color=(121, 22, 76), thickness=2, circle_radius=4
                            ),
                            mp_drawing.DrawingSpec(
                                color=(250, 44, 250), thickness=2, circle_radius=2
                            )
                        )

                _, buffer = cv2.imencode('.jpg', image)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')