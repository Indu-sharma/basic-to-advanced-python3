probe_name=$(basename $0 .${0##*.})
PID_list=`python PID_extracter.py $probe_name`


while [ 1 ]
do
if [ ! -z $PID_list ]
then

break 1

PID_list=`python PID_extracter.py $probe_name`

fi
echo "Sleeping till Any Job process is available"

sleep 60 

done

PID_list=`echo $PID_list | tr ',' '  '`

echo "PID_list", $PID_list

rm -rf application_*_Stats.csv

> /tmp/job_pid_app

for pid in $PID_list
do

app=`cat /proc/$pid/cmdline | grep -Eiao 'application_[0-9_]+'|sort | uniq`
jobname=`yarn application -list | grep -ia $app| awk '{print $2}'`

echo "$pid,$app,$jobname" >> /tmp/job_pid_app

done

## Wait for the process to Finish 
	for i in  $PID_list
	do

		while [ -e /proc/$i ]
		do
    			sleep 10
		done
	done
## All The Processes are Over




for i in `cat /tmp/job_pid_app`
do

pid=`echo $i | cut -d',' -f1`
app=`echo $i | cut -d',' -f2`
jobname=`echo $i | cut -d',' -f3`

if [ ! -f ${app}_Stats.csv ];
then

    stg=`hadoop fs -cat /spark/events/${app}/* | grep "SparkListenerStageSubmitted" | awk -F"," '{print $2}' | awk -F: '{print $NF}' | sort -n | tr '\n' ' '`
    NoOfStages=`echo $stg | wc -w` 
    echo "StageID,TimeTaken, NumOfTasks, NumTasksSuccess, NumTasksFailed, TotalInpBytesRead, NumProcLocal, NumNodeLocal, NumRackLocal, AvgExeDesTime, MaxExeDesTime, MaxGCTime, MaxGCTaskID, TotalMemByteSpill, TotalDiscByteSpill, TotalShufByteRead, TotalShufByteWrite" >> ${app}_Stats.csv
    for i in $stg
    do
        hadoop fs -cat /spark/events/${app}/* |  grep "\"Stage ID\":$i," > /tmp/stage_$i
        wait 
        echo -n "Stage-ID${i}," >> ${app}_Stats.csv
        python gather_stats.py -f /tmp/stage_$i >> ${app}_Stats.csv
        rm -rf /tmp/stage_$i      
    done 
    wait
    #JT=`grep -i 'Stage-ID' ${app}_Stats.csv | awk -F, '{sum+=$2};END{print sum}'`
fi

IFS='\n'
for line in  `cat ${app}_Stats.csv`
do

echo $pid,$app,$jobname,$line

done


done
