import speech_recognition as sr
import pyrebase


def recognize_speech():
    
    firebaseconfig = {
        "apiKey": "AIzaSyBE9Sv-C4mSO1ZeyPLl8uv59qExaPNJLj4",
        "authDomain": "drishti-ab653.firebaseapp.com",
        "databaseURL": "https://drishti-ab653-default-rtdb.firebaseio.com",
        "projectId": "drishti-ab653",
        "storageBucket": "drishti-ab653.appspot.com",
        "messagingSenderId": "495917202335",
        "appId": "1:495917202335:web:47b9f422b86e8ee1939baa",
    }
    firebase = pyrebase.initialize_app(firebaseconfig)
    db = firebase.database()
    
    while True:
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source)
            recognizer.dynamic_energy_threshold = 3000
            
            try:
                print("Listening...")
                audio = recognizer.listen(source,timeout=5)
                response = recognizer.recognize_google(audio)
                print(response)
                data = {"Text": response}
                db.update(data)
            except sr.UnknownValueError:
                print("Didn't recognize")

if __name__ == "__main__":
    recognize_speech()

