import cv2
import numpy as np
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render


def generate_random_frame(width=640, height=480, grid_size=20):
    _frame = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(0, height, grid_size):
        for x in range(0, width, grid_size):
            color = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
            _frame[y:y + grid_size, x:x + grid_size] = color
    return _frame


def get_frame_from_webcam(device_index=0, width=640, height=480):
    cap = cv2.VideoCapture(device_index)
    success, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    return frame


def video_stream():
    cap = cv2.VideoCapture(0)
    while True:
        # frame = generate_random_frame()
        # frame = get_frame_from_webcam()
        success, frame = cap.read()
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_data = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n\r\n')


def stream_video(request):
    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    return render(request, 'webcam_app/index.html')


def hello_world(request):
    return HttpResponse("Hello, world.")
