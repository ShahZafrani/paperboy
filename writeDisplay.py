# from waveshare_lib import epd7in5
from waveshare_lib import epd7in5v2
import datetime
import time
from image import createImage


if __name__ == '__main__':
    try:
        # epd = epd7in5.EPD()
        epd = epd7in5v2.EPD()
        epd.init()
        now = datetime.datetime.now()
        image = createImage(now)
        epd.display(epd.getbuffer(image))
        time.sleep(5)
        epd.sleep()
        epd.Dev_exit()
        exit()
    except KeyboardInterrupt:   
        print("keyboard-interrupt")
        epd7in5v2.epdconfig.module_exit()
        exit()
    except Exception as e:
        print(str(e))
        print("ERROR: check stacktrace above")
        epd.sleep()
        epd7in5v2.epdconfig.module_exit()
        exit()
