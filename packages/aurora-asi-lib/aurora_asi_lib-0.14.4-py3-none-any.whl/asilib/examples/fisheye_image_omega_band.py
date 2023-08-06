"""
This example generates an image of an omega band aurora. This event was studied
in:

Liu, J., Lyons, L. R., Archer, W. E., Gallardo-Lacourt, B., Nishimura, Y., Zou,
Y., … Weygand, J. M. (2018). Flow shears at the poleward boundary of omega bands
observed during conjunctions of Swarm and THEMIS ASI. Geophysical Research Letters,
45, 1218– 1227. https://doi.org/10.1002/2017GL076485
"""

import matplotlib.pyplot as plt

import asilib

asi_array_code = 'THEMIS'
location_code = 'KAPU'
time = '2008-03-09T04:39:00'

asilib.plot_fisheye(asi_array_code, location_code, time)
plt.tight_layout()
plt.show()
