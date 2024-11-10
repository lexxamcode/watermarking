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
    watermarked_high_and_medium_fft = Watermarker.insert_watermark(high_and_medium_fft)
    
    watermarked_entire_fft = np.array((watermarked_high_and_medium_fft + zones["low"]))
    watermarked_baboon = DftCalculator.inverse_and_return_for(watermarked_entire_fft)
    # cv2.imwrite("watermarked_baboon.png", watermarked_baboon.astype(np.float64))
    
    # print(watermarked_entire_fft[0][0])
    # print(baboon_image_fft[0][0])
    # cv2.imshow("baboon", baboon_image.astype(np.uint8)) # redo as imwrite
    # cv2.imshow("fft", baboon_image_fft.astype(np.uint8))
    # cv2.imshow("watermarked_fft", watermarked_entire_fft.astype(np.uint8))
    # cv2.imshow("watermarked_baboon", watermarked_baboon.astype(np.uint8))
    # cv2.imshow("difference between fft", (watermarked_entire_fft - baboon_image_fft).astype(np.uint8) * 255)
    cv2.waitKey(0)
    
    # Proverka
    watermarked_entire_fft2 = DftCalculator.calculate_and_return_for(watermarked_baboon)
    default_omega_vector_indices, _ = Watermarker.get_indices_for_insertion_and_vector_length(zones["high"] + zones["medium"])
    watermarked_omega_vector_place = watermarked_entire_fft2[default_omega_vector_indices[:, 0], default_omega_vector_indices[:, 1]]
    just_baboon_omega_vector_place = baboon_image_fft[default_omega_vector_indices[:, 0], default_omega_vector_indices[:, 1]]
    
    omega_estimate = (watermarked_omega_vector_place - just_baboon_omega_vector_place) / (alpha * just_baboon_omega_vector_place)
    omega_real = np.load("omega_vector.npy")

    # print(np.linalg.norm(watermarked_entire_fft.flatten() - watermarked_entire_fft2.flatten()))
    
    detect = sum(np.multiply(omega_estimate, omega_real)) / (np.sqrt(np.sum(omega_real**2)) * np.sqrt(np.sum(omega_estimate**2)))
    print("Порог четотам: ", detect.real)
    #