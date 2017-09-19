import cv2
import numpy as np

# def image_enhancement (original_image):
#     kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
#                                  [-1, 2, 2, 2, -1],
#                                  [-1, 2, 8, 2, -1],
#                                  [-1, 2, 2, 2, -1],
#                                  [-1, -1, -1, -1, -1]]) / 8.0
#     large_image = cv2.resize(original_image, (0, 0), fx=2.5, fy=2.5, interpolation = cv2.INTER_LANCZOS4)
#     output_image = cv2.filter2D(large_image, -1, kernel_sharpen_3)
#     return output_image

# load the image and show it
image = cv2.imread("/home/jay/Desktop/03-07-2017/customers/sample_20170702-133617.png")


#cv2.imshow("original", image)
#ticker_img = image[122:1070, 18:135] # Crop from x, y, w, h -> 100, 200, 300, 400
ticker_img = image[382:989, 45:665]
cv2.imshow("ticker1", ticker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# country_img = image[122:1070, 136:180]
# market_img = image[122:1070, 181:237]
# sales_img = image[122:1070, 238:602]
# revenue_img = image[122:1070, 603:967]
# relationship_img = image[122:1070, 969:1342]
# account_img = image[122:1070, 1343:1404]
# cost_img = image[122:1070, 1405:1763]
# source_img = image[122:1070, 1764:1841]
# date_img = image[122:1070, 1842:1916]
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
#cv2.imwrite('/home/jay/Downloads/ticker.png', ticker_img)
#cv2.imwrite('/home/jay/Downloads/ticker.png', country_img)

#cv2.imshow("ticker", ticker_img)
#cv2.imshow("country", country_img)
#cv2.imshow("market", market_img)
#cv2.imshow("sales", sales_img)
#cv2.imshow("revenue", revenue_img)
#cv2.imshow("relationship", relationship_img)
#cv2.imshow("account", account_img)
#cv2.imshow("cost", cost_img)
#cv2.imshow("source", source_img)
#cv2.imshow("date", date_img)

#small = cv2.resize(image, (0,0), fx=2.5, fy=2.5)
#cv2.imshow("big", small)
#cv2.waitKey(0)



#img = small
#cv2.imshow('Original', img)

# generating the kernels
# kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
# kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
#                              [-1,2,2,2,-1],
#                              [-1,2,8,2,-1],
#                              [-1,2,2,2,-1],
#                              [-1,-1,-1,-1,-1]]) / 8.0

# applying different kernels to the input image
#output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
#output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
#output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

#cv2.imshow('Sharpening', output_1)
#cv2.imshow('Excessive Sharpening', output_2)
#cv2.imshow('Edge Enhancement', output_3)

#cv2.imwrite('/home/jay/Downloads/sharpening.png', output_1)
#cv2.imwrite('/home/jay/Downloads/excessive.png', output_2)
#cv2.imwrite('/home/jay/Downloads/enhancement.png', output_3)
# ticker_enh = image_enhancement(ticker_img)
# cv2.imshow("ticker", ticker_enh)
# cv2.imwrite(location, ticker_enh)
# cv2.waitKey(0)
#cv2.destroyAllWindows()

