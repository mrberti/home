#!/bin/bash
fullpath=`realpath $0`
dirname=`dirname $fullpath`
cd $dirname
cp `sed 's!^!'"$HOME"'/!' < files.txt` .
