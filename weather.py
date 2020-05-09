import requests


def getWeather(cityname, apikey):  
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + cityname + "&appid=" + apikey
    weather_response = requests.get(url)
    return weather_response.status_code, weather_response.json()

def getIconCode(wjson):
    wlist = wjson.get('weather')
    icon = weather_icons.get(wlist[0].get('icon'))
    if icon is None:
        return broken
    else:
        return icon


def getTemp(wjson, centigrade=False):
    wmain = wjson.get('main')
    kelvin_temp = wmain.get('temp')
    return convertTemp(kelvin_temp, centigrade)


def convertTemp(k, centigrade):
    temp = k - 273.0
    if (centigrade == False):
        temp = (temp * 1.8) + 32
    return temp

broken = "\uf753"


weather_icons = {
    "01d" : u"\uf185",
    "02d" : u"\uf6c4",
    "03d" : u"\uf0c2",
    "04d" : u"\uf0c2",
    "09d" : u"\uf743",
    "10d" : u"\uf740",
    "11d" : u"\uf0e7",
    "13d" : u"\uf2dc",
    "50d" : u"\uf75f",
    "01n" : u"\uf186",
    "02n" : u"\uf6c3",
    "03n" : u"\uf6c3",
    "04n" : u"\uf6c3",
    "09n" : u"\uf73c",
    "10n" : u"\uf73c",
    "11n" : u"\uf0e7",
    "13n" : u"\uf2dc",
    "50n" : u"\uf75f"
}

if __name__ == '__main__':
    cityname = "atlanta"
    apikey = "51eaa17d4260ee5567ea2e6468010e2e"
    status, wjson = getWeather(cityname, apikey)
    print("status: {}".format(status))
    print(wjson)
    print(getTemp(wjson))
    print("temp test: {} === {}".format(convertTemp(233, False), convertTemp(233, True)))

# openweather api reference
# 01d clear sky
# 02d few clouds
# 03d scattered clouds
# 04d broken clouds
# 09d shower rain
# 10d rain
# 11d thunderstorm
# 13d snow
# 50d mist 
# 01n clear sky (night)
# 02n few clouds (night)
# 03n scattered clouds (night)
# 04n broken clouds (night)
# 09n shower rain (night)
# 10n rain  (night)
# 11n thunderstorm (night)
# 13n snow (night)
# 50n mist  (night)
