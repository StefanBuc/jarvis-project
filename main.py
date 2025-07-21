from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from core.commandHandler import CommandHandler

listener = Listener()
speaker = Speaker()
brain = Brain()
command_handler = CommandHandler()

while True:
    phrase = listener.listen()
    command = brain.proccess_command(phrase)
    response = command_handler.handle_command(command)
    if command['action'] == "stop_listener":
        print("Stopping listener...")
        break

    speaker.speak(response)
