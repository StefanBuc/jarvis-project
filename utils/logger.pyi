import logging
import logging.handlers

class Logger:
    def __init__(self) -> None: ...
    def get_logger(self) -> logging.Logger: ...

class QueueHandlerWithListener(logging.handlers.QueueHandler):
    listener: logging.handlers.QueueListener