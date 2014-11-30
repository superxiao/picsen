import fileinput
import random
import os
import webbrowser
import Image
import common
import random


# Create the text files containing training and test image
# names and their classes.
HIGHT_RAITING_PERC = 0.1
LOW_RAITING_PERC = 0.1

TRAIN_NUM_HIGH = 19000
TEST_NUM_HIGH = 1000
TRAIN_NUM_LOW = 19000
TEST_NUM_LOW = 1000

high_list = common.get_high_list(HIGHT_RAITING_PERC)
low_list = common.get_low_list(LOW_RAITING_PERC)
high_list = high_list[-20000:]
low_list = low_list[:20000]

print "Hight list is " + str(len(high_list)) + " long, low list is " + str(len(low_list))

f_low = open("low_list.txt", "w")
f_high = open("high_list.txt", "w")
f_high_shuffled = open("high_shuffled.txt", "w")
f_low_shuffled = open("low_shuffled.txt", "w")
for high in high_list:
	cells = high[0].split(" ")
	idx = int(cells[0])
	isGood = 1
	f_high.write(cells[0]+"-"+cells[1]+".jpg");
	print cells
	f_high.write(" "+str(isGood) + " "+ str(common.get_avg(cells)) +"\n");

for low in low_list:
	cells = low[0].split(" ")
	idx = int(cells[0])
	isGood = 0
	f_low.write(cells[0]+"-"+cells[1]+".jpg");
	f_low.write(" "+str(isGood)+ " " + str(common.get_avg(cells)) +"\n");

random.shuffle(high_list)
random.shuffle(low_list)

for high in high_list:
	cells = high[0].split(" ")
	idx = int(cells[0])
	isGood = 1
	f_high_shuffled.write(cells[0]+"-"+cells[1]+".jpg");
	print cells
	f_high_shuffled.write(" "+str(isGood) + " "+ str(common.get_avg(cells)) +"\n");

for low in low_list:
	cells = low[0].split(" ")
	idx = int(cells[0])
	isGood = 0
	f_low_shuffled.write(cells[0]+"-"+cells[1]+".jpg");
	f_low_shuffled.write(" "+str(isGood)+ " " + str(common.get_avg(cells)) +"\n");

