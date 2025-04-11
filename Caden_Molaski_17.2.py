# 17.2 Code Like Weather Data


data = {
    "coord": {
        "lon": -86.52,
        "lat": 39.17
    },
    "weather": {
            "id": 501,
            "main": "Rain",
            "description": "moderate rain",
            "icon": "10n"
    },
    "main": {
        "temp": 291.4,
        "feels_like": 292.42,
        "temp_min": 290.93,
        "temp_max": 292.15,
        "pressure": 1014,
        "humidity": 88
    },
    "wind": {
        "speed": 1.5,
        "deg": 150
    },
    "rain": {
        "1h": 1.02
    },
    "clouds": {
        "all": 75
    },
    "sys": {
        "type": 1,
        "id": 3471,
        "country": "US",
        "sunrise": 1590661414,
        "sunset": 1590714219
    }
}

print("\nWeather data options:")
for key, value in data.items():
    print(f"Key: {key}")
    if isinstance(value, dict): 
        print("Values:")
        for sub_key, sub_value in value.items():
            print(f"{sub_key} : {sub_value}")
    else:
        print(f"Value: {value}")
    print()

