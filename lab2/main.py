from MatrtixSplitter import MatrixSplitter
from Watermarker import Watermarker
from DftCalculator import DftCalculator
import cv2
import numpy as np

if __name__ == "__main__":
    baboon_image = cv2.imread("baboon.tif", cv2.IMREAD_GRAYSCALE)
    baboon_image_fft = DftCalculator.calculate_and_return_for(baboon_image)
    
    zones = MatrixSplitter.split_into_fft_zones_and_return(baboon_image_fft)
    entire_high_and_medium_zones_matrices = np.fromiter((zones["high"], zones["medium"]), dtype=np.ndarray)
    high_and_medium_fft = MatrixSplitter \
        .construct_matrix_from_its_fft_zones(entire_high_and_medium_zones_matrices)
    watermarked_high_and_medium_fft = Watermarker.insert_watermark(high_and_medium_fft)
    
    watermarked_entire_fft = (watermarked_high_and_medium_fft + zones["low"])

    watermarked_baboon = DftCalculator.inverse_and_return_for(watermarked_entire_fft)
    
    difference = watermarked_entire_fft - baboon_image_fft
    print(len(difference[abs(difference) > 0.001]))
    
    print(watermarked_baboon)
    cv2.imshow("baboon", baboon_image.astype(np.uint8))
    cv2.imshow("fft", baboon_image_fft.astype(np.uint8))
    cv2.imshow("watermarked_fft", watermarked_entire_fft.astype(np.uint8))
    cv2.imshow("watermarked_baboon", watermarked_baboon.astype(np.uint8))
    cv2.imshow("difference between fft", (watermarked_entire_fft - baboon_image_fft).astype(np.uint8) * 255)
    cv2.waitKey(0)
    