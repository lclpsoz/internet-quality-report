#!/bin/bash

sleep 15

ot=/home/pi/out.txt

now () {
	ret=`date +"%s %Z"`
}

echo START >> $ot

# echo "`date` start" > $ot
while true; do
		if ping -c 1 google.com > /dev/null
		then
			now
			echo "$ret ok"
			echo "$ret ok" >> $ot
		else
			now
			echo "$ret fail"
			echo "$ret fail" >> $ot
		fi
		sleep 5
done

