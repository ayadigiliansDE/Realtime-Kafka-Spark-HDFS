# 🚀 Real-Time Kafka Spark Streaming Pipeline

![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Spark](https://img.shields.io/badge/Spark-Processing-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## 📌 Overview
This project is a real-time data engineering pipeline built using Apache Kafka, Spark Streaming, Hadoop HDFS, and Docker. It simulates an end-to-end streaming workflow: data ingestion → processing → storage.

## 🧱 Architecture
- Kafka Producer → generates streaming data  
- Kafka Broker → handles message streaming  
- Spark Streaming → processes real-time data  
- Hadoop HDFS → stores processed output  
- Docker Compose → runs the full system  

## ⚙️ Tech Stack
Kafka • Spark • Hadoop HDFS • Python (PySpark) • Docker • Docker Compose  

## 📁 Project Structure
Realtime-Kafka-Spark-HDFS/  
├── producer.py  
├── docker-compose.yml  
├── scripts/spark_streaming.py  
├── images/  
│   ├── kafka_producer.png  
│   ├── spark_streaming.png  
│   ├── hdfs_output.png  
│   └── docker_status.png  

## ▶️ How to Run
docker-compose up -d  
python producer.py  
python scripts/spark_streaming.py  

## 📊 Screenshots
Kafka Producer → images/kafka_producer.png  
Spark Streaming → images/spark_streaming.png  
HDFS Output → images/hdfs_output.png  
Docker Status → images/docker_status.png  

## 🎯 Goal
To build a complete real-time data pipeline using Kafka, Spark Streaming, and Hadoop inside Docker.

## 👩‍💻 Author
Data Engineering Project
