from .cli import CLI
from .lib.MicroLog.microlog import Logger


class Main:
    def __init__(self):
        self.cli = CLI()
        self.log = Logger()

    def run(self, arguments=None):
        try:
            self.cli.parse()
            return

        except Exception as e:
            Main().log.error(e)

def main():
    Main().run()
