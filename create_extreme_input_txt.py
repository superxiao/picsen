import fileinput
import random
import os
import webbrowser
import Image
import common
import random

f_train_in = open("train_shuffled.txt", "r")
f_test_in = open("test_shuffled.txt", "r")
train_lines = f_train_in.readlines()
test_lines = f_test_in.readlines()
f_train_out = open("input_txt/train_extreme.txt", "w")
f_test_out = open("input_txt/val_extreme.txt", "w")
print "Making train input:"
if(len(train_lines)!=38000):
	print "Problem!: train lines " + str(len(train_lines))

for line in train_lines:
	cells = line.split(" ")
	score = float(cells[2])
	good = int(cells[1])
	if((good == 1 and score < 6) or (good == 0 and score > 4.4) or good not in (1,0)):
		print "problem!: good " + str(good) + " score " + str(score);
	f_train_out.write(cells[0]+" "+cells[1]+"\n")
print "Make test input:"
if(len(test_lines)!=2000):
	print "Problem!: test lines " + str(len(test_lines))

for line in test_lines:
	cells = line.split(" ")
	score = float(cells[2])
	good = int(cells[1])
	if((good == 1 and score < 6) or (good == 0 and score > 4.4) or good not in (1,0)):
		print "problem!: good " + str(good) + " score " + str(score);
	f_test_out.write(cells[0]+" "+cells[1]+"\n")




