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

path = '/data/collector/xyz/2016/01/01/00/'
binInterval = 05
startEpoch = 1481220000
sourceEpoch = 1451606400
outpath = '/data/replicated_data/'
no_of_hours = 3


def unionAll(dfs):
    return reduce (DataFrame.unionAll, dfs)


list = []
for i in range (00, 60, binInterval):
    i = "{:0>2}".format (i)
    df = sqlContext.parquetFile (path + str (i) + '/*')
    list.append (df)

while no_of_hours > 0:
    OffSet = int (startEpoch) - sourceEpoch
    count = 0
    for i in list:
        count = "{:0>2}".format (count)
        df = i.withColumn ('FIRST_SWITCHED', i.FIRST_SWITCHED + OffSet)
        dfs = [[df]]
        dfs = [y for x in dfs for y in x]
        df_final = unionAll (dfs)
        df_final.coalesce (8).write.parquet (outpath + str (startEpoch) + '/' + str (count))
        count = int (count) + binInterval
    startEpoch = int (startEpoch) + 3600
    no_of_hours = no_of_hours - 1
