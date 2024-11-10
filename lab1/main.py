from Image import Image
from LsbPlaneWatermarker import LsbPlaneWatermarker
from SimpleQimWatermarker import SimpleQimWatermarker
from constants import *


def task12():
    baboon_image = Image("baboon.tif")
    watermark_ornament = Image("ornament.tif")
    watermark_mickey = Image("mickey.tif")
    
    _, green_channel, red_channel = baboon_image.get_rgb()
    baboon_image_with_watermark = LsbPlaneWatermarker.add_watermarks_to_green_and_red(baboon_image, watermark_ornament, watermark_mickey)    
    _, green_watermarked, red_watermarked = baboon_image_with_watermark.get_rgb()
    
    returned_ornament, returned_mickey =  LsbPlaneWatermarker.get_watermarks_from_green_and_red(baboon_image, baboon_image_with_watermark)
    
    baboon_image.show()
    green_channel.show()
    green_watermarked.show()
    red_channel.show()
    red_watermarked.show()
    baboon_image_with_watermark.show()
    returned_ornament.show()
    returned_mickey.show()

def task34():
    baboon_image = Image("baboon.tif")
    baboon_image.show()
    
    watermark = Image("ornament.tif")
    
    _, cr, _ = baboon_image.get_yCrCb()
    cr.show()
    
    baboon_image_with_watermark = SimpleQimWatermarker.insert_watermark(baboon_image, watermark)
    baboon_image_with_watermark.show()
    
    _, cr_watermarked, _ = baboon_image_with_watermark.get_yCrCb()
    cr_watermarked.show()
    
    recovered_watermark = SimpleQimWatermarker.get_watermark(baboon_image_with_watermark)
    recovered_watermark.show()

if __name__ == "__main__": 
    task34()