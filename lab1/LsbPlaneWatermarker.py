from Image import Image
from BitPlaneManager import BitPlaneManager
import cv2

class LsbPlaneWatermarker:
    @staticmethod
    def construct_image_from_rgb(blue_channel: Image,
                                 green_channel: Image,
                                 red_channel: Image) -> Image:    
        marked_rgb_data = cv2.merge([blue_channel.data,
                                green_channel.data,
                                red_channel.data])
            
        marked_image = Image(data=marked_rgb_data)
        return marked_image
    
    @staticmethod
    def add_watermark_to_channel(channel: Image,
                                 watermark: Image,
                                 bit_plane_index: int = 0) -> Image:
        bit_planes = BitPlaneManager.split_channel_into_bit_planes(channel)
        bit_planes[bit_plane_index] = BitPlaneManager.insert_watermark_into_bit_plane(bit_planes[bit_plane_index], watermark)
        
        return BitPlaneManager.construct_channel_from_bit_planes(bit_planes)
    
    @staticmethod
    def get_watermark_from_channel(source_channel: Image,
                                   marked_channel: Image,
                                   bit_plane_index: int = 0) -> Image:
        source_bit_plane = BitPlaneManager.split_channel_into_bit_planes(source_channel)[bit_plane_index]
        marked_bit_plane = BitPlaneManager.split_channel_into_bit_planes(marked_channel)[bit_plane_index]
        
        watermark = BitPlaneManager.get_watermark_from_bit_plane(source_bit_plane, marked_bit_plane)
        return watermark
    
    @staticmethod
    def add_watermarks_to_green_and_red(image: Image, watermark_green: Image, watermark_red: Image) -> Image:
        blue_channel, green_channel, red_channel = image.get_rgb()
        
        green_channel = LsbPlaneWatermarker.add_watermark_to_channel(green_channel, watermark_green)
        red_channel = LsbPlaneWatermarker.add_watermark_to_channel(red_channel, watermark_red)
        
        watermarked_image = LsbPlaneWatermarker.construct_image_from_rgb(blue_channel, green_channel, red_channel)
        return watermarked_image
    
    @staticmethod
    def get_watermarks_from_green_and_red(image: Image, watermarked_image: Image) -> list:
        _, green_channel, red_channel = image.get_rgb()
        _, green_channel_watermarked, red_channel_watermarked = watermarked_image.get_rgb()
        
        watermark_green = LsbPlaneWatermarker.get_watermark_from_channel(green_channel, green_channel_watermarked)
        watermark_red = LsbPlaneWatermarker.get_watermark_from_channel(red_channel, red_channel_watermarked)
        
        return [watermark_green, watermark_red]