from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain

listener = Listener()
speaker = Speaker()
brain = Brain()

while True:
    phrase = listener.listen()
    command = brain.proccess_command(phrase)
    if command['action'] == 'stop_listener':
        print("Stopping listener...")
        break
    elif command['action'] == 'unknown':
        print(f"Unknown command: {command['query']}")
    else:
        print(f"Processing command: {command['action']} with query: {command['query']}")
        # Here you would handle the command, e.g., search Wikipedia, get weather, etc.

    speaker.speak(phrase)
