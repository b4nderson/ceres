from lib.utils.paths import original_video_path, original_image_path
import cv2


def video_to_images(folder_name):
    try:
        print('[video_to_images] Converting video to images...')

        video = cv2.VideoCapture(original_video_path(folder_name))
        frame_index = 0

        success, frame = video.read()

        while True:
            success, frame = video.read()
            frame_index += 1

            if not success:
                break

            image_path = original_image_path(folder_name, str(frame_index))
            cv2.imwrite(image_path, frame)

        cv2.destroyAllWindows()
        print('[video_to_images] Video to images converted!')
    except ValueError:
        print('[video_to_images] Its not possible convert video to images!')
