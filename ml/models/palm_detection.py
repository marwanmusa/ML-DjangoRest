# Import Libraries
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
IMG_FILES = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    for idx, file in enumerate(IMG_FILES):
        # Read an img, flip it around y-axis for correct handedness ouput (see above).
        img = cv2.flip(cv2.imread(file), 1)

        # Convert the BGR img to RGB before processing.
        res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Print handness and draw hand landmarks ion the img.
        print('Handedness:', res.multi_handedness)

        if not res.multi_hand_landmarks:
            continue
        img_h, img_w = img.shape
        annotated_img = img.copy()

        for hand_landmarks in res.multi_hand_landmarks:
            print('hand_landmarks:', hand_landmarks)
            print(
                f'Index finger tip coordinates: (',
                f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*img_w}, '
                f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*img_h})'
            )
            mp_drawing.draw_landmarks(
                annotated_img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_img, 1))

            # Draw hand world landmarks.
            if not res.multi_hand_world_landmarks:
                continue

            for hand_world_landmarks in res.multi_hand_world_landmarks:
                mp_drawing.plot_landmarks(hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

# For webcam input:
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            print(" Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the img as not writable to pass by reference.
        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        res = hands.process(img)

        # Draw the hand annotations no the img.add()
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if res.multi_hand_landmarks:
            for hand_landmarks in res.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # Flip the img horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(img, 1))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
