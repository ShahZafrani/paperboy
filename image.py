import epd7in5
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import fuzzytime
# import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    print("1")
    epd = epd7in5.EPD()
    print("2")
    epd.init()
    print("epd init complete")
    line1, line2, line3 = fuzzytime.updateTime(0)
    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 72)
    # draw.rectangle((0, 6, 640, 30), fill = 0)
    draw.text((60, 80), line1, font = font, fill = 0)
    draw.text((60, 160), line2, font = font, fill = 0)
    draw.text((60, 240), line3, font = font, fill = 0)
    # draw.rectangle((200, 80, 600, 280), fill = 0)
    # draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    # draw.rectangle((0, 80, 160, 280), fill = 255)
    # draw.arc((40, 80, 180, 220), 0, 360, fill = 0)
    epd.display_frame(epd.get_frame_buffer(image))
    

    # image = Image.open('bmp/ayah2.bmp')
    # print("1")
    # epd.display_frame(epd.get_frame_buffer(image))
    # print("1")
    
    return True

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)

if __name__ == '__main__':
    main()
    #image = Image.open('bmp/ayah2.bmp')
