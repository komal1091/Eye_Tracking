import cv2
import mediapipe as mp
from gaze_tracking import GazeTracking

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils 


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

try:
    while True:
        # Read a new frame from the webcam
        _, frame = webcam.read()

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(frame_rgb)

        # If hands are detected, draw landmarks on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Check if the hand is visible based on hand landmarks
                # Your logic to determine hand visibility goes here

        # Send the frame to GazeTracking to analyze it
        gaze.refresh(frame)

        # Get the annotated frame from GazeTracking
        frame = gaze.annotated_frame()

        # Display gaze direction information on the frame
        text = ""
        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        # Display the frame
        cv2.imshow("Demo", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the webcam and close OpenCV windows
    webcam.release()
    cv2.destroyAllWindows()



# from django.shortcuts import render
# import cv2
# from gaze_tracking import GazeTracking

# def webcam(request):
#     gaze = GazeTracking()
#     webcam = cv2.VideoCapture(0)

#     try:
#         while True:
#             # Read a new frame from the webcam
#             _, frame = webcam.read()

#             # Your existing code to process the frame and detect gaze
#             # ...

#             # Display the frame
#             _, buffer = cv2.imencode('.jpg', frame)
#             frame_base64 = buffer.tobytes()
#             context = {'frame': frame_base64}
#             return render(request, 'webcam.html', context)

#     finally:
#         # Release the webcam
#         webcam.release()


