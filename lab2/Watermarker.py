from OmegaVectorGenerator import OmegaVectorGenerator
from constants import *
import numpy as np

class Watermarker:
    @staticmethod
    def insert_watermark(fft_matrix: np.ndarray) -> np.ndarray:
        watermarked_fft = np.copy(fft_matrix)
        indices, length = Watermarker.get_indices_for_insertion_and_vector_length(watermarked_fft)
       
        random_values = OmegaVectorGenerator.generate(length)
        watermarked_fft.real[indices[:, 0], indices[:, 1]] *= (1 + alpha * random_values)
        return watermarked_fft
    
    @staticmethod
    def insert_watermark2(fft_matrix: np.ndarray) -> np.ndarray:
        watermarked_fft = np.copy(fft_matrix)
        indices, length = Watermarker.get_indices_for_insertion_and_vector_length(watermarked_fft)
       
        random_values = OmegaVectorGenerator.generate(length)
        watermarked_fft.real[indices[:, 0], indices[:, 1]] *= (1 + alpha * random_values)
        return watermarked_fft
    
    @staticmethod
    def get_indices_for_insertion_and_vector_length(fft_matrix: np.ndarray) -> tuple:
        indices = np.argwhere(fft_matrix)
        sorted_indices = indices[np.argsort(fft_matrix[indices[:, 0], indices[:, 1]])]
        quarter_indices = sorted_indices[:len(sorted_indices) // 4]
        
        return (quarter_indices, len(sorted_indices) //4 )
    
    @staticmethod
    def read_watermark(fft_matrix: np.ndarray) -> np.ndarray:
        watermarked_fft = np.copy(fft_matrix)
        
        indices = np.argwhere(watermarked_fft)
        sorted_indices = indices[np.argsort(watermarked_fft[indices[:, 0], indices[:, 1]])]
        quarter_indices = sorted_indices[:len(sorted_indices) // 4]

        return watermarked_fft[quarter_indices[:, 0], quarter_indices[:, 1]]
    
    @staticmethod
    def zigzag_scan(matrix):
        # Размеры матрицы
        rows, cols = matrix.shape
        
        # Результат зигзагообразной развертки
        result = []
        
        # Индексы для обхода матрицы
        i, j = 0, 0
        
        # Флаг для определения направления обхода
        up = True
        
        while i < rows and j < cols:
            result.append(matrix[i, j])
            
            # Движение вверх-вправо
            if up:
                if j == cols - 1:
                    # Дошли до правого края, переходим на следующую строку
                    i += 1
                    up = False
                elif i == 0:
                    # Дошли до верхнего края, переходим на следующий столбец
                    j += 1
                    up = False
                else:
                    # Продолжаем движение вверх-вправо
                    i -= 1
                    j += 1
            # Движение вниз-влево
            else:
                if i == rows - 1:
                    # Дошли до нижнего края, переходим на следующий столбец
                    j += 1
                    up = True
                elif j == 0:
                    # Дошли до левого края, переходим на следующую строку
                    i += 1
                    up = True
                else:
                    # Продолжаем движение вниз-влево
                    i += 1
                    j -= 1
        
        return result