cityname = "atlanta"
# TODO: extract this key to a gitignored secrets file
openweather_apikey = "GET_YOUR_OWN_KEY"

fontfile = './fonts/Roboto-Medium.ttf'
datefontfile = './fonts/Roboto-Medium.ttf'
moonfontfile = './fonts/moon-phases-font/moon_phases.ttf'
# TODO: find a way to only set this in one place, instead of matching it to the systemd timer trigger
offset = 3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
import time
from util import moonphase
from util import fuzzytime
from util import csv_util

EPD_WIDTH = 800
EPD_HEIGHT = 480
TEXT_FONT_SIZE = 36
TEXT_OFFSET = 8
DATE_FONT_SIZE = 24
BOUNDS_LEFT = 480
BOUNDS_TOP = 30
TIME_OFFSET = 50

DATE_BOUNDS_TOP = 440
DATE_BOUNDS_LEFT = 660

MOON_BOUNDS_TOP = 40
MOON_BOUNDS_LEFT = 50
MOON_FONT_SIZE = 384


# TODO: parameterize weather and time/date text
def createImage(now):
    # time    
    # timetext = fuzzytime.getTime(offset, now)
    datetext = "{}/{}/{}".format(now.month, now.day, now.year)
    filepath = csv_util.get_file_path(now, "augusta")
    today_times = csv_util.get_salat_times(now.day, filepath)

    # image setup
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontfile, TEXT_FONT_SIZE)
    datefont = ImageFont.truetype(datefontfile, DATE_FONT_SIZE)
    moonfont = ImageFont.truetype(moonfontfile, MOON_FONT_SIZE)
    # image draw
    text = "fajr {}\n duhr {}\n asr {}\n maghrib {}\n isha {}".format(today_times[1], today_times[3], today_times[4], today_times[5], today_times[6])
    draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), text, fill=0, font=font, anchor=None, spacing=TIME_OFFSET, align="right")
    # draw.text((BOUNDS_LEFT, BOUNDS_TOP), "fajr {}".format(today_times[1]), fill=0, font=font, direction="rtl")
    # draw.text((BOUNDS_LEFT, BOUNDS_TOP + TIME_OFFSET), "duhr {}".format(today_times[3]), fill=0, font=font, direction="rtl")
    # draw.text((BOUNDS_LEFT, BOUNDS_TOP + TIME_OFFSET*2), "asr {}".format(today_times[4]), fill=0, font=font, direction="rtl")
    # draw.text((BOUNDS_LEFT, BOUNDS_TOP + TIME_OFFSET*3), "maghrib {}".format(today_times[5]), fill=0, font=font, direction="rtl")
    # draw.text((BOUNDS_LEFT, BOUNDS_TOP + TIME_OFFSET*4), "isha {}".format(today_times[6]), fill=0, font=font, direction="rtl")
    
    draw.text((DATE_BOUNDS_LEFT, DATE_BOUNDS_TOP), datetext, fill=0, font=datefont)

    draw.text((MOON_BOUNDS_LEFT, MOON_BOUNDS_TOP), moonphase.getMoonPhaseChar(now), fill=0, font=moonfont)
    # draw.ellipse((40, 40, 400, 400), fill = 0, outline =0)
    return image

if __name__ == '__main__':
        nowImage = createImage(datetime.datetime.now())
        nowImage.save('./images/now.bmp')
