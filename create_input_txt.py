import fileinput

# Create the text files containing training and test image
# names and their classes.

TRAIN_START = 1
TRAIN_END = 100

TEST_START = 301
TEST_END = 400

# The average score is 5.39. We take 5.5 as the threshold
GOOD_THRES = 5.5

def get_avg(line):
	sum = 0;
	count = 0;
	for i in range(2, 12):
		sum += (i - 1) * float(cells[i])
		count += float(cells[i])
	avg = sum / count
	return avg

f_train = open("input_txt/train.txt", "w")
f_test = open("input_txt/val.txt", "w")

for line in fileinput.input("AVA_dataset/AVA.txt"):
	cells = line.split()
	idx = int(cells[0])
	
	# The current train range
	if(idx >= TRAIN_START and idx <= TRAIN_END):
		avg = get_avg(line)
		isGood = 0;
		if(avg >= GOOD_THRES):
			isGood = 1;
		f_train.write(cells[0]+"-"+cells[1]+".jpg");
		f_train.write(" "+str(isGood)+"\n");

	if(idx >= TEST_START and idx <= TEST_END):
		avg = get_avg(line)
		isGood = 0;
		if(avg >= 5.5):
			isGood = 1;
		f_test.write(cells[0]+"-"+cells[1]+".jpg");
		f_test.write(" "+str(isGood)+"\n");


