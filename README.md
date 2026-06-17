# Toshkent Havo Sifati — Real Vaqt Monitoring Pipeline

OpenWeatherMap API orqali Toshkent shahrining havo sifatini real vaqtda
kuzatib boruvchi avtomatik pipeline — ma'lumotlar MySQL bazasiga yoziladi
va Tableau orqali vizualizatsiya qilinadi.

## Loyiha arxitekturasi
## Texnologiyalar

| Texnologiya | Maqsad |
|-------------|--------|
| Python 3 | Asosiy pipeline kodi |
| OpenWeatherMap API | Real vaqt havo ma'lumotlari |
| MySQL | Ma'lumotlarni saqlash |
| Tableau | Vizualizatsiya va dashboard |
| python-dotenv | API kalitlarini himoya qilish |

## Ma'lumotlar tuzilmasi

`air_quality_logs` jadvali:

| Ustun | Turi | Tavsif |
|-------|------|--------|
| id | INT | Avtomatik raqam |
| recorded_at | DATETIME | O'lchov vaqti (unique) |
| aqi | INT | Havo sifati indeksi (1-5) |
| pm2_5 | FLOAT | Mayda zarrachalar (µg/m³) |
| pm10 | FLOAT | Yirik zarrachalar (µg/m³) |
| co | FLOAT | Is gazi (µg/m³) |
| no2 | FLOAT | Azot dioksid (µg/m³) |
| o3 | FLOAT | Ozon (µg/m³) |
| so2 | FLOAT | Oltingugurt dioksid (µg/m³) |

## O'rnatish

### 1. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 2. MySQL bazasini yaratish
```bash
mysql -u root -p < schema.sql
```

### 3. .env fayli yaratish
Loyiha papkasida `.env` fayli yarating:
