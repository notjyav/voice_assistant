import json
import os
from skills.base import Skill
from speech import speak

REMINDERS_FILE = os.path.join(os.path.dirname(__file__), "..", "reminders.json")


def _load_reminders() -> list[str]:
    if not os.path.exists(REMINDERS_FILE):
        return []
    try:
        with open(REMINDERS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def _save_reminders(reminders: list[str]) -> None:
    """Write the current list of reminders to disk, overwriting
    whatever was there before."""
    with open(REMINDERS_FILE, "w") as f:
        json.dump(reminders, f, indent=2)


class ReminderSkill(Skill):
    def can_handle(self, query: str) -> bool:
        return "remind" in query or "reminder" in query

    def handle(self, query: str) -> None:
        reminders = _load_reminders()

        if "list" in query or "what are" in query or "read" in query:
            self._list_reminders(reminders)
        elif "clear" in query or "delete all" in query:
            _save_reminders([])
            speak("All reminders cleared.")
        else:
            self._add_reminder(query, reminders)

    def _add_reminder(self, query: str, reminders: list[str]) -> None:
        text = query
        for phrase in ["remind me to", "add a reminder to", "reminder to", "remind me"]:
            if phrase in text:
                text = text.split(phrase, 1)[1].strip()
                break

        if not text:
            speak("What would you like me to remind you about?")
            return

        reminders.append(text)
        _save_reminders(reminders)
        speak(f"Okay, I'll remember: {text}")

    def _list_reminders(self, reminders: list[str]) -> None:
        if not reminders:
            speak("You don't have any reminders saved.")
            return

        speak(f"You have {len(reminders)} reminder{'s' if len(reminders) != 1 else ''}:")
        for reminder in reminders:
            speak(reminder)