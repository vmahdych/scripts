#!/bin/bash

for f in /home/vmahdych/Pictures/Screenshots/*\ * 
do mv "$f" "${f// /_}" 
done
