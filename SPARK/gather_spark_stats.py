import json
from optparse import OptionParser
import math


def parseEventLog(file):
    
    def convertTime(timeTaken):
            v=(timeTaken)/60000.0
            timeTaken = math.ceil(v*100)/100
            return timeTaken
    fileHdlr = open(file,"r")
    lines = fileHdlr.readlines()
    
    eventSubmitList = []
    eventStartedList = []
    eventEndedList = []
    eventCompletedList = []

    #init all variables
    numOfTasks = 0
    numTasksSuccess = 0
    totalInpBytesRead = 0
    maxExeDesTime = 0
    totalExeDesTime = 0
    maxGCTime = 0
    gcTime = 0
    maxGCTaskID = -1
    totalMemByteSpill = 0
    totalDiscByteSpill = 0
    totalShufByteWrite = 0
    totalShufByteRead = 0
    numTasksFailed = 0
    avgExeDesTime = 0 
    numProcLocal = 0
    numNodeLocal = 0
    numRackLocal = 0

    for l in lines:
        if ("SparkListenerTaskStart" in l):
            eventStartedList.append(json.loads(l))
        elif ("SparkListenerStageSubmitted" in l):
            eventSubmitList.append(json.loads(l))
        elif ("SparkListenerTaskEnd" in l):
            eventEndedList.append(json.loads(l))
        elif ("SparkListenerStageCompleted" in l):
            eventCompletedList.append(json.loads(l))
    #Number of tasks in the stage
    try:
        numOfTasks = eventCompletedList[0]["Stage Info"]["Number of Tasks"] 
    except:
        numOfTasks = 0
    
    #Time taken for the stage
    try:
        launchedTime = int(eventCompletedList[0]["Stage Info"]["Submission Time"])
        completedTime = int(eventCompletedList[0]["Stage Info"]["Completion Time"])
    except:
        launchedTime = 0
        completedTime = 0
    timeTaken=completedTime - launchedTime
    timeTaken=convertTime(timeTaken)
    #Iterate through the logs to get the stats from Task ended logs
    for i in range(len(eventEndedList)):
        #Completion status success
        try:
            if (eventEndedList[i]["Task End Reason"]["Reason"] == "Success"):
                numTasksSuccess = numTasksSuccess + 1
        except:
            numTasksSuccess = 0

        #Total input bytes read
        try:
            totalInpBytesRead = totalInpBytesRead + int(eventEndedList[i]["Task Metrics"]["Input Metrics"]["Bytes Read"])
        except:
            totalInpBytesRead = "NA"

        #Executor Deserialize Time - total/max
        try:
            exeDesTime = int(eventEndedList[i]["Task Metrics"]["Executor Deserialize Time"])
            exeDesTime=convertTime(exeDesTime)
        except:
            exeDesTime = 0
            
        if (maxExeDesTime < exeDesTime):
            maxExeDesTime = exeDesTime
        totalExeDesTime = totalExeDesTime + exeDesTime
        totalExeDesTime=convertTime(totalExeDesTime)
        
        #Max GC time and the task id
        try:
            gcTime = int(eventEndedList[i]["Task Metrics"]["JVM GC Time"])  
        except:
            gcTime = 0
        if(maxGCTime < gcTime):
            maxGCTime = gcTime
            maxGCTaskID = i
        maxGCTime=convertTime(maxGCTime)
        #Total memory bytes spilled
        try:
            totalMemByteSpill = totalMemByteSpill + int(eventEndedList[i]["Task Metrics"]["Memory Bytes Spilled"])
        except:
            totalMemByteSpill = "NA"


        #Total disk bytes spilled
        try:
            totalDiscByteSpill = totalDiscByteSpill + int(eventEndedList[i]["Task Metrics"]["Disk Bytes Spilled"])
        except:
            totalDiscByteSpill = "NA"


        #Total shuffle bytes written
        try:
            totalShufByteWrite = totalShufByteWrite + int(eventEndedList[i]["Task Metrics"]["Shuffle Write Metrics"]["Shuffle Bytes Written"])
        except:
            totalShufByteWrite = "NA" 

        #Total shuffle bytes read
        try:
            totalShufByteRead = totalShufByteRead + int(eventEndedList[i]["Task Metrics"]["Shuffle Read Metrics"]["Remote Bytes Read"])
        except:
            totalShufByteRead = "NA"
    
    #Completion status failure
    if (numTasksSuccess == numOfTasks):
        numTasksFailed = 0
    else:
        numTasksFailed = numOfTasks - numTasksSuccess


    #Average executor deserialized time
    avgExeDesTime = totalExeDesTime/numOfTasks

    avgExeDesTime=convertTime(avgExeDesTime)
    #Iterate through the logs to get the stats from taskStarted logs
    for i in range(len(eventStartedList)):
        try:
            locality = eventStartedList[i]["Task Info"]["Locality"]
        except:
            locality = "NA"

        #No of Process_local tasks
        if (locality == "PROCESS_LOCAL"):
            numProcLocal = numProcLocal + 1
        
        #No of Node_local tasks
        elif (locality == "NODE_LOCAL"):
            numNodeLocal = numNodeLocal + 1

        #No of Rack_local tasks
        elif (locality == "RACK_LOCAL"):
            numRackLocal = numRackLocal + 1


    return("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(timeTaken, numOfTasks, numTasksSuccess, numTasksFailed, totalInpBytesRead, numProcLocal, numNodeLocal, numRackLocal, avgExeDesTime, maxExeDesTime, maxGCTime, maxGCTaskID, totalMemByteSpill, totalDiscByteSpill, totalShufByteRead, totalShufByteWrite))

parser = OptionParser()
parser.add_option("-f", "--file", dest="eventLog",help="file name of the Event Log", metavar="FILE")
(options, args) = parser.parse_args()
if (options.eventLog != None):
    file = options.eventLog
    resStr = parseEventLog(file)
    print resStr 
else:
    print " "
    exit(-1)
