from pathlib import PurePath
from os import path, makedirs

from config.extensions import video_extension, image_extension
from config.filenames import video_original, video_cartoon


def videos_folder_path(folder_name):
    return PurePath('assets', folder_name, 'videos')


def original_video_folder_path(video_name):
    return PurePath(
        'assets',
        video_name,
        'videos',
        '{}.{}'.format(video_original, video_extension)
    )


def cartoon_video_folder_path(folder_name):
    full_path = PurePath(
        'assets',
        folder_name,
        'videos',
        '{}.{}'.format(video_cartoon, video_extension)
    )

    return str(full_path)


def original_video_path(folder_name):
    full_path = PurePath(
        'assets',
        folder_name,
        'videos',
        '{}.{}'.format(video_original, video_extension)
    )

    return str(full_path)


def cartoon_video_path(folder_name):
    full_path = PurePath(
        'assets',
        folder_name,
        'videos',
        '{}.{}'.format(video_cartoon, video_extension)
    )

    return str(full_path)


def original_images_folder_path(folder_name):
    full_path = PurePath('assets', folder_name, 'images', 'originals')
    return str(full_path)


def images_folder_path(folder_name):
    full_path = PurePath('assets', folder_name, 'images')
    return str(full_path)


def original_image_path(folder_name, frame_name):
    full_folder_path = PurePath('assets', folder_name, 'images', 'originals')

    if not path.exists(full_folder_path):
        makedirs(full_folder_path)

    if '.{}'.format(image_extension) not in frame_name:
        frame_name += '.{}'.format(image_extension)

    full_path = PurePath(full_folder_path, '{}'.format(frame_name))

    return str(full_path)


def cartoons_images_folder_path(folder_name):
    full_path = PurePath('assets', folder_name, 'images', 'cartoons')
    return str(full_path)


def cartoon_image_path(folder_path, frame_name):
    full_folder_path = PurePath('assets', folder_path, 'images', 'cartoons')

    if not path.exists(full_folder_path):
        makedirs(full_folder_path)

    if '.{}'.format(image_extension) not in frame_name:
        frame_name += '.{}'.format(image_extension)

    full_path = PurePath(full_folder_path, '{}'.format(frame_name))

    return str(full_path)
