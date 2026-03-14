import cv2
import sys

# --- Configuration ---
# Path to the pre-trained Haar Cascade model for face detection
# The script will first try to load this from the installed OpenCV library.
# If that fails, it will look for the file in the same directory as the script.
CASCADE_FILE = 'haarcascade_frontalface_default.xml'
# Font for displaying text on the video feed
FONT = cv2.FONT_HERSHEY_SIMPLEX

def main():
    """
    Main function to run the head detection application.
    """
    # Attempt to load the cascade file from the OpenCV data path first
    cascade_path = cv2.data.haarcascades + CASCADE_FILE
    
    # Check if the cascade file exists at the default path
    if not cv2.os.path.exists(cascade_path):
        # If not, try to load it from the local directory
        cascade_path = CASCADE_FILE

    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print(f"Error loading cascade file.")
        print(f"Please make sure '{CASCADE_FILE}' is in the same directory as the script or that OpenCV is installed correctly.")
        print("You can download the file from: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml")
        sys.exit(1)

    # Initialize video capture from the default camera (index 0)
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open video stream.")
        sys.exit(1)

    print("Starting camera feed. Press 'q' to exit.")

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert the frame to grayscale for the face detector
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Get the head count
        head_count = len(faces)

        # Draw a rectangle around each detected face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the head count on the frame
        count_text = f"Head Count: {head_count}"
        cv2.putText(frame, count_text, (10, 30), FONT, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Surveillance Feed', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
    print("Application terminated.")

if __name__ == '__main__':
    main()
