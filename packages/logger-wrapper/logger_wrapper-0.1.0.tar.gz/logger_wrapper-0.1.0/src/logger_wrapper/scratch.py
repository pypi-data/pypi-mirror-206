import logging
import traceback
from datetime import datetime
from pathlib import Path


class SingletonLogger(logging.Logger):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init(*args, **kwargs)
        return cls._instance

    def _init(self, name=None, level=logging.DEBUG, meta=True, date_filename=True, handlers=None):
        super().__init__(name or "root", level)

        if date_filename:
            now = datetime.now()
            log_filename = f"log_{now.strftime('%Y%m%d_%H%M%S')}.log"
        else:
            log_filename = "log.log"

        formatter = logging.Formatter('%(asctime)s,%(msecs)03d,[%(levelname)s:pid=%(process)d:%(threadName)s:%(module)s:%(funcName)s:%(lineno)d],%(message)s')
        self.formatter = formatter
        self.propagate = meta

        if handlers:
            for handler in handlers:
                handler.setFormatter(self.formatter)
                self.addHandler(handler)


class LoggerWrapper(logging.Logger):

    def __init__(self, name: str | Path = None, level: int = logging.DEBUG, meta: bool = True, date_filename: bool = True, handlers=None):
        text = traceback.extract_stack()[-2][3]
        self.instance_name = text[:text.find('=')].strip()
        super().__init__(name, level)

        self.logger = SingletonLogger()

        if handlers:
            for handler in handlers:
                handler.setFormatter(self.logger.formatter)
                self.logger.addHandler(handler)

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        msg = f"{self.instance_name}: {msg}"
        self.logger._log(level, msg, args, exc_info, extra, stack_info)


# Usage example
if __name__ == "__main__":
    handlers = [logging.StreamHandler(),
                logging.FileHandler("test.logs")
                ]

    log1 = LoggerWrapper(name="app", level=logging.DEBUG, meta=True, date_filename=True, handlers=handlers)
    log2 = LoggerWrapper()
    log3 = LoggerWrapper()

    log1.info("test one")
    log2.info("another test output")
    log3.info("Yet another")
