from vosk import Model, KaldiRecognizer
import queue
import sounddevice
import os
import json
from utils.logger import Logger

class Listener:
    def __init__(self, logger: Logger, model_path = os.path.join(os.path.dirname(__file__), "../models/vosk-model-en-us-0.22")):
        self.logger = logger.get_logger()
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000, open("config/keywords.list").read())
        self.recognizer.SetWords(True)
        self.audio_queue = queue.Queue()
        
        self.stream = sounddevice.InputStream(
            samplerate=16000,
            channels=1,
            dtype='int16',
            callback=self.audio_callback
        )
        self.stream.start()

    def audio_callback(self, indata, frames, time, status):
        if status:
            self.logger.warning(f"Audio callback status: {status}")
        self.audio_queue.put(bytes(indata))

    def listen(self) -> str:
        self.logger.info("Starting to listen for audio input...")
        while True:
            if not self.audio_queue.empty():
                data = self.audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    self.logger.info(f"Recognition result: {result}")
                    return result.get('text', '')

    def listen_for_wake_word(self, wake_word: str) -> bool:
        self.logger.info(f"Listening for wake word: {wake_word}")
        while True:
            if not self.audio_queue.empty():
                data = self.audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get('text', '')
                    if wake_word.lower() in text.lower():
                        self.logger.info(f"Wake word '{wake_word}' detected.")
                        return True
                    
    def stop(self):
        self.logger.info("Stopping audio stream...")
        self.stream.stop()
        self.stream.close()
        self.logger.info("Audio stream stopped.")