import cv2
import numpy as np

class Image:
    name: str
    data: np.ndarray = np.zeros(1)
    shape: tuple
    color_scheme: int
    
    def __init__(self,
                 filepath: str = '',
                 data: np.ndarray = np.zeros(1),
                 name: str = ''):
        if (filepath is None) and (data is None):
            raise RuntimeError("Neither the file path nor the file data were provided")
        
        self.name = name
        self.data = data
        
        if filepath is not None:
            self.upload_image(filepath)    
            self.name = filepath
        
        try:
            self.shape = self.data.shape
        except:
            pass
        
    def upload_image(self, filepath : str, color_scheme: int = cv2.IMREAD_COLOR) -> None:
        self.data = cv2.imread(filepath)
        self.shape = self.data.shape
        
    def show(self) -> None:
        window_name = self.name
        cv2.imshow(window_name, self.data)
        cv2.waitKey(0)
        
    def get_rgb(self) -> tuple:
        B, G, R = cv2.split(self.data)

        blue_channel_image = Image(data=B)
        green_channel_image = Image(data=G)
        red_channel_image = Image(data=R)

        return blue_channel_image, green_channel_image, red_channel_image
    
    def get_yCrCb(self) -> tuple:
        yCrCb_color = cv2.cvtColor(self.data, cv2.COLOR_BGR2YCrCb)
        Y, Cr, Cb = cv2.split(yCrCb_color)
        
        y_channel_image = Image(data=Y)
        cr_channel_mage = Image(data=Cr)
        cb_channel_image = Image(data=Cb)
        
        return y_channel_image, cr_channel_mage, cb_channel_image