from pytube import YouTube

from lib.format_text import format_text
from lib.utils.paths import videos_folder_path

from config.extensions import video_extension


def youtube_downloader(youtube_url):
    try:
        print('[youtube_downloader] Searching video...')

        youtube_response = YouTube(youtube_url)
        stream = youtube_response.streams.filter(
            progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        print('[youtube_downloader] Downloading {}...'.format(stream.title))

        video_name = format_text(stream.title)
        video_folder_path = videos_folder_path(video_name)
        video_path = 'original.{}'.format(video_extension)

        stream.download(output_path=video_folder_path, filename=video_path)

        print('[youtube_downloader] {} downloaded!'.format(stream.title))

        return video_name
    except ValueError:
        print('Algo deu errado!')
