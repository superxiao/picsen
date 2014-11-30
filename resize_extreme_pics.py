import os
import Image
import common


f_train = open("input_txt/train_extreme.txt")
f_test = open("input_txt/val_extreme.txt")
train_lines = f_train.readlines()
test_lines = f_test.readlines()

def resize_and_save(imgpath):
	resized = "../ava_resized_extreme/"+cells[0]
	if(os.path.exists(resized)):
		print "Already resized! " + cells[0]
		return;
	img = Image.open(imgpath)
	resized = img.resize((256, 256), Image.ANTIALIAS)
	print "Resized image " + cells[0]
	resized.save("../ava_resized_extreme/"+cells[0])

i = 0
for line in train_lines:
	i += 1
	print str(i) + ":"
	cells = line.split(" ")
	imgpath = "../ava/"+cells[0]
	if(os.path.exists(imgpath)):
		resize_and_save(imgpath)
	else:
		print "Image " + cells[0] + " not found yaa! Downloading..."
		common.download_image_by_filename(cells[0])
		resize_and_save(imgpath)

for line in test_lines:
	i += 1
	print str(i) + ":"
	cells = line.split(" ")
	imgpath = "../ava/"+cells[0]
	if(os.path.exists(imgpath)):
		resize_and_save(imgpath)
	else:
		print "Image " + cells[0] + " not found yaa! Downloading..."
		common.download_image_by_filename(cells[0])
		resize_and_save(imgpath)