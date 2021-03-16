#!/usr/bin/python
#__Author__: Indu Sharma
import commands
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
import sys
import subprocess
import os
Loop=0
while Loop ==  0:
    def sendmail(output,per):
        to_address=["indu.sharma@xyz.com"]   ## Put your recievers here
        print "Sending e-mail to :" + str(to_address)
        msg = MIMEMultipart()
        msg['From'] = 'Hadoop-SETUP'
        msg['To'] =  "; ".join(to_address)
        DN_disk="; ".join(DNdiskFullList)
        if int(per) == 11:
            msg['Subject'] = 'CRITICAL:HDFS-Usage or NN Disk >= 90% & DNs'+DeadList+' are DEAD!!!!!'
        elif int(per) == 1:
            msg['Subject'] = 'CRITICAL:DNs: '+DeadList+' DEAD!!!!!'
        elif int(per) == 0:
            msg['Subject'] = 'CRITICAL:HDFS-Usage or NN Disk >= 90% !!!!!' 
        elif int(per) == 2:
            msg['Subject'] = 'CRITICAL:NameNode is in SAFE-MODE !!!!!'
        elif int(per) == 4:
            msg['Subject'] = 'CRITICAL:DNs Disk-Usage >= 90% :'+DN_disk+' !!!!!'
        elif int(per) == 3:
            msg['Subject'] = 'CRITICAL:NameNode Free memory is '+ str(nn_mem) +'GB !!!!!'
        message = str(output)
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP("192.168.104.25")
        mailserver.ehlo()
        for i in to_address:
            msg['To']=i
            print "sending to",i
            mailserver.sendmail(i,i,msg.as_string())
        mailserver.quit()

    cmd="free -g | awk 'NR ==2{print $4}'"
    (nn_mem,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    cmd="hdfs dfsadmin -safemode get | grep -ic 'Safe mode is ON'"
    (mode,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    output="Dear Team,\n Please check the setup ASAP. Following is the status of the setup:\n**** HDFS Usage Stats Summary******\n"
    cmd="hadoop fs -df -h"
    (output1,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    cmd="hadoop fs -df -h | awk  'NR>1{print $NF}'|sed 's/%//g'"
    (hdfs_per,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    cmd="hdfs dfsadmin -report -dead | grep -i 'Dead data' | sed -r 's/Dead datanodes//g;s/\(//;s/\)//;s/://'"
    (dead,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    cmd="hadoop dfsadmin -report"
    output=output+output1
    (output2,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    output=output+"\n*******HDFS data Nodes Reports********"+output2
    cmd="df -klh /data"
    (output3,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    output=output+"\n********NAMENODE Local /data is Usage *************\n"+output3
    cmd="df -klh /data | awk  'NR>1{print $(NF-1)}'|sed 's/%//g'"
    (NN_per,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    cmd="hdfs dfsadmin -report -dead | perl -ne 'next unless m/Name:/;' -e 's/^.*\((.*)\).*/\\1 /;' -e 'print;'|tr '\\n' ',' > /tmp/DeadList "
    os.system(cmd)
    cmd="cat /tmp/DeadList"
    (DeadList,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    print DeadList
    cmd="hdfs dfsadmin -report | perl -ne 'next unless m/Name:/;' -e 's/^.*\((.*)\).*/\\1 /;' -e 'print;'|tr '\\n' ',' > /tmp/AllList "
    os.system(cmd)
    cmd="cat /tmp/AllList"
    (AllList,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
    output=output+'\n****NameNode Free Memory:***\n'+str(nn_mem).strip('\n')+'GB'
    output=output+'\n****DNs Disk Usage %:*******\n'
    DNdiskFullList=[]
    for i in AllList.split(','):
        i=i.strip('\n')
        if i.strip():
            cmd="ssh root@"+i+" \"df -klh /data | awk  'NR>1{print \$(NF-1)}'|sed 's/%//g'\""
            (DN_per,status)=subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True).communicate()
            output=output+i+','+str(DN_per)+'\n'
            if DN_per:
                if int(DN_per) > 89:
                    DNdiskFullList.append(i)  
    if int(mode) > 0:
        usage=2
        sendmail(output,usage)  
    elif (int(hdfs_per) > 89 or int(NN_per) > 89) and int(dead) > 0 :
        usage=11
        sendmail(output,usage)
    
    elif int(dead) > 0:
        usage=1
        sendmail(output,usage)
    
    elif int(hdfs_per) > 89 or int(NN_per) > 89:
        usage=0
        sendmail(output,usage)
    elif len(DNdiskFullList) > 0:
        usage=4
        sendmail(output,usage)
    elif int(nn_mem) < 3:
        usage=3
        sendmail(output,usage)
    time.sleep(36000)
