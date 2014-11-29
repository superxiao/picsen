import fileinput
import random

# Create the text files containing training and test image
# names and their classes.

TRAIN_NUM = 10000
VAL_NUM = 1000

# The average score is 5.39. We take 5.5 as the threshold
GOOD_THRES = 5.5

def get_avg(split_line):
	print line 
	print cells
	sum = 0;
	count = 0;
	for i in range(2, 12):
		sum += (i - 1) * float(split_line[i])
		count += float(split_line[i])
	avg = sum / count
	return avg

f_train = open("input_txt/train_tmp.txt", "w")
f_test = open("input_txt/val_tmp.txt", "w")

f_in = open("AVA_dataset/AVA.txt");
lines = f_in.readlines();
lines = lines[:30000]
random.shuffle(lines)
print "Lines has "+str(len(lines))


for line in lines[:TRAIN_NUM]:
	cells = line.split()
	idx = int(cells[0])
	avg = get_avg(cells)
	isGood = 0;
	if(avg >= GOOD_THRES):
		isGood = 1;
	f_train.write(cells[0]+"-"+cells[1]+".jpg");
	f_train.write(" "+str(isGood)+"\n");

for line in lines[TRAIN_NUM:TRAIN_NUM+VAL_NUM]:	
	cells = line.split()
	idx = int(cells[0])
	avg = get_avg(cells)
	isGood = 0;
	if(avg >= GOOD_THRES):
		isGood = 1;
	f_test.write(cells[0]+"-"+cells[1]+".jpg");
	f_test.write(" "+str(isGood)+"\n");


