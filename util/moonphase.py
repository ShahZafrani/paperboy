from . import pyorbital_moon_phase
import string 
import datetime

fullThreshold = 0.985
newThreshold = 0.015

waxing_phase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
waning_phase_chars = ['z', 'y', 'x', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']

def getMoonPhase(now):
    currentPosition = pyorbital_moon_phase.moon_phase(now)
    if currentPosition >= fullThreshold:
        return "0", "full moon"
    if currentPosition <= newThreshold:
        return "1", "new moon"
    yesterdayPosition = pyorbital_moon_phase.moon_phase(now - datetime.timedelta(days=1))
    if (yesterdayPosition >= currentPosition):
        direction = "waning"
        char_pos = int (round(currentPosition * len(waning_phase_chars)))
        if (char_pos == len(waning_phase_chars)):
            char_pos -=1
        char = waning_phase_chars[char_pos]
    elif (yesterdayPosition < currentPosition):
        direction = "waxing"
        char_pos = int (round(currentPosition * len(waxing_phase_chars)))
        if (char_pos == len(waxing_phase_chars)):
            char_pos -=1
        char = waxing_phase_chars[char_pos]
    if (char == "g"):
        phase_text = "first quarter"
    elif (char == "t"):
        phase_text = "last quarter"
    elif (currentPosition < 0.50):
        phase_text = direction + " crescent"
    else:
        phase_text = direction + " gibbous"
    return char, phase_text
    
    
