from lib.utils.paths import original_image_path, original_images_folder_path
from lib.utils.paths import cartoon_image_path

from os import listdir
import cv2


def images_to_cartoons(folder_name):
    images = listdir(original_images_folder_path(folder_name))

    for image_index in range(1, len(images)):
        image_path = original_image_path(folder_name, image_index)
        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        color = cv2.bilateralFilter(image, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        cartoon_path = cartoon_image_path(folder_name, str(image_index))
        cv2.imwrite(cartoon_path, cartoon)
