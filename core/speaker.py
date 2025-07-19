import pyttsx3

class Speaker:
    def __init__(self, rate=200, voice=None, volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('voice', voice)
        self.engine.setProperty('volume', volume)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)
    
    def set_voice(self, voice):
        self.engine.setProperty('voice', voice)
    
    def set_volume(self, volume):
        self.engine.setProperty('volume', volume)
    
    def get_rate(self):
        return self.engine.getProperty('rate')
    
    def get_voice(self):
        return self.engine.getProperty('voice')
    
    def get_volume(self):
        return self.engine.getProperty('volume')
    