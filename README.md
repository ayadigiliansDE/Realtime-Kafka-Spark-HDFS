# Realtime-Kafka-Spark-HDFS Pipeline

## Overview
This project implements a robust, real-time data pipeline that synchronizes streaming data from **Kafka** to **HDFS** using **Apache Spark**. The system is designed to handle live transaction streams, process them in micro-batches, and store them in an optimized columnar format for long-term storage and analysis.

## Architecture
The pipeline follows a standard Big Data architecture:
1.  **Data Producer:** A Python script that simulates real-time electricity transaction data.
2.  **Message Broker:** **Apache Kafka** ensures reliable data ingestion and buffering.
3.  **Processing Engine:** **Apache Spark Structured Streaming** consumes the data, applies a predefined schema, and handles the micro-batch logic.
4.  **Storage Layer:** **Hadoop HDFS** serves as the Data Lake, storing the processed output in **Parquet** format.

## Implementation Details

### Data Schema
The pipeline enforces the following schema on the incoming JSON stream:
*   **id**: Unique transaction identifier.
*   **value**: Measured electricity consumption value.
*   **amount**: Financial cost of the transaction.
*   **currency**: Currency unit.
*   **timestamp**: Event generation time.

### Storage Optimization
Data is sinked to HDFS at `/data/raw/transactions_parquet` with the following optimizations:
*   **Format:** Parquet (Optimized for analytical queries).
*   **Compression:** Snappy (Balances CPU usage and storage space).

## Execution Evidence

### 1. Spark Batch Processing
The Spark engine successfully processes micro-batches and manages offsets. Evidence of batch commits can be seen in the processing logs below:

![Spark Processing Logs](Screenshot%202026-05-03%20124214.png)

### 2. HDFS File System Verification
The HDFS environment confirms the successful creation of over 1,100 Parquet files, ensuring data persistence and scalability:

![HDFS Parquet Files](Screenshot%202026-05-03%20124542.jpg)

## How to Run
1.  **Start Infrastructure:**
    ```bash
    docker-compose up -d
    ```
2.  **Submit Spark Streaming Job:**
    ```bash
    docker exec -it spark-master /spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0 /opt/spark-apps/spark_streaming.py
    ```
3.  **Start Data Producer:**
    ```bash
    python scripts/producer.py
    ```
