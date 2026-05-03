"""from kafka import KafkaProducer

import json , time , random 

producer = KafkaProducer(
    bootstrap_servers = "localhost:9092", 
    value_serializer = lambda v: json.dumps(v).encode('utf_a')
)

while True :
    data = {
        
        "tx_id" : random.randint(1000, 9999), 
        "amount": round(random.uniform(10.5, 500.0), 2),
        "currency": random.choice(["USD", "EUR", "GBP"]),
        "timestamp": int(time.time())
        
    }   
    
    print(f"sent : {data}")
    time.sleep(1) """
    
    
    
from kafka import KafkaProducer
import json
import time
import random

# create producer
producer = KafkaProducer(
 bootstrap_servers="localhost:9092",
 value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# send messages
while True:
 data = {
 "value": random.randint(1000, 9999),
 "amount": round(random.uniform(10.5, 500.0), 2),
 "currency": random.choice(["USD", "EUR", "GBP"]),
 "timestamp": int(time.time()),
 }

 producer.send("transaction", value=data)
 print(f"Sent: {data}")

 time.sleep(1)

producer.flush()