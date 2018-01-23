#!/bin/bash

# This script needs to be run from its own directory, so cd into it
fullpath=`realpath $0`
dirname=`dirname $fullpath`
cd $dirname

if [ ! -e "files.txt" ]; then
	echo "File 'files.txt' does not exist."
	exit 1
fi

for file in `cat files.txt`; do
	
	if [ -e $file ]; then
		diff -u $file ../$file | patch
	fi
done
#cp `sed 's!^!'"$HOME"'/!' < files.txt` .
