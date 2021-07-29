
# pip install python-kafka

from kafka import KafkaProducer,KafkaConsumer

print("starting Producer")
producer = KafkaProducer(bootstrap_servers='localhost:29092')
producer.send('topic_name', b'some_message_bytes')
print("Message Sent\n\n\n")

print("starting Consumer")
consumer = KafkaConsumer('topic_name',bootstrap_servers='localhost:29092' ,auto_offset_reset='earliest')
for msg in consumer: print (msg.topic,msg.value)