"""
Maps an image of STEVE (the thin band). Reproduced from 
http://themis.igpp.ucla.edu/nuggets/nuggets_2018/Gallardo-Lacourt/fig2.jpg
"""

from datetime import datetime

import matplotlib.pyplot as plt

import asilib

ax = asilib.make_map(lon_bounds=(-127, -100), lat_bounds=(45, 65))

image_time, image, skymap, ax, p = asilib.plot_map(
    'THEMIS', 'ATHA', datetime(2010, 4, 5, 6, 7, 0), 110, ax=ax
)
plt.tight_layout()
plt.show()
