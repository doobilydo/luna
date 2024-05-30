#!usr/bin/env python3

'''
Get the current Moon phase, age, and consetllation it's in.'
'''
# https://rhodesmill.org/skyfield/examples.html#what-phase-is-the-moon-tonight
from datetime import datetime
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from skyfield.api import position_of_radec, load_constellation_map
from skyfield.api import load_constellation_names
import os
from time import sleep
import locale

# My library.
import sunrise

version = "0.0.2"
city = "timbuktu" # Hardcoded. Change city as needed.

def getLunarInfo():
    # Create a timescale and ask the current time.
    ts = load.timescale()
    t = ts.now()
    current_dateTime = datetime.now()
    
    #_sunrise, _sunset = sunrise.getSunrise(current_dateTime, city)

    eph = load("de421.bsp")
    sun, moon, earth = eph["sun"], eph["moon"], eph["earth"]

    e = earth.at(t)
    s = e.observe(sun).apparent()
    m = e.observe(moon).apparent()

    _, slon, _ = s.frame_latlon(ecliptic_frame)
    _, mlon, _ = m.frame_latlon(ecliptic_frame)
    phase = (mlon.degrees - slon.degrees) % 360.0

    percent = 100.0 * m.fraction_illuminated(sun)
    illuminated = "{0:.1f}%".format(percent)
    # lifespan = 27 # In days (Source: https://spaceplace.nasa.gov/moon-phases/en/)
    lifespan = 29.5 # In days (Source: https://aa.usno.navy.mil/faq/moon_phases)
    age = lifespan * (phase / 360)  # In days

    d = dict(load_constellation_names())
    constellation_at = load_constellation_map()

    '''
    Eliptic degree, Illumination

    0° and 360°, 0% = new
    90°, 50% = first quarter
    180°, 100% = full
    270°, 50% = last quarter
    '''
    
    # Moon phase based on its illumination *and* phase degree.
    if (0 < percent < 47 and phase < 180):
        phase_name = "Waxing Crescent"
    
    elif (47 <= percent <= 53 and phase < 180):
        phase_name = "First Quarter" # Approximately 50%.
        
    elif (percent < 97 and phase < 180):
        phase_name = "Waxing Gibbous"
        
    elif (97 <= percent <= 100): # Illumination only.
        phase_name = "Full"
        
    elif (53 <= percent < 97 and phase > 180):
        phase_name = "Waning Gibbous"
        
    elif (47 <= percent <= 53 and phase > 180):
        phase_name = "Last Quarter" # Approximately 50%.
        
    elif (0 < percent < 47 and phase > 180):
        phase_name = "Waning Crescent"
        
    elif (0 <= percent <= 3): # Illumination only.
        phase_name = "New"

    phase_name += " Moon"

    print(current_dateTime)
    print("Phase: {0:.1f}°,".format(phase), phase_name)
    print(f"Moon is {float(age):.1f} days old.")
    print(f"{illuminated} illuminated.")
    print(f"Moon is in constellation {d[constellation_at(m)]}.")
    print(f"(City: {city})")
    #print("Sunrise: ", _sunrise)
    #print("Sunset: ", _sunset)
    print(f"(Version: {version})")


def main():
    while True:
        # Clear screen.
        os.system("clear")
        
        getLunarInfo()
        sleep(300) # Sleep for 300 seconds (5 minutes).
    
# Start the application.
main()
