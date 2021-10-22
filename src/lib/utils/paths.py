from pathlib import PurePath
from os import path, makedirs


def videos_folder_path(video_name):
    return PurePath('assets', video_name, 'videos')


def video_path(video_name):
    full_path = PurePath('assets', video_name, 'videos',
                         '{}.mp4'.format(video_name))
    return str(full_path)


def original_images_folder_path(image_name):
    full_path = PurePath('assets', image_name, 'images', 'originals')
    return str(full_path)


def images_folder_path(image_name):
    full_path = PurePath('assets', image_name, 'images')
    return str(full_path)


def original_image_path(image_name, frame_name):
    full_folder_path = PurePath('assets', image_name, 'images', 'originals')

    if not path.exists(full_folder_path):
        makedirs(full_folder_path)

    full_path = PurePath(full_folder_path, '{}.png'.format(frame_name))

    return str(full_path)


def cartoon_image_path(image_name, frame_name):
    full_folder_path = PurePath('assets', image_name, 'images', 'cartoons')

    if not path.exists(full_folder_path):
        makedirs(full_folder_path)

    full_path = PurePath(full_folder_path, '{}.png'.format(frame_name))

    return str(full_path)
