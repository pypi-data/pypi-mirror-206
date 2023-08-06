import cv2
def add(x, y):
    return x + y

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def image(self, img:str, width = 800, height = 600):
        try:
            frame = cv2.imread(img)
            cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Image", width, height)
            cv2.imshow("Image", frame)
        except cv2.error:
            pass