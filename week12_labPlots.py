#making a plot: by Kay Towner

import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
import pandas as pd
import math

stars = pd.read_csv('g_stars.csv')

lumin = pd.DataFrame(stars, columns=['logL'])
age = pd.DataFrame(stars, columns=['logAge'])

#PLOTTING:
fig, axs = plt.subplots(2)
fig.suptitle('G-stars')
fig.patch.set_facecolor('xkcd:light grey')

axs[0].plot(lumin, color='firebrick', label='Luminocity of Star')
axs[1].plot(age, color='olive', label='Age of Star')
plt.legend(loc='best')

for ax in axs.flat:
    ax.set(xlabel='log', ylabel='log') #the x and y values, but I can't tell what they are

plt.show()
plt.savefig('G-starGraph_KayTowner.png')
