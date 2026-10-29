import argparse
from .interpreter import Interpreter


class CLI:
    def __init__(self):
        self.inter = Interpreter()
        self.parser = argparse.ArgumentParser(prog="ymd")

        self.parser.add_argument(
                "url",
                nargs="*",
                help="one or more video URLs",
            )

        self.parser.add_argument(
            "-p",
            "--playlist",
            dest="playlist",
            action="store_true",
            help="download playlist",
        )

        self.parser.add_argument(
            "--path",
            type=str,
            help="set download directory",
        )

        self.parser.add_argument(
            "--get_path",
            action="store_true",
            help="get download directory path",
        )

        self.parser.add_argument(
            "--config",
            action="store_true",
            help="get config path",
        )

    def parse(self):
        args = self.parser.parse_args()

        self.inter.interpret(args)