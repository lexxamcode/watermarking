from Image import Image
from LsbPlaneWatermarker import LsbPlaneWatermarker
from SimpleQimWatermarker import SimpleQimWatermarker
from constants import *


def task12():
    baboon_image = Image("baboon.tif")
    watermark = Image("ornament.tif")
    
    baboon_image.show()
    
    baboon_image_with_watermark = LsbPlaneWatermarker.add_watermark(baboon_image, watermark)
    baboon_image_with_watermark.show()
    
    watermark = LsbPlaneWatermarker.get_watermark(baboon_image, baboon_image_with_watermark)
    watermark.show()

def task34():
    baboon_image = Image("baboon.tif")
    watermark = Image("ornament.tif")
    baboon_image.show()
    
    baboon_image_with_watermark = SimpleQimWatermarker.insert_watermark(baboon_image, watermark)
    baboon_image_with_watermark.show()
    
    recovered_watermark = SimpleQimWatermarker.get_watermark(baboon_image_with_watermark)
    recovered_watermark.show()

if __name__ == "__main__": 
    task34()