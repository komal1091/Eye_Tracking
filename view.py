from django.shortcuts import render
import cv2
from gaze_tracking import GazeTracking

def webcam(request):
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)

    try:
        while True:
            # Read a new frame from the webcam
            _, frame = webcam.read()

            # Your existing code to process the frame and detect gaze
            # ...

            # Display the frame
            _, buffer = cv2.imencode('.jpg', frame)
            frame_base64 = buffer.tobytes()
            context = {'frame': frame_base64}
            return render(request, 'webcam.html', context)

    finally:
        # Release the webcam
        webcam.release()
