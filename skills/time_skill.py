import datetime 
from skills.base import Skill 
from speech import speak

class TimeSkill(Skill):
    def can_handle(self, query: str) -> bool:
        return "time" in query

    def handle(self, query: str) -> None:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
