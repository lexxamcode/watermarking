from MatrtixSplitter import MatrixSplitter
from Watermarker import Watermarker
from DftCalculator import DftCalculator
from constants import *
from scipy.spatial.distance import cosine
import cv2
import numpy as np

if __name__ == "__main__":
    baboon_image = cv2.imread("baboon.tif", cv2.IMREAD_GRAYSCALE)
    baboon_image_fft = DftCalculator.calculate_and_return_for(baboon_image)
    
    zones = MatrixSplitter.split_into_fft_zones_and_return(baboon_image_fft)
    entire_high_and_medium_zones_matrices = np.fromiter((zones["high"], zones["medium"]), dtype=np.ndarray)
    high_and_medium_fft = MatrixSplitter \
        .construct_matrix_from_its_fft_zones(entire_high_and_medium_zones_matrices)
    watermarked_high_and_medium_fft = Watermarker.insert_watermark2(high_and_medium_fft)
    
    watermarked_entire_fft = np.array((watermarked_high_and_medium_fft + zones["low"]))
    watermarked_baboon = DftCalculator.inverse_and_return_for(watermarked_entire_fft)
    # cv2.imwrite("watermarked_baboon.png", watermarked_baboon.astype(np.float64))
    
    # print(watermarked_entire_fft[0][0])
    # print(baboon_image_fft[0][0])
    # cv2.imshow("baboon", baboon_image.astype(np.uint8)) # redo as imwrite
    # cv2.imshow("fft", baboon_image_fft.astype(np.uint8))
    cv2.imshow("watermarked_fft", watermarked_entire_fft.astype(np.uint8))
    cv2.imshow("watermarked_baboon", watermarked_baboon.astype(np.uint8))
    cv2.imshow("difference between fft", (watermarked_entire_fft - baboon_image_fft).astype(np.uint8) * 255)
    cv2.waitKey(0)
    
    # Proverka
    watermarked_entire_fft2 = DftCalculator.calculate_and_return_for(watermarked_baboon)
    
    omega_estimate = watermarked_entire_fft2[0:256, ((512 - 40) // 2):((512 - 40) // 2) + 40]
    omega_real = np.load("omega_vector2.npy")

    # print(np.linalg.norm(watermarked_entire_fft.flatten() - watermarked_entire_fft2.flatten()))
    print(len(omega_estimate.flatten()))
    detect = sum(np.multiply(omega_estimate.flatten(), omega_real))
    print("Порог четотам: ", detect.real)
    #