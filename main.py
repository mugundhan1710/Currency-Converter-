import tkinter as tk
import requests
def get_weather():
    city = entry_city.get()
    api_key = "82c30028723289e2e81bbfe6aa041e3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        api_result = requests.get(url)
        api_result.raise_for_status()
        data = api_result.json()

        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        weather = data['weather'][0]['main']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        result = f"City: {city_name}, {country}\n"
        result += f"Temperature: {temp} °C\n"
        result += f"Weather: {weather}\n"
        result += f"Humidity: {humidity}%\n"
        result += f"Wind Speed: {wind} m/s"

        label_result.config(text=result)

    except requests.exceptions.HTTPError:
        label_result.config(text="City not found. Please try again.")
    except Exception as e:
        label_result.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("WEATHER APP")
root.geometry("1000x1000")
root.configure(bg="orange")

label_title = tk.Label(root, text="Enter City Name:", font=("Comic Sans MS", 16), bg="white")
label_title.pack(pady=10)

entry_city = tk.Entry(root, font=("Comic Sans MS", 14))
entry_city.pack(pady=10)

btn_result = tk.Button(root, text="Get Weather", font=("Comic Sans MS", 12),
                       bg="white", fg="black", command=get_weather)
btn_result.pack(pady=18)

label_result = tk.Label(root, text="", font=("Comic Sans MS", 16),
                        bg="white", justify="center")
label_result.pack(pady=10)
root.mainloop()