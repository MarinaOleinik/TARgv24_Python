import requests
import tkinter as tk
from tkinter import messagebox
# 1. Получаем API-ключ OpenWeatherMap:
#     Регистрируемся на https://openweathermap.org/api.
#     Берём бесплатный API-ключ.
#     Твой API-ключ (замени на свой из OpenWeatherMap)
API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#   Функция для получения погоды
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Viga", "Sisesta linn!")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].capitalize()

        weather_label.config(text=f"🌡 Tmp: {temp}°C\n💧 Niiskus: {humidity}%\n☁ {description}")
    else:
        messagebox.showerror("Viga", "Midagi äks valesti. Konntrolli linna nimetus.")

# 🔹 Создание GUI
app = tk.Tk()
app.title("Ilm")
app.geometry("300x250")

tk.Label(app, text="Linn:", font=("Arial", 12)).pack(pady=5)

city_entry = tk.Entry(app, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(app, text="Saada ilm", font=("Arial", 12), command=get_weather).pack(pady=10)

weather_label = tk.Label(app, text="", font=("Arial", 12), justify="center")
weather_label.pack(pady=20)

app.mainloop()
