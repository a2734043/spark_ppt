#!/bin/bash

bin/spark-submit \
   --master k8s://https://10.0.0.228:6443 \
   --deploy-mode cluster \
   --name spark-pi \
   --class org.apache.spark.examples.SparkPi \
   --conf spark.executor.instances=2 \
   --conf spark.kubernetes.container.image=spark:2.4.5\
   --conf spark.kubernetes.container.image.pullPolicy=Never \
   --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
   /opt/spark/examples/jars/spark-examples_2.11-2.4.5.jar 100
