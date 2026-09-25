from speech import listen, speak
from skills.time_skill import TimeSkill
from skills.joke_skill import JokeSkill
from skills.wikipedia_skill import WikipediaSkill
from skills.music_skill import MusicSkill
from skills.reminder_skill import ReminderSkill
from skills.weather_skill import WeatherSkill


WAKE_WORD = "hey assistant"

SKILLS = [
    TimeSkill(),
    JokeSkill(),
    WikipediaSkill(),
    MusicSkill(),
    ReminderSkill(),
    WeatherSkill(),
]

def handle_query(query: str) -> bool:
    if not query:
        return True
    
    words = query.split()
    if "exit" in words or "quit" in words or "stop" in words or "end the program" in query:
        speak("Goodbye!")
        return False

    for skill in SKILLS:
        if skill.can_handle(query):
            skill.handle(query)
            return True

    speak("Sorry, I don't know how to do that yet")
    return True

def run() -> None:
    speak("Hello! I'm ready. How can I help?")
    running = True
    while running:
        query = listen()
        running = handle_query(query)

if __name__ == "__main__":
    run()