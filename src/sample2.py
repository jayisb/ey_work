import cv2
import numpy as np

def image_enhancement (original_image):
    kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, 2, 8, 2, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, -1, -1, -1, -1]]) / 8.0
    large_image = cv2.resize(original_image, (0, 0), fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
    output_image = cv2.filter2D(large_image, -1, kernel_sharpen_3)
    return output_image

# For B/W
# image = cv2.imread("/home/jay/Pictures/bloomberg/sample_20170428-120928.png", 0)
image = cv2.imread("/home/jay/Pictures/bloomberg/sample_20170428-120928.png")
location = '/home/jay/Pictures/bloomberg/t1.png'

cv2.imshow("original", image)
ticker_img = image[382:989, 45:321] # Crop from x, y, w, h -> 100, 200, 300, 400
ticker_img = image_enhancement(ticker_img)

# For B/W
#(thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#For writing
cv2.imwrite(location, ticker_img)
#cv2.imshow("ticker", ticker_img)
cv2.waitKey(0)
#cv2.destroyAllWindows()

