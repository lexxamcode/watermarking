import numpy as np
from constants import *

class OmegaVectorGenerator:
    @staticmethod
    def generate(size: int) -> np.ndarray:
        omega_vector = np.random.normal(mean, std, size)
        np.save("omega_vector.npy", omega_vector)
        return omega_vector