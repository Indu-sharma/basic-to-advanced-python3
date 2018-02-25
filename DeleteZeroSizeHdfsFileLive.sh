#!/bin/bash
if [ $# -ne 2 ]; then
	echo "Usage : `basename $0` <start epoch to delete netflow> <netflow base path>"
	echo "Example: ./`basename $0` 1489053600  /data/collector/*/"
exit
fi
epoch_current=$(date -d "`date`" +%s)
epoch=$1
basepath=$2
while [ 1 ]
do
	diff=`expr ${epoch_current} - ${epoch}` 
	if [ $diff  -lt  5400 ] ; then
		echo "Sleeping till reaching live::"
		sleep 5400
	fi
	dir=`date -d@$epoch +%Y/%m/%d/%H`
	isDeleted=0
	echo $dir
	hadoop fs -ls ${basepath}${dir}/*/br.[0-9][0-9]*.[0-9]* | awk '$5==0{print $NF}' > /data/all_files
	for i in `cat /data/all_files`
	do	
		
		#echo "Inside for Loop"
		hadoop fs -test -f $i
		notFile=$?
		hadoop fs -test -z $i
		notZero=$?
		if  [ ${notFile}  -eq 0 ]  && [ ${notZero} -eq 0 ]
		then
			isDeleted=1
			echo "Removing $i"
			hadoop fs -rm  $i
		fi
	done
	epoch_current=$(date -d "`date`" +%s)
	epoch=`expr $epoch + 3600`
	if [ $isDeleted -eq 0 ]; then
		echo "None of the file is deleted from netflow path : ${basepath}${dir}" 
	fi
done
