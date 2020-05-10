cityname = "atlanta"
openweather_apikey = "GET_YOUR_OWN_KEY"

fontfile = './fonts/Roboto-Medium.ttf'
datefontfile = './fonts/Roboto-Medium.ttf'
weatherfontfile = './fonts/Font Awesome 5 Free-Solid-900.otf'
offset = 3
debug = True

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
import time
import fuzzytime
import weather

if debug == False:
    import epd7in5

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

def displayImage(image, epd=None):
    if debug == False:
        epd.display(epd.getbuffer(image))
    else:
        image.save('./images/test.bmp')

def createClockImage(now):
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
    timetext = fuzzytime.getTime(offset, now)
    datetext = fuzzytime.getDate(now)
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontfile, TEXT_FONT_SIZE)
    datefont = ImageFont.truetype(datefontfile, DATE_FONT_SIZE)
    wfont = ImageFont.truetype(weatherfontfile, WEATHER_ICON_SIZE)

    draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), timetext, fill=0, font=font, anchor=None, spacing=0, align="left")
    draw.text((DATE_BOUNDS_LEFT, DATE_BOUNDS_TOP), datetext, fill=0, font=datefont)
    draw.text((WBOUNDS_LEFT, WBOUNDS_TOP), weather_icon, font = wfont, fill = 0)
    draw.text((TEMPBOUNDS_LEFT, TEMPBOUNDS_TOP), weather_temp, font = font, fill = 0)
    return image


def main():
    if debug == False:
        try:
            epd = epd7in5.EPD()
            epd.init()
            epd.Clear()
            lastMinuteText = "forever"
            while True:
                now = datetime.datetime.now()
                minuteText = fuzzytime.getTime(offset, now)[0]
                if (minuteText != lastMinuteText):
                    lastMinuteText = minuteText
                    # draw
                    image = createClockImage(now)
                    displayImage(image, epd)
                # check for a re-draw every minute, after the offset is reached, this should only trigger every five minutes
                time.sleep(60)
        except KeyboardInterrupt:   
            print("keyboard-interrupt")
            epd7in5.epdconfig.module_exit()
            exit()
        except:
            print("ERROR: check potential stacktrace above")
            epd7in5.epdconfig.module_exit()
            exit()
    else:
        # tuesday september twentyseventh,twenty twenty two is the longest date string in the near future
        # twentyfive to twelve is the longest time string in a  day
        image = createClockImage(datetime.datetime.fromtimestamp(1664292930))
        # image = createClockImage(datetime.datetime.now())
        displayImage(image)



if __name__ == '__main__':
    main()
