#By: Kay Towner

import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

f = pd.read_csv('berger_2018_edited.txt', 'r', delimiter='|')
bins = f['Bin']


#print("Within the berger file there are:", len(f), "items.")
#24018072 <-- got this when I oppend the file with a different method

###rouph draft:
binary = []
nonbinary = []

tempnb = []
radnb = []

tempb = []
radb = []

for x in bins:
    if x == 0:
        binary.append(x)
        tempb.append(x)
        radb.append(x)
        
    else:
        nonbinary.append(x)
        tempnb.append(x)
        radnb.append(x)

#Plotting:
radii = radnb + radb 
temp = tempnb + tempb

plt.scatter(radii, temp)
plt.title('Binary vs. Nonbinary Stars')
plt.xlabel('radii')
plt.ylabel('Temperature')

plt.xlim()
plt.ylim()

plt.yscale('log')
plt.xscale('log')
plt.show


#FUNCTION

def Lumin(R,,T):
    """Function of Stefan Boltzmann Law
    Output: Luminosity of a star."""
    return 4*np.pi*R**2 T**4











