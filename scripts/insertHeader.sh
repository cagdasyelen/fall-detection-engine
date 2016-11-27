#!/usr/bin/env bash


DIR=$1

for f in "$DIR"/*.csv ; do
	if [[ "$(cat $f)" == *"index"* ]]; then
		echo "includes"
	else
		perl -lpe 'BEGIN{print "index,ax,ay,az,gx,gy,gz"}' "$f" > foo;
		mv foo "$f"
	fi

done


