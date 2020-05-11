cityname = "atlanta"
# TODO: extract this key to a gitignored secrets file
openweather_apikey = "GET_YOUR_OWN_KEY"

fontfile = './fonts/Roboto-Medium.ttf'
datefontfile = './fonts/Roboto-Medium.ttf'
weatherfontfile = './fonts/Font Awesome 5 Free-Solid-900.otf'
# TODO: find a way to only set this in one place, instead of matching it to the systemd timer trigger
offset = 3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
import time
from util import fuzzytime
from util import weather

EPD_WIDTH = 640
EPD_HEIGHT = 384
TEXT_FONT_SIZE = 84
TEXT_OFFSET = 8
DATE_FONT_SIZE = 24
WEATHER_ICON_SIZE = 144
BOUNDS_LEFT = 30
BOUNDS_TOP = 30

DATE_BOUNDS_TOP = 354
DATE_BOUNDS_LEFT = 6

WBOUNDS_LEFT = 450
WBOUNDS_TOP = 40
TEMPBOUNDS_LEFT = 465
TEMPBOUNDS_TOP = 190


# TODO: parameterize weather and time/date text
def createClockImage(now):
    # weather
    try:
        weather_response_code, weather_json = weather.getWeather(cityname, openweather_apikey)
    except:
        print("error getting weather")
        weather_response_code = 9001
    if (weather_response_code == 200):
        weather_icon = weather.getIconCode(weather_json)
        weather_temp = str(int(round(weather.getTemp(weather_json)))) + u"\u00B0"
    else: 
        weather_icon = weather.broken
        weather_temp = "101"+ u"\u00B0"
    # time    
    timetext = fuzzytime.getTime(offset, now)
    datetext = fuzzytime.getDate(now)

    # image setup
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontfile, TEXT_FONT_SIZE)
    datefont = ImageFont.truetype(datefontfile, DATE_FONT_SIZE)
    wfont = ImageFont.truetype(weatherfontfile, WEATHER_ICON_SIZE)
    # image draw
    draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), timetext, fill=0, font=font, anchor=None, spacing=0, align="left")
    draw.text((DATE_BOUNDS_LEFT, DATE_BOUNDS_TOP), datetext, fill=0, font=datefont)
    draw.text((WBOUNDS_LEFT, WBOUNDS_TOP), weather_icon, font = wfont, fill = 0)
    draw.text((TEMPBOUNDS_LEFT, TEMPBOUNDS_TOP), weather_temp, font = font, fill = 0)
    return image

if __name__ == '__main__':
        # tuesday september twentyseventh,twenty twenty two is the longest date string in the near future
        # twentyfive to twelve is the longest time string in a day
        longImage = createClockImage(datetime.datetime.fromtimestamp(1664292930))
        longImage.save('./images/long.bmp')
        nowImage = createClockImage(datetime.datetime.now())
        nowImage.save('./images/now.bmp')
