from Image import Image
from BitPlaneManager import BitPlaneManager
import cv2

class LsbPlaneWatermarker:
    @staticmethod
    def add_watermark(image: Image, watermark: Image) -> Image:
        (blue_channel, green_channel, red_channel) = image.get_rgb()
        bit_plane_index = 0
        
        red_bin_planes = BitPlaneManager.split_channel_into_bit_planes(red_channel)
        green_bin_planes = BitPlaneManager.split_channel_into_bit_planes(green_channel)
        
        red_bin_planes[bit_plane_index] = BitPlaneManager.insert_watermark_into_bit_plane(red_bin_planes[bit_plane_index], watermark)
        green_bin_planes[bit_plane_index] = BitPlaneManager.insert_watermark_into_bit_plane(green_bin_planes[bit_plane_index], watermark)
        
        red_channel_with_watermark = BitPlaneManager.construct_channel_from_bit_planes(red_bin_planes)
        green_channel_with_watermark = BitPlaneManager.construct_channel_from_bit_planes(green_bin_planes)
        
        marked_rgb_data = cv2.merge([blue_channel.data,
                                green_channel_with_watermark.data,
                                red_channel_with_watermark.data])
            
        marked_image = Image(data=marked_rgb_data)
        return marked_image
    
    @staticmethod
    def get_watermark(source_image: Image,
                      marked_image: Image) -> Image:
        bit_plane_index = 0
        source_green = source_image.get_rgb()[1]
        marked_green = marked_image.get_rgb()[1]
        
        source_bit_plane = BitPlaneManager.split_channel_into_bit_planes(source_green)[bit_plane_index]
        marked_bit_plane = BitPlaneManager.split_channel_into_bit_planes(marked_green)[bit_plane_index]
        watermark = BitPlaneManager.get_watermark_from_bit_plane(source_bit_plane, marked_bit_plane)
        return watermark
                