#import boto3
import os,sys
import os.path
import pyspark.sql.functions as psf
from pyspark.sql import SparkSession


# spark = (SparkSession.builder.config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.1.2',)
#     .config("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
#     .config("fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
#     .getOrCreate()
# )

#df = spark.read.json("s3://dataminded-academy-capstone-resources/raw/open_aq/")
#df.write.format('json').save('save.json')
spark = (SparkSession.builder.config('spark.jars.packages', 
 'org.apache.hadoop:hadoop-aws:3.1.2,net.snowflake:spark-snowflake_2.12:2.9.0-spark_3.1,net.snowflake:snowflake-jdbc:3.13.3')
 .getOrCreate())
df = spark.read.json("save.json")
df.show()
df.printSchema()
df.select("*","coordinates.latitude","coordinates.longitude","date.local","date.utc").drop("coordinates","date").show()

