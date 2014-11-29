# Create the text files containing training and test image
# names and their classes.
import fileinput
import urllib
import os
import bs4

def get_avg(cells):
	sum = 0;
	count = 0;
	for i in range(2, 12):
		sum += (i - 1) * float(cells[i])
		count += float(cells[i])
	avg = sum / count
	return avg

def get_high_list(percent):
	f_in = open("AVA_dataset/AVA.txt");
	lines = f_in.readlines();
	processed_lines = [0] * len(lines)
	i = 0
	for line in lines:
		cells = line.split()
		avg = get_avg(cells)
		processed_lines[i] = [line, avg]
		i += 1
	processed_lines.sort(key=lambda x: x[1])
	return processed_lines[-int(percent*len(lines)):]

def get_low_list(percent):
	f_in = open("AVA_dataset/AVA.txt");
	lines = f_in.readlines();
	processed_lines = [0] * len(lines)
	i = 0
	for line in lines:
		cells = line.split()
		avg = get_avg(cells)
		processed_lines[i] = [line, avg]
		i += 1
	processed_lines.sort(key=lambda x: x[1])
	return processed_lines[:int(percent*len(lines))]

def download_image(line):

	cells = line.split(" ")
	if(os.path.exists("../ava/"+cells[0]+"-"+cells[1]+".jpg")):
		print cells[1] + " already downloaded"
		return
	id = cells[1]
	url = "http://www.dpchallenge.com/image.php?IMAGE_ID="+id
	code = urllib.urlopen(url).read()
	soup = bs4.BeautifulSoup(code)
	tbs = soup.findAll('td')
	for tb in tbs:
		if tb.has_key('class') and tb['class'][0] == "page-image":
			imgs = tb.find_all('img')
			img = imgs[1]
			src = img.get('src')
			print "Current src is " + src
			urllib.urlretrieve(src, "../ava/"+cells[0]+"-"+id+'.jpg')
			print cells[0]+": Photo " + id + " downloaded" 
			
