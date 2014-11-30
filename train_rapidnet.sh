#!/usr/bin/env sh

$HOME/caffe/build/tools/caffe.bin train --solver=rapidnet_solver.prototxt 2> rapidnet.log
