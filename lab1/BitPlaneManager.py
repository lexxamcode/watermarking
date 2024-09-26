from Image import Image
import numpy as np

class BitPlaneManager:
    @staticmethod
    def split_channel_into_bit_planes(image_channel: Image) -> np.ndarray:
        bit_planes_without_shift = image_channel.data[:, :, np.newaxis]
        shift_values = np.arange(8)
        shifted_bit_planes = bit_planes_without_shift >> shift_values
        
        result_bit_planes = shifted_bit_planes & 1
        return result_bit_planes.transpose((2, 0, 1)).astype(np.uint8)
    
    @staticmethod
    def construct_channel_from_bit_planes(bit_planes: np.ndarray) -> Image:
        shift_values = np.arange(8)
        shift_values_expanded = shift_values[:, np.newaxis, np.newaxis]
        shifted_bit_planes = bit_planes << shift_values_expanded
        channel_data = np.sum(shifted_bit_planes, axis=0).astype(np.uint8)
    
        channel = Image(data=channel_data)    
        return channel
    
    @staticmethod
    def insert_watermark_into_bit_plane(bit_plane: np.ndarray,
                                        watermark: Image) -> np.ndarray:
        boolean_watermark = watermark.data[:, :, 0] > 0
        return np.bitwise_xor(bit_plane, boolean_watermark).astype(np.uint8)
    
    @staticmethod
    def get_watermark_from_bit_plane(bit_plane: np.ndarray,
                                     marked_bit_plane: np.ndarray) -> Image:
        watermark = np.bitwise_xor(bit_plane, marked_bit_plane)
        watermark_image = Image(data=watermark * 255)
        return watermark_image