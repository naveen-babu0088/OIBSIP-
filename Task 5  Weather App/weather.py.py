import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Replace with your OpenWeatherMap API key
API_KEY = "paste_your_actual_key_here"


class WeatherApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("700x650")
        self.root.resizable(False, False)

        self.unit = "metric"

        title = tk.Label(
            root,
            text="Weather Forecast Application",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=10)

        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        self.city_entry = tk.Entry(
            input_frame,
            width=25,
            font=("Arial", 12)
        )
        self.city_entry.grid(row=0, column=0, padx=5)

        search_btn = tk.Button(
            input_frame,
            text="Search",
            command=self.get_weather
        )
        search_btn.grid(row=0, column=1, padx=5)

        self.unit_var = tk.StringVar(value="Celsius")

        unit_menu = ttk.Combobox(
            input_frame,
            textvariable=self.unit_var,
            values=["Celsius", "Fahrenheit"],
            state="readonly",
            width=12
        )
        unit_menu.grid(row=0, column=2, padx=5)

        self.weather_info = tk.Label(
            root,
            text="Enter a city and click Search",
            font=("Arial", 11),
            justify="left",
            anchor="w"
        )
        self.weather_info.pack(pady=10)

        forecast_title = tk.Label(
            root,
            text="Forecast",
            font=("Arial", 15, "bold")
        )
        forecast_title.pack()

        self.forecast_box = tk.Text(
            root,
            height=18,
            width=80
        )
        self.forecast_box.pack(pady=10)

    def get_weather(self):

        city = self.city_entry.get().strip()

        if not city:
            messagebox.showerror(
                "Error",
                "Please enter a city name"
            )
            return

        self.unit = (
            "metric"
            if self.unit_var.get() == "Celsius"
            else "imperial"
        )

        weather_url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units={self.unit}"
        )

        forecast_url = (
            f"https://api.openweathermap.org/data/2.5/forecast"
            f"?q={city}&appid={API_KEY}&units={self.unit}"
        )

        try:
            weather_response = requests.get(weather_url, timeout=10)
            weather_data = weather_response.json()

            if str(weather_data.get("cod")) != "200":
                messagebox.showerror(
                    "Error",
                    weather_data.get("message", "City not found")
                )
                return

            self.display_current_weather(weather_data)

            forecast_response = requests.get(forecast_url, timeout=10)
            forecast_data = forecast_response.json()

            self.display_forecast(forecast_data)

        except requests.exceptions.ConnectionError:
            messagebox.showerror(
                "Error",
                "No internet connection."
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def display_current_weather(self, data):

        unit_symbol = (
            "°C"
            if self.unit == "metric"
            else "°F"
        )

        weather_description = (
            data["weather"][0]["description"]
            .title()
        )

        icon_code = data["weather"][0]["icon"]

        icon_url = (
            f"https://openweathermap.org/img/wn/"
            f"{icon_code}@2x.png"
        )

        text = (
            f"City: {data['name']}\n"
            f"Country: {data['sys']['country']}\n"
            f"Temperature: {data['main']['temp']}{unit_symbol}\n"
            f"Feels Like: {data['main']['feels_like']}{unit_symbol}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Pressure: {data['main']['pressure']} hPa\n"
            f"Wind Speed: {data['wind']['speed']}\n"
            f"Condition: {weather_description}\n\n"
            f"Weather Icon URL:\n{icon_url}"
        )

        self.weather_info.config(text=text)

    def display_forecast(self, data):

        self.forecast_box.delete("1.0", tk.END)

        if str(data.get("cod")) != "200":
            self.forecast_box.insert(
                tk.END,
                "Forecast data unavailable."
            )
            return

        unit_symbol = (
            "°C"
            if self.unit == "metric"
            else "°F"
        )

        self.forecast_box.insert(
            tk.END,
            "Upcoming Forecast\n"
            + "=" * 50 + "\n\n"
        )

        for item in data["list"][:10]:

            date_time = item["dt_txt"]
            temp = item["main"]["temp"]
            humidity = item["main"]["humidity"]
            weather = item["weather"][0]["description"].title()

            self.forecast_box.insert(
                tk.END,
                f"Date & Time: {date_time}\n"
                f"Temperature: {temp}{unit_symbol}\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {weather}\n"
                + "-" * 50 + "\n"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()