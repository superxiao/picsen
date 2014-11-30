#!/usr/bin/env sh
# Create the ava lmdb inputs

# This folder should contain the input txt files (containing
# image path, classification)
DATA=input_txt

# Set this to the built tools folder of caffe
TOOLS=$HOME/caffe/build/tools

# set the path to the ava train + val data dirs
TRAIN_DATA_ROOT=../ava_resized_extreme/
VAL_DATA_ROOT=../ava_resized_extreme/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."



echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset.bin \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    $VAL_DATA_ROOT \
    $DATA/val_extreme.txt \
    ava_val_lmdb

echo "Done."
