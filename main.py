from pytube import YouTube
import argparse


class Downloader():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Download YouTube Videos for free!')
        self.parser.add_argument('--url', '-u', metavar='url', required=True, help='YouTube Video URL')
        self.parser.add_argument('--dir', '-d', metavar='save_dir', required=False, help='Save Directory')

    def get_args(self):
        args = self.parser.parse_args()
        self.url = args.url
        try:
            self.directory = args.dir
        except AttributeError:
            self.directory = ''

    def download(self):
        self.get_args()
        video_url = YouTube(self.url)
        video = video_url.streams.get_highest_resolution()
        if self.directory == '':
            video.download()
        else:
            video.download(output_path=self.directory)


if __name__ == '__main__':
    downloader = Downloader()
    downloader.download()