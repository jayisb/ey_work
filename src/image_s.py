import cv2
import pyautogui
import time
from PIL import Image
import datetime
import shutil
import os

print "hi"

input_directory = "/home/jay/Documents/jay_data/suppliers1/"

# Output directory for storing enhanced images
output_directory_correct = "/home/jay/Documents/jay_data/suppliers1_correct/"

output_directory_incorrect = "/home/jay/Documents/jay_data/customers1_incorrect/"

if not os.path.exists(output_directory_correct):
    os.makedirs(output_directory_correct)

if not os.path.exists(output_directory_incorrect):
    os.makedirs(output_directory_incorrect)

count = 0
for filename in os.listdir(input_directory):
	if filename.endswith(".png"):
		count = count + 1
		print (os.path.join(input_directory, filename))
		input_image = cv2.imread(os.path.join(input_directory, filename))
		ticker_img = input_image[111:181, 1350:1950] 
		cv2.imwrite("/home/jay/Desktop/trt.png", ticker_img)
		print count
		if pyautogui.locate("/home/jay/Desktop/Capture.PNG", "/home/jay/Desktop/trt.png"):
			shutil.move(input_directory+filename, output_directory_correct)
		else:
			shutil.move(input_directory+filename, output_directory_incorrect)