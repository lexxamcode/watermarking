import numpy as np
import scipy

class DftCalculator:
    @staticmethod
    def calculate_and_return_for(array: np.ndarray) -> np.ndarray:
        return scipy.fftpack.fft(scipy.fftpack.fft(array, axis=0), axis=1)
    
    @staticmethod
    def inverse_and_return_for(fft_array: np.ndarray) -> np.ndarray:
        return scipy.fftpack.ifft(scipy.fftpack.ifft(fft_array, axis=0), axis=1)