# fastapi-kafka-microservice
## Getting Started
1- [Overview](#Overview)\
2- [Project Structure](#project_structure) \
3- [Setup Instructions](#setup_instructions) \

## Overview

This project demonstrates how to build two FastAPI microservices that communicate with each other using Apache Kafka. The microservices are containerized using Docker, and the setup includes Kafka and Kafka-UI for monitoring.

### Languages And Tools
	
<div>
	<img src="https://skillicons.dev/icons?i=python"/>
	<img src="https://skillicons.dev/icons?i=fastapi"/>
	<img src="https://skillicons.dev/icons?i=docker"/>
 <img src="https://skillicons.dev/icons?i=kafka"/>
</div>

## Project Structure

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

## Setup Instructions

&ensp;1. Prerequisites : \
&ensp;&ensp;&ensp;&ensp;Docker and Docker Compose installed on your machine.

&ensp;2. Clone the Repository\
```
git clone https://github.com/Hoomanzoh79/fastapi-kafka-microservice.git
```
&ensp;3. Start the Services
Run the following command to start all services:
```
docker-compose up --build
```
&ensp;4. Access the Services\
```microservice1: http://localhost:8081/docs```

```microservice2: http://localhost:8082/docs```

```Kafka-UI: http://localhost:8080```

