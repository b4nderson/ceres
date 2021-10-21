from pytube import YouTube

from lib.format_text import format_text
from lib.utils.paths import videos_folder_path


def youtube_downloader(youtube_url):
    try:
        youtube_response = YouTube(youtube_url)
        stream = youtube_response.streams.filter(
            progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        video_name = format_text(stream.title)
        video_folder_path = videos_folder_path(video_name)
        video_path = '{}.mp4'.format(video_name)

        stream.download(output_path=video_folder_path, filename=video_path)

        return video_name
    except ValueError:
        print('Algo deu errado!')
