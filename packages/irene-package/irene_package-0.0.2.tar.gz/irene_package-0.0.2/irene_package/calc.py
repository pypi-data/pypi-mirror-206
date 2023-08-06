import cv2
def add(x, y):
    return x + y

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def image(self, img:str, width = 800, height = 600):
        try:
            while True:
                frame = cv2.imread(img)
                cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("Image", width, height)
                cv2.imshow("Image", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except cv2.error:
            pass

d = Display()
d.image(img=r"C:\Users\100050\OneDrive - AIF Rwanda\Irene Nsengumukiza\Downloads\animations\3dgraphics.png")