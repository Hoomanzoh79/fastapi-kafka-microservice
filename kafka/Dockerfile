# kafka/Dockerfile
FROM bitnami/kafka:latest

COPY kafka-setup.sh /kafka-setup.sh
RUN chmod +x /kafka-setup.sh

CMD ["/kafka-setup.sh"]