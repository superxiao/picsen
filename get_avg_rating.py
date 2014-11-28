import fileinput
import matplotlib.pyplot as plt 

# Compute the average rating of AVA
tags = [0] * 66
total_count = 0;
total_avg = 0;
for line in fileinput.input("../../AVA_dataset/AVA.txt"):
	if(total_count >= 30000):
		break;
	cells = line.split()
	sum = 0;
	count = 0;
	for i in range(2, 12):
		sum += (i - 1) * float(cells[i])
		count += float(cells[i])
	avg = sum / count;
	#print "This average is " + str(avg);
	total_avg += avg;
	total_count += 1

print "Total average is " + str(total_avg/total_count)

# Result is 5.3918171898. We take 5.5 as the threshold