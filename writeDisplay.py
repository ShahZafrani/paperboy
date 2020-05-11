from waveshare_lib import epd7in5
import datetime
import time
from image import createClockImage


if __name__ == '__main__':
    try:
        epd = epd7in5.EPD()
        epd.init()
        epd.Clear()
        now = datetime.datetime.now()
        image = createClockImage(now)
        epd.display(epd.getbuffer(image))
        time.sleep(5)
        epd.sleep()
        exit()
    except KeyboardInterrupt:   
        print("keyboard-interrupt")
        epd.sleep()
        exit()
    except Exception as e:
        print(str(e))
        print("ERROR: check stacktrace above")
        epd.sleep()
        exit()