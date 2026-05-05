import datetime
import wikipedia
import pyttsx3
import time
import os
import cv2
import speech_recognition as sr
import webbrowser

a = 'ROBOT:'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")


def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


def capture_photo():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(f"{a} Error: Couldn't open camera.")
        speak("Error. Couldn't open camera.")
        return

    photos_dir = os.path.join(os.path.expanduser('~'), 'Pictures', 'Camera Roll')
    if not os.path.exists(photos_dir):
        os.makedirs(photos_dir)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        elif key == ord('c'):
            photo_path = os.path.join(photos_dir, "captured_photo.jpg")
            cv2.imwrite(photo_path, frame)
            print(f"{a} Photo captured successfully.")
            speak("Photo captured successfully")
            break

    cap.release()
    cv2.destroyAllWindows()


def open_photos_folder():
    photos_folder_path = os.path.join(os.path.expanduser('~'), 'Pictures', 'Camera Roll')

    if os.path.exists(photos_folder_path):
        os.startfile(photos_folder_path)
    else:
        print(f"{a} Photos folder does not exist!")
        speak("Folder doesn't exist")


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"User: {query}")
        return query

    except Exception:
        print(f"{a} Couldn't understand. Please try again.")
        speak("I didn't catch that")
        return ""


def listen_for_wake_word():
    """Waits until user says 'robot'"""
    while True:
        query = listen()
        if "hey robot" in query:
            print(f"{a} Yes, how can I help?")
            speak("Yes, how can I help?")
            return


if __name__ == "__main__":
    print("Initialising Robot...")
    wishMe()

    msg = "I am Mr.ROBOT. Please tell me how may I help you."
    print(msg)
    speak(msg)

    while True:
        listen_for_wake_word()

        user_input = listen()

        if "time" in user_input:
            current_time = get_current_time()
            print(f"{a} The correct time is- {get_current_time()}")
            speak(f"The current time is {current_time}")

        elif "open google" in user_input:
            print(f"{a} Opening google....")
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'love me' in user_input:
            print(
                f"{a} Sorry but my first and final love is my creator mayank. I am currently in a relationship with "
                "connected wifi. I hope you understand that.")
            speak(
                "Sorry but my first and final love is my creator mayank. I am currently in a relationship with "
                "connected wifi. I hope you understand that")

        elif 'open youtube' in user_input:
            print(f"{a} Opening YouTube.....")
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'abusing me' in user_input:
            print(f"{a} Hey you bloody, just shut up. Don't abuse my owner")
            speak("Hey you bloody, just shut up. Don't abuse my owner")

        elif 'how many languages you know' in user_input:
            print("Currently I know only English")
            speak(f" Currently I know only English")

        elif 'licence' in user_input:
            print(
                f"{a} I was created in 2024 on 3rd March Friday at 9:40 PM by Mayank at his private lab of AI in "
                "India as demo project of a final year college student called Virtual AI assistant. Mayank remains "
                "Python's principle lover, my lead developer although I doesn't include any type of contributions from others.")
            speak(
                "I was created in 2024 on 3rd March Friday at 9:40 PM by Mayank at his private lab of AI in India as "
                "demo project of a final year college student called Virtual AI assistant. Mayank remains Python's "
                "principle lover, my lead developer although I doesn't includes any type of contributions from others.")

        elif 'wikipedia' in user_input:
            print(f"{a} Searching Wikipedia....")
            speak("Searching Wikipedia....")
            user_input = user_input.replace("wikipedia", "")
            results = wikipedia.summary(user_input, sentences=2)
            print(a, results)
            speak(results)

        elif 'open photos' in user_input:
            print(f"{a} Opening photos....")
            speak("opening photos")
            open_photos_folder()

        elif 'who is your developer' in user_input:
            print(
                f"{a} My developer and owner is Mayank. Please contact him for my source code and further any type of "
                "information.")
            speak(
                "My developer and owner is Mayank. Please contact him for my source code and further any type of "
                "information.")

        elif 'open stackoverflow' in user_input:
            print(f"{a} Opening Stackoverflow")
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open camera' in user_input:
            print(f"{a} Opening Camera....")
            speak("Opening Camera")
            print(f"{a} Press C for capture the photo")
            print(f"{a} Press Q for exit the camera")
            speak("Press C for capture the photo")
            speak("Press Q for exit the camera")
            capture_photo()
            speak("Photo captured successfully")

        elif 'who are you' in user_input:
            print(
                f"{a} {msg}")
            speak(msg)

        elif 'name' in user_input:
            print(f"{a} I am a virtual AI assistant. Sorry but my creator didn't christin me yet")
            speak("I am a virtual AI assistant. Sorry but my creator didn't christin me yet")

        elif "terminate yourself" in user_input:
            print(f"{a} I am terminating.....")
            time.sleep(2)
            print("Terminated")
            speak("Terminated")
            exit(0)

        elif 'how are you' in user_input:
            print(f"{a} Yeah I am good bro!. I hope you are doin' well.")
            speak("Yeah I am good bro!. I hope you are doin' well.")

        elif 'how you doin' in user_input:
            print(f"{a} Yeah I am doing absolutely good! Thanks for asking....")
            speak("Yeah I am doing absolutely good. Thanks for asking")


        elif 'shutdown' in user_input:
            print(f"{a} Shutting down PC")
            speak("Shutting down PC")
            time.sleep(3)
            os.system("shutdown/s /t 1")
