cityname = "atlanta"
openweather_apikey = "GET_YOUR_OWN_KEY"

fontfile = './fonts/JandaManateeSolid.ttf'
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
# import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384
TEXT_FONT_SIZE = 72
TEXT_OFFSET = 8
WEATHER_ICON_SIZE = 144
BOUNDS_LEFT = 30
BOUNDS_TOP = 30

WBOUNDS_LEFT = 450
WBOUNDS_TOP = 40
TEMPBOUNDS_LEFT = 480
TEMPBOUNDS_TOP = 190

def draw_clock(): 
    now = datetime.datetime.now()
    weather_response_code, weather_json = weather.getWeather(cityname, openweather_apikey)
    if (weather_response_code == 200):
        weather_icon = weather.getIconCode(weather_json)
        weather_temp = str(int(round(weather.getTemp(weather_json))))
    else: 
        weather_icon = weather.broken
        weather_temp = "gg"
    line1, line2, line3 = fuzzytime.updateTime(offset, now)
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
    wfont = ImageFont.truetype(weatherfontfile, WEATHER_ICON_SIZE)

    if (debug == False):  
        draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), line1 + "\n  " + line2 + "\n    " + line3, fill=0, font=font, anchor=None, spacing=0, align="left")
    else:  
        draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), "twentyfive" + "\n  " + line2 + "\n    " + line3, fill=0, font=font, anchor=None, spacing=0, align="left")
    draw.text((WBOUNDS_LEFT, WBOUNDS_TOP), weather_icon, font = wfont, fill = 0)
    draw.text((TEMPBOUNDS_LEFT, TEMPBOUNDS_TOP), weather_temp, font = font, fill = 0)
    if debug == False:
        epd.display_frame(epd.get_frame_buffer(image))
    else:
        image.save('./images/test.bmp')

def main():
    if debug == False:
        while True:
            # draw
            draw_clock()
            # only redraw after 5 minutes
            time.sleep(300)
    else:
        draw_clock()



if __name__ == '__main__':
    main()
