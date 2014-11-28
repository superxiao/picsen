import fileinput
import urllib
import os
import bs4

for line in fileinput.input("AVA.txt"):
	cells = line.split(" ")
	if(int(cells[0])>30000):
		break
	if(os.path.exists("../../ava/"+cells[0]+"-"+cells[1]+".jpg")):
		continue

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
			urllib.urlretrieve(src, "../../ava/"+cells[0]+"-"+id+'.jpg')
			print cells[0]+": Photo " + id + " downloaded" 
			break
