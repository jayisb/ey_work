from PIL import Image
import pyscreenshot as ImageGrab
import datetime
import time
import os

if __name__ == "__main__":
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    file_location = os.path.join('C:\\Users\\31049\\Desktop\\03-05-2017', file_name)
    print file_location
    im.save(file_location)