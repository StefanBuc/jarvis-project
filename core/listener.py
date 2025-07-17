from vosk import Model, KaldiRecognizer
import queue
import sounddevice
import os
import json

class Listener:
    def __init__(self, model_path = os.path.join(os.path.dirname(__file__), "../models/vosk-model-en-us-0.22")):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
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
            print("Audio status:", status)
        self.audio_queue.put(bytes(indata))

    def listen(self):
        print("Listening...")
        while True:
            if not self.audio_queue.empty():
                data = self.audio_queue.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    if "stop" in result.get('text'):
                        print("Stopping listener.")
                        break
                else:
                    partial_result = json.loads(self.recognizer.PartialResult())
                    print("Partial result:", partial_result.get('partial', ''))
