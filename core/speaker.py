import pyttsx3
from utils.logger import Logger

class Speaker:
    def __init__(self, logger: Logger, rate=200, voice=None, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('voice', voice)
        self.engine.setProperty('volume', volume)
        self.logger = logger.get_logger()
        self.logger.info(f"Speaker initialized with rate: {rate}, voice: {voice}, volume: {volume}")

    def speak(self, text):
        self.logger.info(f"Speaking text: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.logger.info("Stopping speech synthesis.")
        self.engine.stop()

    def set_rate(self, rate):
        self.logger.info(f"Setting speech rate to: {rate}")
        self.engine.setProperty('rate', rate)
    
    def set_voice(self, voice):
        self.logger.info(f"Setting speech voice to: {voice}")
        self.engine.setProperty('voice', voice)
    
    def set_volume(self, volume):
        self.logger.info(f"Setting speech volume to: {volume}")
        self.engine.setProperty('volume', volume)
    
    def get_rate(self):
        return self.engine.getProperty('rate')
    
    def get_voice(self):
        return self.engine.getProperty('voice')
    
    def get_volume(self):
        return self.engine.getProperty('volume')
    