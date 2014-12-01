caffe_root = "$HOME/caffe/"
import sys
import io
import numpy as np
import datetime
sys.path.insert(0, caffe_root+'python')

import caffe


net = caffe.Classifier('caffe_mod_deploy.prototxt',
	'snapshots_flickr_iter_12000.caffemodel')
net.set_phase_test()
net.set_mode_gpu()
net.set_mean('data', np.load("ava_train_mean.npy"))
net.set_raw_scale('data', 255)
net.set_channel_swap('data', (2, 1, 0))

f_train = open("input_txt/train_extreme.txt", "r")
f_val = open("input_txt/val_extreme.txt", "r")
train_lines = f_train.readlines()
val_lines = f_val.readlines()
lines = train_lines + val_lines
i = 0
batch = []
results = []
batch_idx = 0

f_out = open("../predicted_scores.txt", "w")
for line in (train_lines + val_lines):
	cells = line.split(" ")
	fileName = cells[0]
	fileName = "../ava_resized_extreme/" + fileName
	isGood = int(cells[1])
	batch.append([fileName, isGood])
	i+= 1
	if (i >= 256):
		scores = net.predict([caffe.io.load_image(item[0]) for item in batch])
		print "First scores " + str(scores[0])
	
		print datetime.datetime.now()
		print "Processed batch: " + str(batch_idx) + " Image: " + str((batch_idx+1)*256)
		batch_idx += 1

		for item, score in zip(batch, scores):
			f_out.write(str(item[0]) + " "+str(item[1])+" " + str(score[0]) + " "+ str(score[1]) + "\n")
		i=0
		batch = []

 