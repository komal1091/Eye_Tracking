"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

# import cv2
# from gaze_tracking import GazeTracking

# gaze = GazeTracking()
# webcam = cv2.VideoCapture(0)

# while True:
#     # We get a new frame from the webcam
#     _, frame = webcam.read()

#     # We send this frame to GazeTracking to analyze it
#     gaze.refresh(frame)

#     frame = gaze.annotated_frame()
#     text = ""

#     if gaze.is_blinking():
#         text = "Blinking"
#     elif gaze.is_right():
#         text = "Looking right"
#     elif gaze.is_left():
#         text = "Looking left"
#     elif gaze.is_center():
#         text = "Looking center"

#     cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#     left_pupil = gaze.pupil_left_coords()
#     right_pupil = gaze.pupil_right_coords()
#     cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#     cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

#     cv2.imshow("Demo", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     # if cv2.waitKey(1) == 27:
#     #     break
   
# webcam.release()
# cv2.destroyAllWindows()


# import cv2
# from gaze_tracking import GazeTracking

# gaze = GazeTracking()
# webcam = cv2.VideoCapture(0)

# try:
#     while True:
#         # We get a new frame from the webcam
#         _, frame = webcam.read()

#         # We send this frame to GazeTracking to analyze it
#         gaze.refresh(frame)

#         frame = gaze.annotated_frame()
#         text = ""

#         if gaze.is_blinking():
#             text = "Blinking"
#         elif gaze.is_right():
#             text = "Looking right"
#         elif gaze.is_left():
#             text = "Looking left"
#         elif gaze.is_center():
#             text = "Looking center"

#         cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#         left_pupil = gaze.pupil_left_coords()
#         right_pupil = gaze.pupil_right_coords()
#         cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#         cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

#         cv2.imshow("Demo", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#         # if cv2.waitKey(1) == 27:
#         #     break
# finally:
#     # Release the webcam and close OpenCV windows
#     webcam.release()
#     cv2.destroyAllWindows()

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




# import cv2
# import mediapipe as mp
# from gaze_tracking import GazeTracking

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands()
# mp_drawing_hands = mp.solutions.drawing_utils  # Import drawing utilities for hands

# mp_face_detection = mp.solutions.face_detection
# face_detection = mp_face_detection.FaceDetection()
# mp_drawing_face = mp.solutions.drawing_utils  # Import drawing utilities for face

# gaze = GazeTracking()
# webcam = cv2.VideoCapture(0)

# try:
#     while True:
#         # Read a new frame from the webcam
#         _, frame = webcam.read()

#         # Convert the frame to RGB
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Detect hands in the frame
#         hands_results = hands.process(frame_rgb)

#         # Detect face in the frame
#         face_results = face_detection.process(frame_rgb)

#         # If hands are detected, draw landmarks on the frame
#         if hands_results.multi_hand_landmarks:
#             for hand_landmarks in hands_results.multi_hand_landmarks:
#                 # Draw hand landmarks on the frame
#                 mp_drawing_hands.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#                 # Check if the hand is visible based on hand landmarks
#                 # Your logic to determine hand visibility goes here

#         # If face is detected, draw bounding box and landmarks on the frame
#         if face_results.detections:
#             for detection in face_results.detections:
#                 mp_drawing_face.draw_detection(frame, detection)

#         # Send the frame to GazeTracking to analyze it
#         gaze.refresh(frame)

#         # Get the annotated frame from GazeTracking
#         frame = gaze.annotated_frame()

#         # Display gaze direction information on the frame
#         text = ""
#         if gaze.is_blinking():
#             text = "Blinking"
#         elif gaze.is_right():
#             text = "Looking right"
#         elif gaze.is_left():
#             text = "Looking left"
#         elif gaze.is_center():
#             text = "Looking center"

#         cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

#         left_pupil = gaze.pupil_left_coords()
#         right_pupil = gaze.pupil_right_coords()
#         cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
#         cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

#         # Display the frame
#         cv2.imshow("Demo", frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# finally:
#     # Release the webcam and close OpenCV windows
#     webcam.release()
#     cv2.destroyAllWindows()
