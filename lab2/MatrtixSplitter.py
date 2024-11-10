import numpy as np

class MatrixSplitter:
    @staticmethod
    def construct_matrix_from_its_fft_zones(zones: np.ndarray) -> np.ndarray:
        return np.sum(zones)
    
    @staticmethod
    def split_into_fft_zones_and_return(matrix: np.ndarray) -> dict:
        zones_dictionary = {
            "high": np.zeros(1),
            "medium": np.zeros(1),
            "low": np.zeros(1)
        }
        one_piece_height = matrix.shape[0] // 4
        one_piece_width = matrix.shape[1] // 4
        splitted_image = MatrixSplitter.split_into_pieces(matrix, one_piece_height)
        empty_piece = np.zeros((one_piece_height, one_piece_width))
        
        # low frequency zone construction
        low_first_row = np.concatenate((splitted_image[0], empty_piece, empty_piece, splitted_image[3]), axis=1)
        low_second_row = np.concatenate((empty_piece, empty_piece, empty_piece, empty_piece), axis=1)
        low_third_row = np.concatenate((empty_piece, empty_piece, empty_piece, empty_piece), axis=1)
        low_fourth_row = np.concatenate((splitted_image[12], empty_piece, empty_piece, splitted_image[15]), axis=1)
        zones_dictionary["low"] = np.concatenate((low_first_row, low_second_row, low_third_row, low_fourth_row), axis=0)
        
        # medium frequency zone construction
        medium_first_row = np.concatenate((empty_piece, splitted_image[1], splitted_image[2], empty_piece), axis=1)
        medium_second_row = np.concatenate((splitted_image[4], empty_piece, empty_piece, splitted_image[7]), axis=1)
        medium_third_row = np.concatenate((splitted_image[8], empty_piece, empty_piece, splitted_image[11]), axis=1)
        medium_fourth_row = np.concatenate((empty_piece, splitted_image[13], splitted_image[14], empty_piece), axis=1)
        zones_dictionary["medium"] = np.concatenate((medium_first_row, medium_second_row, medium_third_row, medium_fourth_row), axis=0)
        
        # high frequency zone construction
        high_first_row = np.concatenate((empty_piece, empty_piece, empty_piece, empty_piece), axis=1)
        high_second_row = np.concatenate((empty_piece, splitted_image[5], splitted_image[6], empty_piece), axis=1)
        high_third_row = np.concatenate((empty_piece, splitted_image[9], splitted_image[10], empty_piece), axis=1)
        high_fourth_row = np.concatenate((empty_piece, empty_piece, empty_piece, empty_piece), axis=1)
        zones_dictionary["high"] = np.concatenate((high_first_row, high_second_row, high_third_row, high_fourth_row), axis=0)
            
        return zones_dictionary
        
        
    @staticmethod
    def split_into_pieces(array, N):    
        A = []
        for v in np.vsplit(array, array.shape[0] // N):
            A.extend([*np.hsplit(v, array.shape[0] // N)])
        return np.array(A)