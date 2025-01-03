# Hand Gesture Controlled Game (Dinosaur Run)

This project demonstrates a Python-based application that uses computer vision and hand gesture recognition to control a game (like the Chrome Dinosaur Run). The implementation involves:

## Features
- **Hand Tracking and Gesture Detection**: Utilizes the `cvzone` library's Hand Tracking Module to detect hand gestures in real time.
- **Keyboard Simulation**: Employs the `pynput` library to simulate keyboard key presses (e.g., Up and Down arrow keys) based on the detected gestures.
- **Webcam Input**: Captures live video feed using `OpenCV` for processing hand gestures.
- **Real-Time Interaction**: Maps the index finger and thumb gestures to control the dinosaur's movements (jumping or ducking).

## Prerequisites
- Python 3.x
- Required Libraries:
  - `opencv-python`
  - `cvzone`
  - `pynput`

Install the dependencies using the following command:
```bash
pip install opencv-python cvzone pynput
```

## Usage
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-directory>
   ```
3. Run the script:
   ```bash
   python dino.py
   ```
4. Use your webcam to perform gestures to control the game:
   - open google dino game
   - Raise your **index finger** to make the dinosaur jump.
   - Raise your **thumb** to make the dinosaur duck.
6. Press the `Esc` key to exit the application.

## Code Explanation
- **Hand Detection**: Detects hand gestures using `cvzone.HandTrackingModule`.
- **Gesture Mapping**: Identifies specific finger positions (index or thumb raised) to control the game.
- **Keyboard Events**: Simulates keypresses (`Key.up` and `Key.down`) using the `pynput.keyboard` module.
- **Real-Time Feedback**: Displays live video feed with gesture status and movement instructions overlaid.

## Future Enhancements
- Add support for more gestures and controls.
- Integrate additional games or applications.
- Enhance gesture detection accuracy.

## Example Output
When running the application, the webcam feed will display real-time hand tracking, and corresponding game actions will be triggered based on gestures.

## Contributing
Feel free to fork the repository, experiment, and contribute to improve the project! If you encounter any issues or have suggestions, please open an issue or submit a pull request.

---

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy coding and gaming! 🎮
