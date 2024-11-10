from DftCalculator import DftCalculator
from MatrtixSplitter import MatrixSplitter
from Watermarker import Watermarker
from scipy.spatial.distance import cosine
from constants import *
import numpy as np
import cv2

if __name__ == "__main__":
    watermarked_baboon = cv2.imread("watermarked_baboon.tif", cv2.IMREAD_GRAYSCALE).astype(np.uint8)
    print(watermarked_baboon.shape)
    watermarked_baboon_fft = DftCalculator.calculate_and_return_for(watermarked_baboon)
    cv2.imshow("watermarked fft", watermarked_baboon_fft.astype(np.uint8))
    
    just_baboon = cv2.imread("baboon.tif", cv2.IMREAD_GRAYSCALE)
    just_baboon_fft = DftCalculator.calculate_and_return_for(just_baboon)
    
    print(watermarked_baboon_fft[0][0])
    print(just_baboon_fft[0][0])
    
    cv2.imshow("source baboon fft", just_baboon_fft.astype(np.uint8))
    
    just_baboon_fft_zones = MatrixSplitter.split_into_fft_zones_and_return(just_baboon_fft)
    watermark_baboon_fft_zones = MatrixSplitter.split_into_fft_zones_and_return(watermarked_baboon_fft)
    default_omega_vector_indices, _ = Watermarker.get_indices_for_insertion_and_vector_length(just_baboon_fft_zones["high"] + just_baboon_fft_zones["medium"])
    print(default_omega_vector_indices)
    
    watermarked_omega_vector_place = watermarked_baboon_fft[default_omega_vector_indices[:, 0], default_omega_vector_indices[:, 1]]
    print(len(watermarked_omega_vector_place))
    just_baboon_omega_vector_place = just_baboon_fft[default_omega_vector_indices[:, 0], default_omega_vector_indices[:, 1]]
    print(len(just_baboon_omega_vector_place))

    omega_estimate = (watermarked_omega_vector_place.real - just_baboon_omega_vector_place.real) / (alpha * just_baboon_omega_vector_place.real)
    omega_real = np.load("omega_vector.npy")
    print(cosine(omega_estimate, omega_real))
    cv2.waitKey(0)