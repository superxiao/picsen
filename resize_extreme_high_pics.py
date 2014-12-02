import os
import Image
import common
import shutil

HIGHT_RAITING_PERC = 0.1
LOW_RAITING_PERC = 0.1

def resize_and_save(imgpath):
	img = Image.open(imgpath)
    #resized = img.resize((256, 256), Image.ANTIALIAS)
	print "Resized image " + cells[1]
	img.save("../high_pics/"+cells[0]+"-"+cells[1]+".jpg")

high_list = common.get_high_list(HIGHT_RAITING_PERC)
low_list = common.get_low_list(LOW_RAITING_PERC)
i = 0
for high in reversed(high_list):
	i += 1
	print str(i) + ":"
	line = high[0]
	cells = line.split(" ")
	imgpath = "../ava/"+cells[0]+"-"+cells[1]+".jpg"
	if(os.path.exists(imgpath)):
		shutil.copyfile(imgpath, "../high_pics/"+cells[0]+"-"+cells[1]+".jpg")
		#resize_and_save(imgpath)
	else:
		print "Image " + cells[1] + " not found yaa! Downloading..."
		common.download_image(line)
		resize_and_save(imgpath)
	if (i > 2000):
		break;
