import json
import logging.config
import atexit
import pathlib
from typing import cast, TYPE_CHECKING

if TYPE_CHECKING:
    from utils.logger import QueueHandlerWithListener

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("Jarvis")
        self.queue_hander = None
        self.listener = None
        config_file = pathlib.Path("config/logging.json")
        with open(config_file, 'r') as file:
            config = json.load(file)
        logging.config.dictConfig(config)
        self.queue_handler = logging.getHandlerByName("queue_handler")
        if self.queue_handler is not None:
            self.queue_handler = cast("QueueHandlerWithListener", self.queue_handler)
            self.listener = self.queue_handler.listener
            if self.listener is not None:
                self.listener.start()
        

    def get_logger(self):
        return self.logger

    def shutdown(self):
        if self.listener is not None:
            self.listener.stop()
        logging.shutdown()
    
        
