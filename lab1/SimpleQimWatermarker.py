from Image import Image
from constants import *

class SimpleQimWatermarker:
    @staticmethod
    def insert_watermark(image: Image, watermark: Image) -> Image:
        y_channel, cr_channel, cb_channel = image.get_yCrCb()
        v_matrix = cr_channel.data % delta
        
        marked_cr = ((cr_channel.data // (2*delta)) * (2 * delta)) + watermark.data[:, :, 0] * delta + v_matrix
        
        marked_image_data = cv2.merge([y_channel.data, marked_cr, cb_channel.data])
        rgb_marked_image_data = cv2.cvtColor(marked_image_data, cv2.COLOR_YCR_CB2BGR)
        
        result_image = Image(data=rgb_marked_image_data, name="Watermarked image")
        return result_image
    
    @staticmethod
    def get_watermark(marked_image: Image) -> Image:
        _, cr_channel, _ = marked_image.get_yCrCb()
        v_matrix = cr_channel.data % delta
        
        watermark = cr_channel.data - ((cr_channel.data// (2*delta)) * (2*delta)) - v_matrix
        watermark *= 255
        
        watermark_image = Image(data=watermark, name="Watermark")
        return watermark_image        