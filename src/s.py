from PIL import Image
import pyscreenshot as ImageGrab
import time

if __name__ == "__main__":
    im=ImageGrab.grab()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print timestr
    file_name = "sample_" + timestr + ".png"
    im.save(file_name)