import webbrowser
import urllib.parse
from skills.base import Skill
from speech import speak

class MusicSkill(Skill):
    def can_handle(self, query: str) -> bool:
        return query.startswith("play") or "play music" in query or "play song" in query

    def _extract_search_term(self, query: str) -> str:
        """'play bohemian rhapsody' -> 'bohemian rhapsody'"""
        for phrase in ["play song", "play music", "play"]:
            if query.startswith(phrase):
                return query[len(phrase):].strip()
        return query.strip()

    def handle(self, query: str) -> None:
        search_term = self._extract_search_term(query)

        if not search_term:
            speak("What would you like to play?")
            return

        encoded_term = urllib.parse.quote(search_term)
        search_url = f"https://open.spotify.com/search/{encoded_term}"

        speak(f"Searching Spotify for {search_term}")
        webbrowser.open(search_url)