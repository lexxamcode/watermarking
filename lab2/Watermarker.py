from constants import *
import numpy as np

class Watermarker:
    @staticmethod
    def insert_watermark(fft_matrix: np.ndarray) -> np.ndarray:
        watermarked_fft = np.copy(fft_matrix)
        
        indices = np.argwhere(watermarked_fft)

        # Сортируем индексы по значениям элементов массива
        sorted_indices = indices[np.argsort(watermarked_fft[indices[:, 0], indices[:, 1]])]

        # Выбираем первую 1/4 отсортированных индексов
        quarter_indices = sorted_indices[:len(sorted_indices) // 2]

        # Добавляем случайное число к значениям элементов, соответствующих выбранным индексам
        random_values = np.random.normal(mean, std, len(quarter_indices))
        watermarked_fft[quarter_indices[:, 0], quarter_indices[:, 1]] += random_values
        
        return watermarked_fft