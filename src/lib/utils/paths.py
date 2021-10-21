from pathlib import PurePath


def videos_folder_path(video_name):
    return PurePath('assets', video_name, 'videos')


def video_path(video_name):
    path = PurePath('assets', video_name, 'videos',
                    '{}.mp4'.format(video_name))
    return str(path)


def images_folder_path(image_name):
    path = PurePath('assets', image_name, 'images')
    return str(path)


def image_path(image_name, frame_name):
    path = PurePath('assets', image_name, 'images',
                    '{}.png'.format(frame_name))
    return str(path)
