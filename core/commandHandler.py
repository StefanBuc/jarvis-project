import webbrowser
import wikipedia
import datetime
from utils.logger import Logger
import requests
import os
from dotenv import load_dotenv


class CommandHandler:
    def __init__(self):
        load_dotenv()
        self.logger = Logger().get_logger()
        self.weather_api_key = os.getenv("WEATHER_API_KEY")

    def handle_command(self, command: dict) -> str:
        self.logger.info(f"Handling command: {command}")

        if command == "get_time":
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        elif command == "get_weather":
            url = "http://api.weatherapi.com/v1/current.json"
            params = {
                "key": self.weather_api_key,
                "q": "Toronto",
            }
            response = requests.get(url=url, params=params)
            data = response.json()
            return f"Current temperature in Toronto: {data['current']['temp_c']}°C"
        elif command == "search_wikipedia":
            try:
                summary = wikipedia.summary(command.get('query', ''), sentences=2)
                return f"Wikipedia summary: {summary}"
            except:
                return "Could not retrieve Wikipedia summary. Please check your query."
        else:
            return "Unknown command."