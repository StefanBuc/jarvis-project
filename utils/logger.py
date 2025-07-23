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
        config_file = pathlib.Path("config/logging.json")
        with open(config_file, 'r') as file:
            config = json.load(file)
        logging.config.dictConfig(config)
        queue_handler = logging.getHandlerByName("queue_handler")
        if queue_handler is not None:
            queue_handler = cast("QueueHandlerWithListener", queue_handler)
            queue_handler.listener.start()
            atexit.register(queue_handler.listener.stop)

    def get_logger(self):
        return self.logger
    
        
