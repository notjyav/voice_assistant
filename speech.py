import speech_recognition as sr
import pyttsx3

_engine = pyttsx3.init()

def speak(text: str) -> None:
    print(f"Assistant: {text}")
    try:
        _engine.say(text)
        _engine.runAndWait()
    except Exception as e:
        print(f"[speech output unavailable: {e}]")

def listen(timeout: int = 8, phrase_time_limit: int = 12) -> str:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1.2

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration = 1.0)
            audio = recognizer.listen(
                source, timeout=timeout, phrase_time_limit=phrase_time_limit
            )
    except sr.WaitTimeoutError:
        print("[no speech detected in time]")
        return ""
    except OSError as e:
        print(f"[mircrophone unavailable: {e}]")
        return ""

    try:
        text = recognizer.recognize_google(audio)
        print(f"you said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        speak("I'm having trouble reaching the speech service.")
        print(f"[recognition request failed: {e}]")
        return "" 
