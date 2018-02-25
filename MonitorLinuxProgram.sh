#!/bin/sh
if [ $# -ne 1 ]; then
	echo "Usage: `basename $0` <full path of a program> "
	echo "Example :: sh `basename $0` /usr/bin/bgpd"
	exit
fi
program=$1

ls -lrt $program 2>/dev/null

if [ $? -ne 0 ]; then
	echo "Program: $program doesnt exist!!"
	exit

logFile=$(basename ${program})
echo "Running CPU/Memory Capture Stats for:: ${program} . Stats are logged to  /tmp/${logFile}.log"
headers=$(ps -p $(lsof  $program  | awk 'NR==2{print $2}') -o pmem,pcpu,vsize,pid | head -1)
echo $headers,Date >/tmp/${logFile}.log
while [ 1 ]
do
	stats=$(ps -p $(lsof  $program | awk 'NR==2{print $2}') -o pmem,pcpu,vsize,pid | tail -1)
	echo $stats, `date +%Y/%m/%d-%H:%M` >> /tmp/${logFile}.log
	sleep 60
done
