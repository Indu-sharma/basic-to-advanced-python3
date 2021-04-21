import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext
from pyspark.sql.functions import col

appName = "ParquetPyspark::Filter"
conf = SparkConf().setAppName(appName)

conf.setExecutorEnv('PYTHONPATH', '/opt/spark/python:/opt/spark/python/lib/py4j-0.8.2.1-src.zip')

conf.set("spark.driver.maxResultSize", "2g")
sc = SparkContext(conf=conf)
sqlContext = HiveContext(sc)

if len(sys.argv) < 3:
    print "Usage: /opt/spark/bin/spark-submit --master yarn  --deploy-mode client   --executor-memory 2G --num-executors 2 --total-executor-cores 2 " + sys.argv[
        0] + " <input parquet files directory> <file with list of IP addresses to filter> <output filtered text directory>"
    sys.exit()
input_path = sys.argv[1]
input_ip = sys.argv[2]
output_path = sys.argv[3]

list = []
for line in open(input_ip).readlines():
    line = line.strip('\n')
    list.append(line)
df = sqlContext.parquetFile(input_path)
df_filtered = df.where(col("IPV4_SRC_ADDR").isin(list))
df_filtered.rdd.map(lambda row: [str(field) for field in row]).saveAsTextFile(output_path)
