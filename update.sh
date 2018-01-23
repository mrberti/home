#!/bin/bash

# This script needs to be run from its own directory, so cd into it
fullpath=`realpath $0`
dirname=`dirname $fullpath`
cd $dirname

file_to_update=$1
file_to_read=$2

if [ ! -e $file_to_update ] || [ -z $1 ]; then
	echo "File '$file_to_update' does not exist."
	echo "Usage: $0 file_to_update [file_to_read]"
	echo "	When file_to_read is empty, using ../file_to_update"
	exit 1
fi

[ -z $file_to_read ] && file_to_read="../$file_to_update"

echo $file_to_read

echo "patching $file_to_update, source file: $file_to_read"
diff -u $file_to_update $file_to_read | patch
