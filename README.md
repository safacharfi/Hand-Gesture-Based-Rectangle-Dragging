
# Hand Gesture-Based Rectangle Dragging

## Overview

This project demonstrates a simple interactive application using OpenCV and the `cvzone` HandTrackingModule to allow users to drag multiple rectangles on the screen using hand gestures. The application detects hand movements and updates the position and color of rectangles based on the index finger's position and the distance between the index and middle fingers.

## Features

- **Real-Time Interaction**: Detects hand gestures in real-time to drag rectangles.
- **Multiple Rectangles**: Handles multiple rectangles that can be individually dragged.
- **Dynamic Color Change**: Changes the color of rectangles when the hand is within their area.

## Requirements

- Python 3.x
- OpenCV
- cvzone

You can install the required packages using pip:

```bash
pip install opencv-python cvzone
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/safacharfi/hand-gesture-rectangle-dragging.git
   cd hand-gesture-rectangle-dragging
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   python main.py
   ```

## Usage

1. **Start the Application**

   Run the application using the command:

   ```bash
   python main.py
   ```

2. **Interact with Rectangles**

   - Use your hand to move the index finger closer to the middle finger to activate dragging mode.
   - Move the index finger to drag the rectangles around the screen.
   - The color of the rectangle will change to green when the index finger is inside the rectangle, and revert to pink when outside.

3. **Exit the Application**

   Press `q` to quit the application.

## Code Explanation

- **Hand Detection**: Uses `cvzone.HandTrackingModule` to detect hands and their landmarks.
- **Rectangle Class**: `DragRec` class defines rectangles with position and size. It updates their color and position based on hand gestures.
- **Main Loop**: Captures video from the webcam, detects hands, and updates rectangle positions and colors based on hand gestures.

## Contributing

Feel free to contribute to this project by submitting pull requests, reporting issues, or suggesting improvements. 


## Contact

For any questions or feedback, please contact (charfi.safa@enis.tn).

## Acknowledgments

- **cvzone**: Provides hand tracking functionalities.
- **OpenCV**: Used for computer vision tasks and video capture.
