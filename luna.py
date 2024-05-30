#!usr/bin/env python3

'''
https://rhodesmill.org/skyfield/examples.html#what-phase-is-the-moon-tonight    
'''

from skyfield.api import load
from skyfield.framelib import ecliptic_frame
from datetime import datetime

planets = load('de421.bsp')
earth, sun, luna = planets['earth'], planets['sun'], planets['moon']


ts = load.timescale()
t = ts.now()
now = datetime.now()

e = earth.at(t)
m = e.observe(luna).apparent()
s = e.observe(sun).apparent()

_, slon, _ = s.frame_latlon(ecliptic_frame)
_, mlon, _ = m.frame_latlon(ecliptic_frame)
# 0 - 360
# 170 - 190 is Full
phase = (mlon.degrees - slon.degrees) % 360.0

percent = 100.0 * m.fraction_illuminated(sun)


print(now)
print(f"Phase: {phase:.1f}")
print(f"Illuminated: {percent:.1f}%")

