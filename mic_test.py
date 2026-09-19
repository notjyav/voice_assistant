import speech_recognition as sr

r = sr.Recognizer()
try:
    mic = sr.Microphone()
    print("Microphone found. Say something...")
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=5)
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except Exception as e:
    print(f"Something went wrong: {e}")