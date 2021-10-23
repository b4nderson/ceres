
from lib.cartoons_to_video import cartoons_to_video
from lib.join_video_with_audio import join_video_with_audio
from lib.video_to_audio import video_to_audio
from lib.youtube_downloader import youtube_downloader
from lib.video_to_images import video_to_images
from lib.images_to_cartoons import images_to_cartoons

#from services.insert_data_service import insert_data_service


def main():
    youtube_url = input('VIDEO URL: ')

    folder_name = youtube_downloader(youtube_url)
    # insert_data_service(folder_name)
    video_to_audio(folder_name)
    video_to_images(folder_name)
    images_to_cartoons(folder_name)
    cartoons_to_video(folder_name)
    join_video_with_audio(folder_name)


main()
