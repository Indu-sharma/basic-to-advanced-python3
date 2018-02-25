# Hostname, PID, CPU_usage, Num_threads
probe_name=$(basename $0 .${0##*.})

PID_list=`python PID_extracter.py $probe_name`

echo "PID;Vmem;RSS;SwapMem"
while [ 1 ]
do
PID_list=`python PID_extracter.py $probe_name`
IFS=','
for pid in  $PID_list
do

mem_stats=`cat /proc/$pid/status | awk -F':' '$1~/VmPeak|VmRSS|VmSwap/{print $2}' | sed -r 's/kB//g;s/^[ \t]+//;s/[ \t]+$//' | tr '\n' ';'`

echo ${pid}';'${mem_stats}
done
sleep 10
done

