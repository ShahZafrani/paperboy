fontfile = './fonts/Roboto-Medium.ttf'
offset = 3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
import time
from util import fuzzytime

EPD_WIDTH = 640
EPD_HEIGHT = 384
TEXT_FONT_SIZE = 138
TEXT_OFFSET = 8
BOUNDS_LEFT = 0
BOUNDS_TOP = 30


# TODO: parameterize weather and time/date text
def createClockImage(now):
    # time    
    timetext = fuzzytime.getTime(offset, now)
    # datetext = fuzzytime.getDate(now)

    # image setup
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontfile, TEXT_FONT_SIZE)
    # image draw
    draw.multiline_text((BOUNDS_LEFT, BOUNDS_TOP), timetext, fill=0, font=font, anchor=None, spacing=0, align="left")
    return image

if __name__ == '__main__':
        # tuesday september twentyseventh,twenty twenty two is the longest date string in the near future
        # twentyfive to twelve is the longest time string in a day
        longImage = createClockImage(datetime.datetime.fromtimestamp(1664292930))
        longImage.save('./images/long.bmp')
        nowImage = createClockImage(datetime.datetime.now())
        nowImage.save('./images/now.bmp')
