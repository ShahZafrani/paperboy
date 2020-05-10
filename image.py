cityname = "atlanta"
openweather_apikey = "GET_YOUR_OWN_KEY"

fontfile = './fonts/Roboto-Medium.ttf'
datefontfile = './fonts/Roboto-MediumItalic.ttf'
weatherfontfile = './fonts/Font Awesome 5 Free-Solid-900.otf'
offset = 3
debug = False

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
import time
import fuzzytime
import weather

if debug == False:
    import epd7in5
# import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384
TEXT_FONT_SIZE = 84
TEXT_OFFSET = 8
DATE_FONT_SIZE = 24
WEATHER_ICON_SIZE = 144
BOUNDS_LEFT = 30
BOUNDS_TOP = 30

DATE_BOUNDS_TOP = 358
DATE_BOUNDS_LEFT = 62

WBOUNDS_LEFT = 450
WBOUNDS_TOP = 40
TEMPBOUNDS_LEFT = 480
TEMPBOUNDS_TOP = 190

def draw_clock(now): 
    weather_response_code, weather_json = weather.getWeather(cityname, openweather_apikey)
    if (weather_response_code == 200):
        weather_icon = weather.getIconCode(weather_json)
        weather_temp = str(int(round(weather.getTemp(weather_json)))) + u"\u00B0"
    else: 
        weather_icon = weather.broken
        weather_temp = "gg"
    line1, line2, line3 = fuzzytime.updateTime(offset, now)
    datetext = fuzzytime.getDate(now)
    if debug == False:
        epd = epd7in5.EPD()
        epd.init()
        print("epd init complete")
    else: 
        print(line1)
        print(line2)
        print(line3)
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontfile, TEXT_FONT_SIZE)
    datefont = ImageFont.truetype(datefontfile, DATE_FONT_SIZE)
    wfont = ImageFont.truetype(weatherfontfile, WEATHER_ICON_SIZE)

    if (debug == False):  
        draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), line1 + "\n  " + line2 + "\n    " + line3, fill=0, font=font, anchor=None, spacing=0, align="left")
        draw.text((DATE_BOUNDS_LEFT, DATE_BOUNDS_TOP), datetext, fill=0, font=datefont)
    else:  
        draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), "twentyfive" + "\n  " + line2 + "\n    " + line3, fill=0, font=font, anchor=None, spacing=0, align="left")
        draw.text((DATE_BOUNDS_LEFT, DATE_BOUNDS_TOP), "September Twentyseventh, Twenty Twenty", fill=0, font=datefont)
    draw.text((WBOUNDS_LEFT, WBOUNDS_TOP), weather_icon, font = wfont, fill = 0)
    draw.text((TEMPBOUNDS_LEFT, TEMPBOUNDS_TOP), weather_temp, font = font, fill = 0)
    if debug == False:
        epd.display_frame(epd.get_frame_buffer(image))
    else:
        image.save('./images/test.bmp')

def main():
    if debug == False:
        lastMinuteText = "forever"
        while True:
            now = datetime.datetime.now()
            minuteText = fuzzytime.updateTime(offset, now)[0]
            if (minuteText != lastMinuteText):
                lastMinuteText = minuteText
                # draw
                draw_clock(now)
            # check for a re-draw every minute, after the offset is reached, this should only trigger every five minutes
            time.sleep(60)
    else:
        draw_clock(datetime.datetime.now())



if __name__ == '__main__':
    main()
