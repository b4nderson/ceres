from lib.utils.paths import original_video_path, original_audio_path
from moviepy.editor import VideoFileClip


def video_to_audio(folder_name):
    try:
        print('[video_to_audio] Converting video to audio...')

        video_path = original_video_path(folder_name)
        video = VideoFileClip(video_path)

        audio_path = original_audio_path(folder_name)
        video.audio.write_audiofile(audio_path)

        print('[video_to_audio] Video to audio converted!')
    except ValueError:
        print('[video_to_audio] Its not possible convert video to audio!')
