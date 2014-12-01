import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

caffe_root = "$HOME/caffe/"
import sys
sys.path.insert(0, caffe_root+'python')

import caffe

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

net = caffe.Classifier('caffe_mod_deploy.prototxt',
	'snapshots_flickr_iter_8500.caffemodel')
net.set_phase_test()
net.set_mode_cpu()
net.set_mean('data', np.load("ava_train_mean.npy"))
net.set_raw_scale('data', 255)
net.set_channel_swap('data', (2, 1, 0))

scores = net.predict([caffe.io.load_image('bird.jpg')])

[(k, v.data.shape) for k, v in net.blobs.items()]
[(k, v[0].data.shape) for k, v in net.params.items()]



# take an array of shape (n, height, width) or (n, height, width, channels)
#  and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)
def vis_square(data, padsize=1, padval=0):
    data -= data.min()
    data /= data.max()
    
    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = ((0, n ** 2 - data.shape[0]), (0, padsize), (0, padsize)) + ((0, 0),) * (data.ndim - 3)
    data = np.pad(data, padding, mode='constant', constant_values=(padval, padval))
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    plot(data)
    draw()




