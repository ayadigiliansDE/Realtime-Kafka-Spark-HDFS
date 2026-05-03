from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import (
 StructType,
 StructField,
 StringType,
 IntegerType,
 DoubleType,
)

spark = SparkSession.builder.appName("KafkaToParquet").getOrCreate()

schema = StructType(
 [
 StructField("id", IntegerType()),
 StructField("value", IntegerType()),
 StructField("amount", DoubleType()),
 StructField("currency", StringType()),
 StructField("timestamp", IntegerType()),
 ]
)

df = (
 spark.readStream.format("kafka")
 .option("kafka.bootstrap.servers", "broker:29092")
 .option("subscribe", "transaction")
 .load()
)

json_df = (
 df.selectExpr("CAST(value AS STRING)")
 .select(from_json(col("value"), schema).alias("data"))
 .select("data.*")
)

query = (
 json_df.writeStream.outputMode("append")
 .format("parquet")
 .option("path", "hdfs://namenode:9000/data/raw/transactions_parquet")
 .option(
 "checkpointLocation",
 "hdfs://namenode:9000/data/checkpoints/streaming_to_parquet",
 )
 .start()
)

query.awaitTermination()