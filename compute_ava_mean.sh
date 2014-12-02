#!/usr/bin/env sh
# Compute the mean image from the imagenet training leveldb
# N.B. this is available in data/ilsvrc12
$HOME/caffe/build/tools/compute_image_mean.bin \
ava_train_lmdb ava_train_mean.binaryproto lmdb

$HOME/caffe/build/tools/compute_image_mean.bin \
ava_val_lmdb ava_val_mean.binaryproto lmdb

echo "Done."
