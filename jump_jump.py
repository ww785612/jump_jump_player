from PIL import ImageGrab, Image, ImageChops
import time
from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt

def capture():
    # grab fullscreen
    im = ImageGrab.grab()

    # show image in a window
    cropedImg = trim(im)
    if cropedImg:
        return cropedImg

# get rid of black borders
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100) # Adds two images, dividing the result by scale and adding the offset.
    bbox = diff.getbbox() # Calculates the bounding box of the non-zero regions in the image.
    if bbox:
        return im.crop(bbox) # argument is the crop rectangle, as a (left, upper, right, lower)-tuple.

def removeShadow(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)

if __name__ == '__main__':

    time.sleep(5)
    im = capture()
    if im:
        im.save('screenshot.png')
    #     im.show()

    # im = Image.open("screenshot.png")
    # print(im.format, im.size)
    # shadowPixel = im.getpixel((10,870))
    # brightPixel = im.getpixel((10,970))
    # print(brightPixel[0] - shadowPixel[0], brightPixel[1] - shadowPixel[1], brightPixel[2] - shadowPixel[2])

    # image is always 700x1440 if croped properly
    # imageArr = np.zeros((700, 1440))
    # for row in range(0,700):
    #     for col in range(0,1440):
    #         pixel = im.getpixel((row,col))
    #         # for channel in range(0,3):
    #         imageArr[row][col] = pixel[0]
    # np.savetxt("foo.csv", imageArr, delimiter=",")
    # # plt.imshow(imageArr)
    # # plt.show()

    # opencv store images in BGR format instead of RGB
    imcv = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
    edges = cv2.Canny(image=imcv,threshold1=20,threshold2=45)

    plt.subplot(121), plt.imshow(imcv)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges)
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    print(im.format, im.size)

