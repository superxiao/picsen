#!/usr/bin/env sh

~/caffe/build/tools/caffe.bin train -solver flickr_style_mod_solver.prototxt -weights finetune_flickr_style.caffemodel 2>&1 | tee -a flickr_style_mod.log