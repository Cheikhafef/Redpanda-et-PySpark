  GNU nano 7.2                                                               spark/stream_tickets.py                                                                        import os
os.environ["HADOOP_HOME"] = "C:\\hadoop"
os.environ["hadoop.home.dir"] = "C:\\hadoop"
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, lit, when, count, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Spark session
spark = SparkSession.builder \
    .appName("TicketsStreaming") \
    .config("spark.sql.shuffle.partitions", "2") \
    .config("spark.hadoop.fs.permissions.umask-mode", "022") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .config("spark.hadoop.fs.hdfs.impl", "org.apache.hadoop.hdfs.DistributedFileSystem") \
    .getOrCreate()


spark.sparkContext.setLogLevel("WARN")

# Schéma JSON
schema = StructType([
    StructField("ticket_id", IntegerType()),
    StructField("client_id", IntegerType()),
    StructField("created_at", StringType()),
    StructField("demande", StringType()),
    StructField("type_demande", StringType()),
    StructField("priorite", StringType())
])

# Lecture depuis Redpanda
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "client_tickets") \
    .option("startingOffsets", "latest") \
    .load()