
# Real-Time Weather Monitoring Pipeline

This project demonstrates a real-time data processing pipeline for weather data using:

- **Kafka**: For real-time data streaming.
- **Spark Structured Streaming**: To process incoming weather data.
- **PostgreSQL**: To store the processed data.
- **Docker**: To containerize the entire solution.

### Steps to Run:

1. Clone the repository:
    ```
    git clone <your-repo-link>
    cd weather-streaming-pipeline
    ```

2. Build and start Docker containers:
    ```
    docker-compose up --build
    ```

3. Start the Kafka producer:
    ```
    docker exec -it <kafka-container> bash
    python kafka/weather_producer.py
    ```

4. Start Spark streaming:
    ```
    docker exec -it <spark-container> bash
    spark-submit spark/weather_streaming.py
    ```

5. Optionally, build a dashboard with Streamlit or Grafana to visualize real-time weather data.

### Technologies Used:
- Apache Kafka
- Apache Spark
- PostgreSQL
- Docker
- Python

### License:
MIT License
