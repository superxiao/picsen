import fileinput
import urllib
import os
import bs4
import common

HIGHT_RAITING_PERC = 0.1
LOW_RAITING_PERC = 0.1
high_list = common.get_high_list(HIGHT_RAITING_PERC)
low_list = common.get_low_list(LOW_RAITING_PERC)
print "Will download " + str(len(high_list)) + " photos"
i = 0
for high in high_list:
	print str(i) + ":"
	i+=1
	common.download_image(high[0])
print "Will download " + str(len(low_list)) + " photos"

i = 0
for low in low_list:
	print str(i) + ":"
	i+=1
	common.download_image(low[0])
