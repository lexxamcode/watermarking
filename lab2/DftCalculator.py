import numpy as np
import scipy
import scipy.fftpack

class DftCalculator:
    @staticmethod
    def calculate_and_return_for(array: np.ndarray) -> np.ndarray:
        return np.fft.fft2(array)
    
    @staticmethod
    def inverse_and_return_for(fft_array: np.ndarray) -> np.ndarray:
        return np.fft.ifft2(fft_array)