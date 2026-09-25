import requests
from skills.base import Skill
from speech import speak

HEADERS = {"User-Agent": "PythonVoiceAssistant/1.0 (personal learning project)"}
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "depositing rime fog",
    51: "light drizzle",
    53: "moderate drizzle",
    55: "dense drizzle",
    61: "slight rain",
    63: "moderate rain",
    65: "heavy rain",
    71: "slight snow",
    73: "moderate snow",
    75: "heavy snow",
    80: "slight rain showers",
    81: "moderate rain showers",
    82: "violent rain showers",
    95: "a thunderstorm",
    96: "a thunderstorm with slight hail",
    99: "a thunderstorm with heavy hail",
}


class WeatherSkill(Skill):
    def can_handle(self, query: str) -> bool:
        return "weather" in query

    def _extract_city(self, query: str) -> str:
        if " in " in query:
            return query.split(" in ", 1)[1].strip()
        return ""

    def _geocode(self, city: str):
        params = {"name": city, "count": 1}
        response = requests.get(GEOCODE_URL, params=params, headers=HEADERS, timeout=5)
        response.raise_for_status()
        results = response.json().get("results")
        return results[0] if results else None

    def handle(self, query: str) -> None:
        city = self._extract_city(query)

        if not city:
            speak("Which city would you like the weather for?")
            return

        try:
            location = self._geocode(city)
            if not location:
                speak(f"I couldn't find a place called {city}.")
                return

            params = {
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current_weather": True,
                "temperature_unit": "fahrenheit",
            }
            response = requests.get(FORECAST_URL, params=params, headers=HEADERS, timeout=5)
            response.raise_for_status()

            current = response.json().get("current_weather", {})
            temp = current.get("temperature")
            code = current.get("weathercode")
            condition = WEATHER_CODES.get(code, "unknown conditions")

            place_name = location.get("name", city)
            speak(f"It's currently {temp} degrees with {condition} in {place_name}.")

        except requests.exceptions.RequestException as e:
            speak("I'm having trouble reaching the weather service right now.")
            print(f"[weather error: {e}]")