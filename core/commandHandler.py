import webbrowser
import wikipedia
import datetime


class CommandHandler:
    def __init__(self):
        pass

    def handle_command(self, command: dict) -> str:
        action = command.get('action')

        if action == "get_time":
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        elif action == "get_weather":
            return "Weather functionality is not implemented yet."
        elif action == "search_wikipedia":
            try:
                summary = wikipedia.summary(command.get('query', ''), sentences=2)
                return f"Wikipedia summary: {summary}"
            except:
                return "Could not retrieve Wikipedia summary. Please check your query."
        else:
            return "Unknown command."