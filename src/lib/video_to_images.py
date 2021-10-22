from lib.utils.paths import video_path, original_image_path
import cv2


def video_to_images(video_name):
    video = cv2.VideoCapture(video_path(video_name))
    frame_index = 0

    success, frame = video.read()

    while True:
        success, frame = video.read()
        frame_index += 1

        if not success:
            break

        image_path = original_image_path(video_name, str(frame_index))
        cv2.imwrite(image_path, frame)
