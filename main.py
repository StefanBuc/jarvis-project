from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from core.commandHandler import CommandHandler
from utils.logger import Logger

log = Logger()
listener = Listener(log)
speaker = Speaker(log)
brain = Brain(log)
command_handler = CommandHandler(log)
logger = log.get_logger()

print("Jarvis is ready to listen...")

try:
    while True:
        if listener.listen_for_wake_word("jarvis"):
            logger.info("Wake word detected, listening for command...")
            speaker.speak("Yes?")
            phrase = listener.listen()
            command = brain.proccess_command(phrase)
            response = command_handler.handle_command(command)
            if command["text"] == "stop":
                logger.info("Stopping listener as per command.")
                break
            
            speaker.speak(response)
            logger.info(f"Command processed: {command}, Response: {response}")

finally:
    logger.info("Shutting down.")
    listener.stop()
    speaker.stop()
    logger.info("Shut down complete.")
    log.shutdown()
    print("Shut down complete.")
