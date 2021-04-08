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

axs[0].plot(lumin, color='firebrick', label='Luminocity')
axs[1].plot(age, color='olive', label='Age')

for ax in axs.flat:
    ax.set(xlabel='temp')

plt.show()
plt.savefig('G-starGraph_KayTowner.png')
