import cv2 as cv
import numpy
from image_processing.models import RGBImages, CombinedImage
from time import sleep

class ImageEditor:
    def __init__(self, image_r, image_g, image_b, from_images):
        self.from_images = from_images
        self.image_r = cv.imread(f"./media/{image_r}", cv.IMREAD_GRAYSCALE)
        self.image_g = cv.imread(f"./media/{image_g}", cv.IMREAD_GRAYSCALE)
        self.image_b = cv.imread(f"./media/{image_b}", cv.IMREAD_GRAYSCALE)

    def combine_images(self):
        # Add the channels to the final image
        final_img = cv.merge([self.image_b, self.image_g, self.image_r])
        cv.imwrite(f"./media/images/{self.from_images.id}.png", final_img)
        # Save the needed multi channel image
        combined_image = CombinedImage(from_images=self.from_images,
                                       image=f"/images/{self.from_images.id}.png")
        combined_image.save()
        return combined_image
