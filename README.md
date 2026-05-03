# 🚀 Real-Time Kafka Spark Streaming Pipeline

This project is a real-time data engineering pipeline built using **Kafka, Spark Streaming, Hadoop HDFS, and Docker**.  
It simulates streaming data ingestion, processing, and storage in a distributed environment.

---

## 🧱 Architecture Overview

The pipeline consists of the following components:

- **Kafka Producer**: Generates and sends streaming data
- **Kafka Broker**: Handles message streaming
- **Spark Streaming Job**: Processes real-time data
- **HDFS (Hadoop)**: Stores processed data
- **Docker Compose**: Orchestrates the entire environment

---

## ⚙️ Tech Stack

- Apache Kafka
- Apache Spark (Structured Streaming)
- Hadoop HDFS
- Python (PySpark)
- Docker & Docker Compose

---

## 📁 Project Structure

---

## ▶️ How to Run

1. Start the cluster:
```bash
docker-compose up -d
python producer.py
python scripts/spark_streaming.py
📊 Screenshots

All execution evidence and system outputs are included below:

📌 Stored in images/ folder

Kafka Producer running
Spark Streaming processing
HDFS output results
Docker containers status
🎯 Project Goal

To demonstrate a real-time data pipeline that:

Ingests streaming data
Processes it using Spark
Stores results in HDFS
Runs fully inside Docker containers
👩‍💻 Author

Developed as part of a Data Engineering learning journey.

---

# 🚀 بعد ما تلصقيه اعملي:

```bash
git add README.md
git commit -m "Add professional README"
git push origin main
