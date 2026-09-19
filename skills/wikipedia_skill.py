import requests
from skills.base import Skill
from speech import speak

HEADERS = {"User-Agent": "PythonVoiceAssistant/1.0 (personal learning project)"}
SEARCH_URL = "https://en.wikipedia.org/w/api.php"
SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/{title}"


class WikipediaSkill(Skill):
    def can_handle(self, query: str) -> bool:
        return "wikipedia" in query or "who is" in query or "what is" in query

    def _extract_topic(self, query: str) -> str:
        for phrase in ["search wikipedia for", "wikipedia", "who is", "what is"]:
            if phrase in query:
                return query.split(phrase, 1)[1].strip()
        return query.strip()

    def _search_title(self, topic: str):
        params = {
            "action": "query",
            "list": "search",
            "srsearch": topic,
            "format": "json",
            "srlimit": 1,
        }
        response = requests.get(SEARCH_URL, params=params, headers=HEADERS, timeout=5)
        response.raise_for_status()
        results = response.json().get("query", {}).get("search", [])
        return results[0]["title"] if results else None

    def handle(self, query: str) -> None:
        topic = self._extract_topic(query)

        if not topic:
            speak("What would you like me to look up?")
            return

        try:
            title = self._search_title(topic)
            if not title:
                speak(f"I couldn't find anything on Wikipedia about {topic}.")
                return

            url = SUMMARY_URL.format(title=title.replace(" ", "_"))
            response = requests.get(url, headers=HEADERS, timeout=5)

            if response.status_code == 404:
                speak(f"I couldn't find anything on Wikipedia about {topic}.")
                return
            response.raise_for_status()

            data = response.json()

            if data.get("type") == "disambiguation":
                speak(f"{topic} could mean a few different things. Can you be more specific?")
                return

            extract = data.get("extract", "")
            if not extract:
                speak(f"I couldn't find a summary for {topic}.")
                return

            sentences = extract.split(". ")
            short_summary = ". ".join(sentences[:2]).rstrip(".") + "."
            speak(short_summary)

        except requests.exceptions.RequestException as e:
            speak("I'm having trouble reaching Wikipedia right now.")
            print(f"[wikipedia error: {e}]")