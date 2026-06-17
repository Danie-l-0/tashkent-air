import time
from datetime import datetime
import mysql.connector
import requests
from dotenv import load_dotenv
import os

# .env faylidan maxfiy ma'lumotlarni yuklash
load_dotenv()

API_KEY = os.getenv("API_KEY")
LAT = "41.2995"
LON = "69.2401"
URL = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": 3306
}


def fetch_air_quality():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[{datetime.now()}] API xatosi: {response.status_code}")
            return None
    except Exception as e:
        print(f"[{datetime.now()}] Ulanishda xatolik: {e}")
        return None


def save_to_mysql(data):
    if not data:
        return
    try:
        pollution_data = data["list"][0]
        aqi = pollution_data["main"]["aqi"]
        comp = pollution_data["components"]
        timestamp = pollution_data["dt"]
        recorded_at = datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = """
        INSERT IGNORE INTO air_quality_logs 
        (recorded_at, aqi, pm2_5, pm10, co, no2, o3, so2) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            recorded_at, aqi,
            comp["pm2_5"], comp["pm10"],
            comp["co"], comp["no2"],
            comp["o3"], comp["so2"],
        )
        cursor.execute(query, values)
        conn.commit()
        print(f"[{recorded_at}] Muvaffaqiyatli yozildi! AQI: {aqi}")
    except mysql.connector.Error as err:
        print(f"MySQL xatolik: {err}")
    finally:
        if "conn" in locals() and conn.is_connected():
            cursor.close()
            conn.close()


print("Toshkent havo monitoringi ishga tushdi...")
while True:
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Ma'lumot olinmoqda...")
    raw_data = fetch_air_quality()
    save_to_mysql(raw_data)
    for i in range(60, 0, -1):
        print(f"\r{i} soniya qoldi...", end="", flush=True)
        time.sleep(1)
