# Paperboy

*Paperboy all about that paper, boy*

E-ink clock in the style of FuzzyTime (Pebble fans know what I'm talking about).

![paperboy](.\images\paperboy.png)

## how to use:

1. make sure all dependencies are installe2
2. insert your api-key into image.py
3. run image.py in debug mode (see flag at top), and verify that test.bmp is updating
4. connect your waveshare e-paper hat to your raspberryPi and run image.py with debug set to False
- you can run weather.py or fuzzytime.py individually to test them out
5. setup a service with system.d so it will run on startup [guide here](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

## coming soon:
- tests
- word of the day?


### acknowledgements

epidif.py and epd7in5.py are provided by Waveshare
Weather using OpenWeatherMap
Weather Icons using [FontAwesome](https://fontawesome.com/)