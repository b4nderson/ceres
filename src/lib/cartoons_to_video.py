from lib.utils.paths import (
    cartoon_image_path, cartoons_images_folder_path, cartoon_video_folder_path)

from lib.utils.sorted_alphanumeric import sorted_alphanumeric

from config.video import frame_rate

from os import listdir
import cv2


def cartoons_to_video(folder_name):
    try:
        print('[cartoons_to_video] Converting cartoons to video...')

        cartoon_list = sorted_alphanumeric(
            listdir(cartoons_images_folder_path(folder_name)))
        cartoons = []

        for image__list_index in range(1, len(cartoon_list)):
            cartoon_path = cartoon_image_path(
                folder_name, cartoon_list[image__list_index])

            cartoon = cv2.imread(cartoon_path)

            height, width, layers = cartoon.shape
            size = (width, height)

            cartoons.append(cartoon)

        output_path = cartoon_video_folder_path(folder_name)
        output = cv2.VideoWriter(
            output_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, size)

        for cartoon_index in range(len(cartoons)):
            output.write(cartoons[cartoon_index])

        output.release()
        cv2.destroyAllWindows()

        print('[cartoons_to_video] Cartoons to video converted!')
    except ValueError:
        print(
            '[cartoons_to_video] Its not possible convert cartoons to video!'
        )
