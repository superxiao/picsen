import fileinput
import random
import os
import webbrowser
import Image
import common
import random


TRAIN_NUM_HIGH = 19000
TEST_NUM_HIGH = 1000
TRAIN_NUM_LOW = 19000
TEST_NUM_LOW = 1000

f_high_in = open("high_shuffled.txt", "r")
f_low_in = open("low_shuffled.txt", "r")
high_lines = f_high_in.readlines()
low_lines = f_low_in.readlines()
f_train_out = open("train_shuffled.txt", "w")
f_test_out = open("test_shuffled.txt", "w")


train_list = []
test_list = []

i = 0
for high_line, low_line in zip(high_lines, low_lines):
	print str(i) + ":"
	if(i < TRAIN_NUM_HIGH):
		train_list.append(high_line)
		train_list.append(low_line)
		print high_line
		print "Two scores in this train: \n" +high_line.split(" ")[2]+ low_line.split(" ")[2]
	if(i >= TRAIN_NUM_HIGH and i < TRAIN_NUM_HIGH+TRAIN_NUM_LOW):
		test_list.append(high_line)
		test_list.append(low_line)
		print "Two scores in this test: \n" + high_line.split(" ")[2]+ low_line.split(" ")[2]
	i += 1
print "Tow lists are " + str(len(train_list)) +", " +str(len(test_list))+" long"

random.shuffle(train_list)
random.shuffle(test_list)

for train_line in train_list:
	f_train_out.write(train_line)
for test_line in test_list:
	f_test_out.write(test_line)




