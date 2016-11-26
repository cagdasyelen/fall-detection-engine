#!/usr/bin/env bash


#Labels are:
# 0 : no fall
# 1 : first level fall
# 2 : second level fall
# 3 : third levle fall

#increasing number shows the increase in severity level




LABEL=$1

FILE=/tmp/data.csv


sed -i 1,3d $FILE

cd ~/fall-detection-engine/raw-data 
numberOfFiles=$(ls -l | wc -l)

echo "$(awk '{printf "%d,%s\n", NR, $0}' < $FILE)" > ~/fall-detection-engine/raw-data/"sample"$numberOfFiles"_fall"$LABEL".csv"
rm -rf /tmp/data.csv

