#!/bin/bash
#ls -A | sed -En '/.git$/n;s/(^\.[^\.]+)/cp \1 ~\/\1/p'
fullpath=`realpath $0`
dirname=`dirname $fullpath`
cd $dirname
cp `cat files.txt` ~/
