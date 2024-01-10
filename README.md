# Interactive Orchestra
## Overview

Interactive Orchestra App is a unique collection of Python-based musical tools designed for real-time music creation and interaction using web camera input. The project, which emerged as the Winner of the Morgan Stanley Challenge at the UofG Tech Society Hackathon, skillfully blends advanced technology and creativity. 

Key Features:
- **Hand Gesture Recognition**: Control virtual instruments through intuitive hand movements.
- **Facial Emotion Detection**: The system tunes musical scales based on user’s facial expressions, infusing an emotional depth to the music.
- **Versatile Instruments**: Users can play the piano, violin, or an interactive drum kit.
- **Minion-Style A Cappella**: Unique feature allowing users to enjoy minion-like voice renditions.

## Main Code Files
1. **Piano_Violin.py**
   - **Functionality**: Play piano or violin sounds within an 8-octave range.
   - **Key Parameters** (modifiable):
     - `instrument`: "Piano" or "Violin"
     - `scale`: "Major", "Minor", etc.
     - `beats`: Duration of a beat (e.g., 0.5 seconds)
     - `h`, `w`: Height and width of the camera frame
   - **Dependencies**: `mediapipe`, `cv2`, `threading`, `time`
   - **Note**: The parameters can be adjusted to suit user preferences.

2. **Minions.py**
   - **Functionality**: Play minion-style a cappella with three distinct voices.
   - **Key Parameters**: Similar to `Piano_Violin.py` but with `instrument` set to "Minions".
   - **Dependencies**: Same as `Piano_Violin.py`.

3. **Drums_final.py**
   - **Functionality**: Simulate a drum kit that can be played using hand gestures.
   - **Dependencies**: Same as `Piano_Violin.py`.

4. **Facial_Emotion_to_Music.py**
   - **Functionality**: Adjust the musical scale based on the user's facial expressions detected via the camera.
   - **Dependencies**: `os`, `cv2`, `numpy`, `keras`, `matplotlib`, `keyboard`, `time`, alongside those used in `Piano_Violin.py`.

## Usage and Recommendations
- Ensure all dependencies are installed. Use `pip install <package>` for missing packages.
- Adjust the camera resolution (`h`, `w`) to suit your setup for optimal performance.
- Experiment with different scales and beats to find your preferred musical style.
- For facial emotion recognition, ensure good lighting for accurate detection.

### Running the Programs
1. To run any script, use the command: `python <script_name>.py`
2. Make sure your camera is functional and allowed access by the script.
3. Follow on-screen instructions (if any) for interacting with the program.

### Contributing
Contributions to this project are welcome. Please follow standard procedures for forking the repository, making changes, and submitting pull requests.
