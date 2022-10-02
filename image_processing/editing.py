import cv2
import numpy
from image_processing.models import RGBImages, CombinedImage


class ImageEditor:
    def __init__(self, image_r, image_g, image_b):
        self.rgb_images = RGBImages.objects.get(image_r=image_r)
        self.image_r = cv2.iamread(f"../media/{image_r}", cv2.IMREAD_GRAYSCALE)
        self.image_g = cv2.iamread(f"../media/{image_g}", cv2.IMREAD_GRAYSCALE)
        self.image_b = cv2.iamread(f"../media/{image_b}", cv2.IMREAD_GRAYSCALE)

    def combine_images(self):
        # Add the channels to the final image
        final_img = numpy.dstack([self.image_b, self.image_g, self.image_r]).astype(numpy.uint8)

        # Save the needed multi channel image
        combined_image = CombinedImage(from_images=self.rgb_images, image=final_img)
        combined_image.save()
        return combined_image
