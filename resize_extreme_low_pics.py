import os
import Image
import common

LOW_RAITING_PERC = 0.1

def resize_and_save(imgpath):
	img = Image.open(imgpath)
	resized = img.resize((256, 256), Image.ANTIALIAS)
	print "Resized image " + cells[1]
	resized.save("../ava_resized_extreme/"+cells[0]+"-"+cells[1]+".jpg")

low_list = common.get_low_list(LOW_RAITING_PERC)
i = 0
for low in low_list:
	i += 1
	print str(i) + ":"
	line = low[0]
	cells = line.split(" ")
	imgpath = "../ava/"+cells[0]+"-"+cells[1]+".jpg"
	if(os.path.exists(imgpath)):
		resize_and_save(imgpath)
	else:
		print "Image " + cells[1] + " not found yaa! Downloading..."
		common.download_image(line)
		resize_and_save(imgpath)