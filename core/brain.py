
class Brain:
    def __init__(self):
        pass

    def proccess_command(self, command: str) -> dict:
        command = command.lower()
        if "wikipedia" in command:
            return {"action": "search_wikipedia", "query": command}
        elif "weather" in command:
            return {"action": "get_weather", "query": command}
        elif "time" in command:
            return {"action": "get_time", "query": command}
        elif "stop" in command:
            return {"action": "stop_listener"}
        else:
            return {"action": "unknown", "query": command}