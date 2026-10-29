import yt_dlp
from .ytdlp import *
from pathlib import Path
from .lib.MicroLog.microlog import Logger


class Downloader:
    def __init__(self):
        self.log = Logger()

    def start(self, data: dict) -> None:
        Path(data["output_path"]).mkdir(parents=True, exist_ok=True)

        if data["noplaylist"]:
            outtmpl = f"{data['output_path']}/%(title)s.%(ext)s"
        else:
            outtmpl = f"{data['output_path']}/%(playlist_title)s/%(title)s.%(ext)s"

        ydl_opts = {
            "logger": YTDLPLogger(self.log),
            "format": "bestaudio/best",
            "outtmpl": outtmpl,

            "writethumbnail": True,

            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": data["format"],
                    "preferredquality": data["quality"],
                },
                {
                    "key": "EmbedThumbnail",
                },
                {
                    "key": "FFmpegMetadata",
                },
            ],

            "embedthumbnail": data["embed_thumbnail"],
            "noplaylist": data["noplaylist"],

            "parse_metadata": [
                "title:%(artist)s - %(title)s"
            ],

            "metadata_from_title": "%(artist)s - %(title)s",
        }

        self._download(ydl_opts, data["url"])

    def _download(self, opts: dict, url: list[str]) -> None:
        with yt_dlp.YoutubeDL(opts) as ydl:                            
            self.log.info("Start loading")
            ydl.download(url)
            self.log.info("Download completed successfully.")
        
        
