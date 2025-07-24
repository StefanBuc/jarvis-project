from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from core.commandHandler import CommandHandler
from utils.logger import Logger
import datasets
from typing import cast

logger = Logger().get_logger()
# listener = Listener()
# speaker = Speaker()
brain = Brain()
command_handler = CommandHandler()

print(brain.proccess_command("What is the weather?")) 

# while True:

#     phrase = listener.listen()
#     command = brain.proccess_command(phrase)
#     response = command_handler.handle_command(command)
#     if command['action'] == "stop_listener":
#         logger.info("Stopping listener as per command.")
#         break
    
#     speaker.speak(response)
#     logger.info(f"Command processed: {command}, Response: {response}")
