FROM bitnami/spark:3.5.8

WORKDIR /app

COPY stream_tickets.py .

CMD ["/opt/bitnami/spark/bin/spark-submit", \
"--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.8", \
"/app/stream_tickets.py"]
