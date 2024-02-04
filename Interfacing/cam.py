import cv2
import firebase_admin
from firebase_admin import credentials, db
import time

# Initialize Firebase
cred = credentials.Certificate('path_to_your_private_key_file.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://project-drishti-1bda9-default-rtdb.firebaseio.com/'
})

# Initialize the camera
cap = cv2.VideoCapture(0)

# Create a named window to display the feed
cv2.namedWindow("Video Feed", cv2.WINDOW_NORMAL)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to base64
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Upload the frame to Firebase Realtime Database
        db.reference('frames').push({
            'timestamp': int(time.time()),
            'frame': frame_bytes
        })

        # Display the frame in a pop-up window
        cv2.imshow("Video Feed", frame)

        # Add a small delay
        time.sleep(0.1)

        # Break the loop with a key press on the keyboard
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    # Properly handle a keyboard interrupt
    print("Keyboard interrupt detected. Exiting...")

finally:
    # Release the camera and close the Firebase app
    cap.release()
    cv2.destroyAllWindows()
    firebase_admin.delete_app(firebase_admin.get_app())
