
CREATE TABLE IF NOT EXISTS weather_stats (
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    description VARCHAR(100),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
