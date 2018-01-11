from PIL import ImageGrab
import time
from PIL import Image

if __name__ == '__main__':
    time.sleep(5)
    # grab fullscreen
    im = ImageGrab.grab()

    # save image file
    im.save('screenshot.png')

    # show image in a window
    im.show()
    print(im.format, im.size, im.mode)
