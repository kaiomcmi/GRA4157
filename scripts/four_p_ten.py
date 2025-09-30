"""
Input arguements for v0 and t through the command line
"""

import sys

v0 = float(sys.argv[1])
G = 9.81
t = float(sys.argv[2])
y = v0 * t - 0.5 * G * t**2
print(y)
