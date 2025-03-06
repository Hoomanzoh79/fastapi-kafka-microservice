# fastapi-kafka-microservice
## Getting Started
1- [Overview](#Overview)\
2- [Project Structure](#Project_Structure)\
3- [Setup Instructions](#Setup_Instructions) 

## Overview

This project demonstrates how to build two FastAPI microservices that communicate with each other using Apache Kafka. The microservices are containerized using Docker, and the setup includes Kafka and Kafka-UI for monitoring.

### Languages And Tools
	
<div>
	<img src="https://skillicons.dev/icons?i=python"/>
	<img src="https://skillicons.dev/icons?i=fastapi"/>
	<img src="https://skillicons.dev/icons?i=docker"/>
 <img src="https://skillicons.dev/icons?i=kafka"/>
</div>

## Project_Structure

```
root/
├── microservice1/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── kafka_config.py
│   │   └── kafka_producer.py
│   ├── requirements.txt
│   └── Dockerfile
├── microservice2/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── kafka_config.py
│   │   └── kafka_consumer.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
```

## Setup_Instructions

#### 1. Requirements : 
docker & docker-compose installed on your machine 💻

#### 2. Clone the Repository
```
git clone https://github.com/Hoomanzoh79/fastapi-kafka-microservice.git
```
#### 3. Start the Services 
Run the following command to start all services:
```
docker-compose up --build
```
#### 4. Access the Services 
```microservice1: http://localhost:8081/docs```

```microservice2: http://localhost:8082/docs```

```Kafka-UI: http://localhost:8080```
