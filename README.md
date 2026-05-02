# Real-Time Data Pipeline: Kafka to HDFS with Spark Streaming

This repository contains a real-time ETL pipeline developed to demonstrate the integration between **Apache Kafka**, **Apache Spark Structured Streaming**, and **Hadoop HDFS**.

## 🏗️ System Architecture
The pipeline follows a modern big data flow:
1.  **Data Source:** Real-time transaction data is produced to an **Apache Kafka** topic.
2.  **Stream Processing:** **PySpark** subscribes to the Kafka topic, applies schema enforcement, and processes the micro-batches.
3.  **Data Sink:** The processed data is stored in **Hadoop HDFS** using the **Parquet** columnar format for optimized storage and fast analytical queries.

## 🛠️ Tech Stack
*   **Language:** Python (PySpark)
*   **Message Broker:** Apache Kafka
*   **Processing Engine:** Apache Spark 3.0.0
*   **Storage Layer:** Hadoop HDFS
*   **Infrastructure:** Docker & Docker Compose

## 🚀 Key Implementation Details
### 1. Handling Dependencies
During the session, a core challenge was connecting Spark to Kafka. This was resolved by injecting the required Maven coordinates during runtime:
```bash
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0
