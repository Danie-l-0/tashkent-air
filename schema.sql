CREATE DATABASE IF NOT EXISTS tashkent_air_monitoring;
USE tashkent_air_monitoring;

CREATE TABLE IF NOT EXISTS air_quality_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recorded_at DATETIME UNIQUE,
    aqi INT,
    pm2_5 FLOAT,
    pm10 FLOAT,
    co FLOAT,
    no2 FLOAT,
    o3 FLOAT,
    so2 FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
