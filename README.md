# Project-Drishti

## Problem Statement-
In large-scale events like fairs, carnivals, and festivals, the effective deployment of police personnel is critical for maintaining crowd control and ensuring the safety of attendees. However, a recurring issue involves personnel leaving their assigned posts, creating potential security vulnerabilities. Project-Drishti aims to implement a robust tracking and monitoring system to address this challenge. This system not only identifies instances of personnel leaving their designated areas but also provides detailed insights into their activities during these absences. The overarching goal is to create a secure environment by ensuring officers remain committed to their assigned duties.

## Methodology-

### Hardware Tools-
1. Raspberry Pi 4 model B (4GB RAM): The core computing device that powers the system.
2. U-Blox Neo-6M GPS Module: Provides real-time GPS coordinates for tracking the location of personnel.
3. Mini USB Microphone 2.0 (for Raspberry Pi): Captures real-time speech data for enhanced user interaction.
4. Digital Webcam: Integrated with OpenCV for real-time video processing and surveillance.
5. Raspberry Pi 4 Case: Protects and houses the Raspberry Pi and associated hardware.

### Software Tools-
1. Google Maps API: Visualizes real-time GPS coordinates on maps for user-friendly display.
2. HTML and CSS: Used for creating an intuitive and user-friendly interface for interaction.
3. OpenCV (Python): Employs advanced image and video processing for surveillance and tracking.
4. SpeechRecognition API (Python): Converts real-time speech into text data for analysis.
5. PyAudio (Python): Facilitates audio recording for the SpeechRecognition process.
6. Flac Library (Python): Converts audio data into the FLAC format for compatibility with SpeechRecognition.
7. Raspbian OS: The operating system for the Raspberry Pi.
8. Firebase Database: Stores and manages real-time GPS coordinates and other relevant data.
9. VS Code: Integrated development environment for coding and development.

### Step-1: Geo-Fencing:
The U-Blox Neo-6M GPS Module continuously tracks the real-time GPS coordinates of personnel. A Geo-Fencing algorithm monitors whether individuals are within their predefined designated areas.

### Step-2: Map Generation:
Collected GPS coordinates are stored in the Firebase Database. The Google Maps API is then utilized to visualize these coordinates in real time. A separate display device retrieves the data from the database to render maps for user viewing.

### Step-3: Real-Time Speech-to-Text:
The system employs the SpeechRecognition API, PyAudio, and the Flac Library to capture and convert real-time speech into text data. If a user leaves the predefined area, this data is stored in MongoDB or Firebase for further analysis and tracking.

### Step-4: Real-Time Camera Feed:
Integration of a digital webcam enhanced with OpenCV transforms the project into a comprehensive surveillance system. OpenCV enables sophisticated image and video processing, including facial recognition and object tracking, providing detailed monitoring of personnel who deviate from their designated positions.
