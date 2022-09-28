#!/bin/bash

#Script to clear the Screenshot folder.

echo -e "Checking files in the Screenshot folder"

n=$(ls ~vmahdych/Pictures/Screenshots/ |wc -l)

if [[ $n -gt 0 ]]
then
	echo -e "\nThe following files are there:"
	ls -l ~vmahdych/Pictures/Screenshots/
	sleep 1
	echo -e "\nLet's remove them"
	rm -vf ~vmahdych/Pictures/Screenshots/*
else
	echo -e "\nNo files found"
fi

