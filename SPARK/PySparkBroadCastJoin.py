from pyspark import SparkContext as sc

def broadCastSpark(dataset1, dataset2):
    dataset1_rdd = sc.parallelize(dataset1).map(lambda x: x.split(",")).mapValues(lambda x: int(x)).reduceByKey(
        lambda x, y: x + y)

    dataset2_rdd = sc.parallelize(dataset2).map(lambda x: tuple(x.split(",")))

    for i in dataset1_rdd.join(dataset2_rdd).map(
            lambda x: str(x[0]) + "," + str(x[1][1]) + "," + str(x[1][0])).collect(): print i


# Input 

dataset1 = ["10.1.0.1,1000", "10.1.0.2,2000", "10.1.0.3,3000"] * 1000
dataset2 = ["10.1.0.1,hostname1", "10.1.0.2,hostname2", "10.1.0.3,hostname3"]


broadCastSpark(dataset1, dataset2)




'''Results
10.1.0.1,hostname1,1000000
10.1.0.2,hostname2,2000000
10.1.0.3,hostname3,3000000
'''
