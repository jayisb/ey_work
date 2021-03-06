import cv2
import numpy as np
import os
import time

# Image enhancement for improving OCR accuracy
def image_enhancement(original_image):
    kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, 2, 8, 2, -1],
                                 [-1, 2, 2, 2, -1],
                                 [-1, -1, -1, -1, -1]]) / 8.0
    large_image = cv2.resize(original_image, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    output_image = cv2.filter2D(large_image, -1, kernel_sharpen_3)
    return output_image

# For B/W
# image = cv2.imread("/home/jay/Pictures/bloomberg/sample_20170428-120928.png", 0)

# Input directory containing bloomberg screenshots
input_directory = "/home/jay/Desktop/china_sc/suppliers_17/"

# Output directory for storing enhanced images
output_directory = "/home/jay/Desktop/china_sc_tickers/suppliers_17/"

# Creates output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith(".png"):
        print(os.path.join(input_directory, filename))
        input_image = cv2.imread(os.path.join(input_directory, filename))
        #cv2.imshow(input_image)
        # Cropping the supplier / customer column
        ticker_img = input_image[382:989, 45:665]  # Crop from x, y, w, h -> 100, 200, 300, 400
        # Enhancing the supplier / customer column 
        ticker_img = image_enhancement(ticker_img)
        time_str = time.strftime("%Y%m%d-%H%M%S")
        file_name = "ticker_" + filename
        location = os.path.join(output_directory, file_name)
        # Saving the enhanced image
        cv2.imwrite(location, ticker_img)


# For B/W
# (thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
