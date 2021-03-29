import sys
import os
import tempfile
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
import pyspark.sql.readwriter
from pyspark.sql.types import DateType
from pyspark.sql.functions import col, udf, unix_timestamp
from datetime import datetime
import py4j
from pyspark.sql import DataFrame
from functools import reduce
import itertools
import time
import subprocess
from commands import *
from pyspark.sql.functions import col
import optparse
import re
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

appName = "NetflowReplication:QA"
conf = SparkConf ().setAppName (appName)

conf.setExecutorEnv ('PYTHONPATH', '/opt/spark/python:/opt/spark/python/lib/py4j-0.8.2.1-src.zip')

conf.set ("spark.driver.maxResultSize", "2g")
sc = SparkContext (conf=conf)
sqlContext = HiveContext (sc)

if len(sys.argv) < 3:
	print "Usage: /opt/spark/bin/spark-submit "+ sys.argv[0] +" <netflow input path> <file with list of IP addresses to filter> <output filtered netflow text directory>"
	sys.exit()
path = sys.argv[1]
input_ip = sys.argv[2]
output = sys.argv[3]

list = []
for line in open(input_ip):
	line=line.strip('\n')
	line=sum( [int(i)*2**(8*j) for  i,j in zip( line.split('.'), [3,2,1,0]) ] )
	list.append(line)
print list
df = sqlContext.parquetFile(path)
df.count()
df_filtered=df.where(col("IPV4_SRC_ADDR").isin(list))
df_filtered.rdd.map(lambda row: [str(c) for c in row]).saveAsTextFile(output)