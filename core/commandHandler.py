import webbrowser
import wikipedia
import datetime
from utils.logger import Logger
import requests
import os
from dotenv import load_dotenv


class CommandHandler:
    def __init__(self, logger: Logger):
        load_dotenv()
        self.logger = logger.get_logger()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")

    def handle_command(self, command: dict) -> str:
        self.logger.info(f"Handling command: {command}")
        intent = command.get("intent")
        text = command.get("text", "").lower()

        if intent == "get_time":
            return f"The current time is {datetime.datetime.now().strftime('%I:%M%p')}."
        elif intent == "get_weather":
            url = "http://api.weatherapi.com/v1/current.json"
            params = {
                "key": self.weather_api_key,
                "q": "Toronto",
            }
            response = requests.get(url=url, params=params)
            data = response.json()
            return f"Current temperature in Toronto is {data['current']['temp_c']}°C"
        elif intent == "wikipedia":
            try:
                summary = wikipedia.summary(text.replace("wikipedia", ""), sentences=2)
                self.logger.info(f"Wikipedia summary retrieved: {summary}")
                return f"Wikipedia summary: {summary}"
            except Exception as e:
                self.logger.error(f"Error retrieving Wikipedia summary. {e}")
                return "Could not retrieve Wikipedia summary."
        else:
            return "Sorry, I don't understand that command."