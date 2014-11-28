import fileinput
import matplotlib.pyplot as plt 

tags = [0] * 66
count = 0;
for line in fileinput.input("AVA.txt"):
	if(count > 30000):
		break;
	cells = line.split()
	tag1 = int(cells[12])
	tag2 = int(cells[13])
	if(tag1 == 66 or tag2 == 66):
		print "Get one 65!"
	if(tag1 != 0):
		tags[int(cells[12])-1] += 1;
	if(tag2 != 0):
		tags[int(cells[13])-1] += 1;
	count+=1
plt.bar(range(0, 66), tags)
plt.show()
print tags
