import pyjokes
from skills.base import Skill
from speech import speak


class JokeSkill(Skill):
    def can_handle(self, query: str) -> bool:
        return "joke" in query

    def handle(self, query: str) -> None:
        joke = pyjokes.get_joke()
        speak(joke)