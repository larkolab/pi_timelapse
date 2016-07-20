#!/bin/bash

if [ -z "$1" ]; then 
    echo usage: $0 SLEEP_SEC
    exit
fi

# Check if USB drive is mounted
mount | grep -v grep | grep " /media/usb " > /dev/null
result=$?
if [ "${result}" -ne "0" ] ; then
    echo "`date`: USB drive is not mounted"
    exit
fi

# Check if program is already running
ps -ef | grep -v grep | grep "timelapse.py" > /dev/null
result=$?
if [ "${result}" -eq "0" ] ; then
    echo "`date`: timelapse.py is already running"
    exit
fi

# start timelpase
/home/pi/pi_timelapse/timelapse.py $1 /media/usb/
