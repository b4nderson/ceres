from moviepy.editor import VideoFileClip, AudioFileClip
from lib.utils.paths import (
    cartoon_video_path, original_audio_path, output_video_path)


def join_video_with_audio(folder_name):
    try:
        print('[join_video_with_audio] joining video with audio...')

        video_path = cartoon_video_path(folder_name)
        audio_path = original_audio_path(folder_name)
        output_path = output_video_path(folder_name)

        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)

        output = video.set_audio(audio)
        output.write_videofile(output_path)

        print('[join_video_with_audio] Video to audio joined!')
    except ValueError:
        print('[join_video_with_audio] Its not possible join video to audio!')
