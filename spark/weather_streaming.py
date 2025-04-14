
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType, IntegerType

spark = SparkSession.builder     .appName("WeatherStreaming")     .config("spark.jars", "/opt/spark/jars/postgresql-42.2.18.jar")     .getOrCreate()

schema = StructType()     .add("city", StringType())     .add("temperature", FloatType())     .add("humidity", IntegerType())     .add("description", StringType())

df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "kafka:9092")     .option("subscribe", "weather")     .load()

weather_df = df.selectExpr("CAST(value AS STRING)")     .select(from_json(col("value"), schema).alias("data"))     .select("data.*")

weather_df.writeStream     .foreachBatch(lambda batch_df, _: batch_df.write         .format("jdbc")         .option("url", "jdbc:postgresql://postgres:5432/weather")         .option("dbtable", "weather_stats")         .option("user", "user")         .option("password", "pass")         .option("driver", "org.postgresql.Driver")         .mode("append")         .save())     .start()     .awaitTermination()
