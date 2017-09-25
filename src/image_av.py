import cv2
import pyautogui
import time
from PIL import Image
import datetime
import shutil
import os

print "hi"

input_directory = "/home/jay/Documents/jay_data/suppliers1_correct/"

# Output directory for storing enhanced images
output_directory_correct = "/home/jay/Documents/jay_data/suppliers1_correct_available/"

output_directory_incorrect = "/home/jay/Documents/jay_data/suppliers1_correct_unavailable/"

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
		ticker_img = input_image[415:435, 10:35] 
		cv2.imwrite("/home/jay/Desktop/avail.png", ticker_img)
		print count
		if pyautogui.locate("/home/jay/Desktop/avail.png", "/home/jay/Desktop/availdata.png"):
			shutil.move(input_directory+filename, output_directory_incorrect)
		else:
			shutil.move(input_directory+filename, output_directory_correct)