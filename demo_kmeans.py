from pyspark import SparkContext
from numpy import array
from pyspark.mllib.clustering import KMeans, KMeansModel

def filterData(x):
    line = x.split(',')
    data = list()
    data = line[4:10] + line[13:16]
    return [float(x) for x in data]


sc = SparkContext(appName='k_means Demo')
data = sc.textFile("hdfs://10.0.1.236:9000/kmeans_data.csv")
parsedData = data.filter(lambda x: len(x.split(',')) == 15).map(lambda x: filterData(x)).map(lambda x: array(x))
clusters = KMeans.train(parsedData, 2, maxIterations=300, initializationMode="random")
print('====================================================cluster centers======================================================================')
print(clusters.clusterCenters)
