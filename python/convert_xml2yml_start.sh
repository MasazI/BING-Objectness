#!/bin/bash

if [ $# -ne 1 ]; then
		echo "[Usage]./convert_xml2yml.sh <full path of input directory>"
		exit 1
fi

input_directory=$1

count=1
for xmlfile in $(ls ${input_directory} | grep -e xml ); do
		python convert_xml2yml.py ${input_directory}"/"${xmlfile}
		echo "file number: " ${count}
		count=$(( count + 1 ))
done
