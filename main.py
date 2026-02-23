import speech_recognition as sr
import pyttsx3
import webbrowser
import music

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Make voice faster
engine.setProperty("rate", 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_url(url):
    webbrowser.open(url)   # Faster than os.system

def processCommand(c):
    c = c.lower()
    print("Processing:", c)

    if "open google" in c:
        speak("Opening Google")
        open_url("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        open_url("https://youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        open_url("https://facebook.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        open_url("https://linkedin.com")

    elif "play" in c:
        song = c.replace("play", "").strip()

        if song in music.music:
            speak(f"Playing {song}")
            open_url(music.music[song])
        else:
            speak("Song not found")

if __name__ == "__main__":
    speak("Jarvis ready")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

                command = recognizer.recognize_google(audio)
                print("Heard:", command)

                processCommand(command)

            except sr.WaitTimeoutError:
                pass   # No speech detected, continue listening

            except Exception as e:
                print("Error:", e)
