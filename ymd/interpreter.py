from .loader import Downloader
from .lib.MicroLog.microlog import Logger
from .manager import *


class Interpreter:
    def __init__(self):
        self.log = Logger()
        self.loader = Downloader()
        self.paths = Paths()

    def interpret(self, args):
        if args.path:
            output_path = self.paths.save(args.path)
            self.log.info(f"Path set successfully. New path: {output_path}")
            return
        else:
            output_path = self.paths.load()

        if args.get_path:
            print(self.paths.get_path())
            return

        if args.config:
            print(self.paths.get_config_path())
            return

        if not args.url:
            self.log.error("URL not specified")
            return
                
        data = {
            "noplaylist": not args.playlist,
            "url": args.url,
            "format": "mp3",
            "quality": "0",
            "output_path": str(output_path),
            "embed_thumbnail": True,
        }

        self.loader.start(data)
    

