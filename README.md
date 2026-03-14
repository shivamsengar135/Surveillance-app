# Surveillance App

This application uses your computer's camera to detect and count human heads in real-time.

## Setup

1.  **Install Python:** If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

2.  **Install OpenCV:** Open a terminal or command prompt and install the required library using pip:
    ```bash
    pip install opencv-python
    ```

3.  **Download the Haar Cascade file:**
    *   Download the `haarcascade_frontalface_default.xml` file from the official OpenCV GitHub repository:
        [https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
    *   Save this file in the same directory as the `app.py` script (`C:\Windows\System32\SurveillanceApp`).

## How to Run

1.  Open a terminal or command prompt.
2.  Navigate to the `SurveillanceApp` directory:
    ```bash
    cd C:\Windows\System32\SurveillanceApp
    ```
3.  Run the application:
    ```bash
    python app.py
    ```
4.  A window will open showing your camera feed with rectangles around detected faces and a head count at the top.
5.  Press the 'q' key to quit the application.
