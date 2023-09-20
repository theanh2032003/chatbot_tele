import requests
import json
import datetime
from geopy.geocoders import Nominatim

def weather(text):
   # https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
    # url = 'http://api.openweathermap.org/data/2.5/weather?'
    # city_name = text
    # if not city_name:
    #     pass
    # api_key = "fe8d8c65cf345889139d8e545f57819a"
    # call_url = url + "appid=" + api_key + "&q=" + city_name
    
    geolocator = Nominatim(user_agent="my_application")

    # Lấy thông tin vị trí của địa điểm
    location = geolocator.geocode(text)
    base_url = "http://api.openweathermap.org/data/3.0/onecall?"

    # Tọa độ của vị trí bạn muốn lấy thông tin thời tiết
    lat = str(location.latitude)
    lon = str(location.longitude)

    # Khóa API của bạn
    # api_key = "fe8d8c65cf345889139d8e545f57819a"
    api_key = "baa9836372d89099b39df87393ae2fed"
    # Cập nhật URL với tọa độ và khóa API
    call_url = base_url + "lat=" + lat + "&lon=" + lon + "&exclude=current,minutely,hourly,alerts&appid=" + api_key
    
    response = requests.get(call_url)
    data = response.json()
    # print(data)
    # for key in data:{
    # print(key,":", data[key])
    # }
    # if data['cod'] != '404' :
    #     city_rest = data['main']
    #     current_temp = city_rest['temp']
    #     current_pressure = city_rest['pressure']
    #     current_humidity = city_rest['humidity']
    #     sun_time = data['sys']
    #     sun_rise = datetime.datetime.fromtimestamp(sun_time['sunrise'])
    #     sun_set = datetime.datetime.fromtimestamp(sun_time['sunset'])
    #     weather = data['weather']
    #     weather_des = weather[0]['description']
    #     now = datetime.datetime.now()
    #     content = """
    #     Hôm nay ngày {day} tháng {month} năm {year}
    #     Mặt trời mọc vào {hourrise} giờ {minrise} phút
    #     Mặt trời lặn vào {hourset} giờ {minset} phút
    #     Nhiệt độ trung bình là {temp} độ C
    #     Áp suất không khí là {pressure} héc tơ Pascal
    #     Độ ẩm là {humidity}%
    #     {description}
    #     """.format(day=now.day, month = now.month, year = now.year,
    #               hourrise = sun_rise.hour, minrise = sun_rise.minute,
    #               hourset = sun_set.hour, minset = sun_set.minute,
    #               temp=current_temp, pressure = current_pressure, humidity=current_humidity, description=weather_des)
    #     return content
    # else:
    #     return "Không tìm thấy thành phố"
    
    if data:
    # Lấy thông tin dự báo hàng ngày
        daily_forecasts = data["daily"]
        content=""
    # In thông tin dự báo cho mỗi ngày
        for day in daily_forecasts:
            date = datetime.datetime.fromtimestamp(day['dt'])
            formatted_date = date.strftime('%d/%m/%Y')
            temperature = day["temp"]["day"]-273.15
            humidity = day["humidity"]
            wind_speed = day["wind_speed"]
            pressure = day["pressure"]
            weather_description = day["weather"][0]["description"]
            content += """
            Ngày {date}:
            Nhiệt độ: {temperature} K
            Độ ẩm: {humidity}%
            Tốc độ gió: {wind_speed} m/s
            Áp suất: {pressure} hPa
            Mô tả thời tiết: {weather_description}""".format(date=formatted_date,temperature=round(temperature),humidity=humidity,wind_speed=wind_speed,
                                                             pressure=pressure,weather_description=weather_description)
        return content
    else:
        print("No data found!")


print(weather("Hà Nội"))