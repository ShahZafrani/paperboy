from . import pyorbital_moon_phase
import string 
def getMoonPhaseChar(now):
    lowercase = list(string.ascii_lowercase)
    currentPosition = pyorbital_moon_phase.moon_phase(now)
    position_index = int(round(currentPosition * 26))
    if position_index == 26:
        position_index = 25
    return lowercase[position_index]