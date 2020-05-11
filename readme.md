# Paperboy

*Paperboy all about that paper, boy*

E-ink clock in the style of FuzzyTime (Pebble fans know what I'm talking about).

![paperboy](./images/paperboy.png)

## how to use:

1. make sure spi is enabled on your raspberry pi
2. make sure you have [Pillow](https://pillow.readthedocs.io/en/stable/) and [Requests](https://requests.readthedocs.io/en/master/) installed
3. insert your api-key into image.py
4. run image.py and verify that the bmp files in images look correct. Use this to develop on when customizing your display.
5. connect your waveshare e-paper hat to your raspberryPi and run writeDisplay.py
6. setup a service with systemd and a timer so that writeDisplay.py will run every 5 minutes. See ./systemd. [guide here](https://www.certdepot.net/rhel7-use-systemd-timers/)

## coming soon:
- tests
- word of the day?

## the journey:
- testing my image creation logic at first was cumbersome, so I set a debug flag that would allow me to output an image file instead of writing to the display. This also allowed me to work from a machine that isn't the raspberryPi
- though this is a hobby project, this is the closest I've come to writing python in a production setting. Tests and Exception handling are new to my in the python space. 
- SPI was not enabled by default when I loaded raspbian onto my pi, this took some searching to figure out
- The first night after I framed the clock, it stopped running at some point. After opening up the frame and connecting the pi to an hdmi display I decided to enable ssh and ssh in headless mode. This has saved me a lot of time when troubleshooting, and also decreases the risk of damaging the sensitive ribbon cable for the display..
- having a debug mode was cumbersome, so I refactored in order to separate the image creation and display writing
- After reading the [docs](https://www.waveshare.com/wiki/E-Paper_Driver_HAT) for the display driver, I noticed that it recommends to put the display into sleep mode between writes in order to avoid damaging the unit by leaving the 5v line open. Some refactoring was required to achieve this.
- I initially used time.sleep(300) in an endless while loop to achieve the 5 minute updates to the display. I have since switched to use systemd with timers. Sure it's more accurate, more reliable, and has logging built-in, but the real reason is cause it's an excuse to learn something new about linux.

## acknowledgements
- epidif.py and epd7in5.py are provided by [Waveshare](https://github.com/waveshare/e-Paper)
- Weather using OpenWeatherMap
- Weather Icons using [FontAwesome](https://fontawesome.com/)
