import fileinput
import random
import os
import webbrowser
import Image
import common



# Create the text files containing training and test image
# names and their classes.
HIGHT_RAITING_PERC = 0.1
LOW_RAITING_PERC = 0.1

VAL_NUM = 1000

def get_avg(cells):
	sum = 0;
	count = 0;
	for i in range(2, 12):
		sum += (i - 1) * float(cells[i])
		count += float(cells[i])
	avg = sum / count
	return avg

f_train = open("input_txt/train.txt", "w")
f_test = open("input_txt/val.txt", "w")

f_in = open("AVA_dataset/AVA.txt");
lines = f_in.readlines();
lines = lines[:30000]

processed_lines = [0] * len(lines)

i = 0
for line in lines:
	print line
	cells = line.split()
	avg = get_avg(cells)
	processed_lines[i] = [cells, avg]
	i += 1

processed_lines.sort(key=lambda x: x[1])
count = 0
for line in processed_lines[:int(LOW_RAITING_PERC*len(lines))]:

	cells = line[0]

	if(count < 5):
		#os.system("open ../ava/"+cells[0]+"-"+cells[1]+".jpg")
		count += 1
	idx = int(cells[0])
	avg = get_avg(cells)
	isGood = 1
	f_train.write(cells[0]+"-"+cells[1]+".jpg");
	f_train.write(" "+str(isGood)+"\n");

j = HIGHT_RAITING_PERC*len(lines)
for line in processed_lines[-int(HIGHT_RAITING_PERC*len(lines)):]:	
	j-=1
	cells = line[0]
	if(j < 10):
		print "open ../ava/"+cells[0]+"-"+cells[1]+".jpg"
		image = Image.open("../ava/"+cells[0]+"-"+cells[1]+".jpg")
		image.show()
	idx = int(cells[0])
	avg = get_avg(cells)
	isGood = 0;
	f_test.write(cells[0]+"-"+cells[1]+".jpg");
	f_test.write(" "+str(isGood)+"\n");
print int(HIGHT_RAITING_PERC*len(lines))

