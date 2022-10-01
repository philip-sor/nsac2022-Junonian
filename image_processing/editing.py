import cv2
import numpy as np
from image_processing.models import RGBImages, CombinedImage


class ImageEditor:
    def __init__(self, image_r, image_g, image_b):
        self.image_r = cv2.iamread(image_r, cv2.IMREAD_GRAYSCALE)
        self.image_g = cv2.iamread(image_g, cv2.IMREAD_GRAYSCALE)
        self.image_b = cv2.iamread(image_b, cv2.IMREAD_GRAYSCALE)

    def combine_images(self):
        # Add the channels to the final image
        final_img = np.dstack([self.image_b, self.image_g, self.image_r]).astype(np.uint8)

        # Directory to save
        # final_img_dir = store_directory + "\\" + "img" + image_id
        #
        # # Save the needed multi channel image
        # cv2.imwrite(final_img_dir, final_img)


