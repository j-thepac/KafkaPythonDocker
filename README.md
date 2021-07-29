# Kafka Python Docker 


## Summary
The kafka service is exposed to the host applications through port 29092 and Bootstrap servers property to connect to the Kafka server listening at port 29092 for the host machine.

##### cluster
 9092/tcp, 0.0.0.0:29092->29092/tcp 

#####  zookeeper 
 2888/tcp, 3888/tcp, 0.0.0.0:22181->2181/tcp 

## Pre-Req:
- Python is installed
- Docker is installed
- Docker compose is installed

## Steps :
- Git clone this repo
- docker-compose up -d
- docker-compose logs kafka | grep -i started #check logs (optional)
- Create virtual Environment
- pip install python3-kafka
- $python main.py

## Stop Docker
docker-compose down

## Run Manually (Optional) :

https://kafka.apache.org/quickstart
http://catchbug.blogspot.com/search?q=kafka



## Reference : 
https://www.baeldung.com/ops/kafka-docker-setup