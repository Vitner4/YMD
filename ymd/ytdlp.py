

class YTDLPLogger:
    def __init__(self, log):
        self.log = log

    def debug(self, msg):
        self.log.info(msg)

    def info(self, msg):
        self.log.info(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)
