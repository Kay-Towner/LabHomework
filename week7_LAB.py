#By Kay Towner
#2/24/21
#week7 LAB

#3.) Coding Questions:
#1.
import csv
import matplotlib.pyplot as plt
import numpy as np

f = open("g_stars.csv","r")
reader = csv.reader(f)

#2.
for row in reader:
    logGlist = row([0])
f.close()

#3.
def lumins(x):
#4.
    """Function to convert the value to Solar
    Luminosity.
    """
    x = logGlist
    lumincalc = x * (3.828*10**26)
#5.
    return lumincalc  #(some kind of thing haha)

Lumins(logGlist)
print(Lumins)

#6.
logW = Lumins()

#7.
def logTe(y):

    return y
tempK = logTe()

#8.
x= tempK
y= logW
plt.plot(x,y)
plt.xlabel("temp")
plt.ylabel("Log")
plt.legend(x,y)
plt.show()
plt.save()

#9.
#equation:  Mact = m2/m1

#10.
def mass(m1, m2):
    """Function to find the secondary mass of the
    star
    """
#11.
    Mact = m2/m1
    secondmass = Mact/m1  
    return secondmass
#12.
masslist = mass()
print(masslist)

#13.
#equation: m - M = 5*np.log*d - 5
# d = parsecs

#14.
#rearanged: d = 10*((m-M+5)/5)

#15.
def distance(m, M):
    """function to calculate the distance
    """
    d = 10*((m-M+5)/5)
    return d

#16.
def distance(m, M):
    """function to calculate the distance
    """
    d = 10*((m-M+5)/5)
    meters = (3.086*10**16)
    dist = d * meters
    return dist

#17.

for row in reader:
    Av = row(['Av'])
f.close()

def distance(m, M, Av):
    """function to calculate the distance
    """
    d = 10*((m-M+5)/5)
    meters = (3.086*10**16)
    dist = d * meters
#18
    distwithAv = 10*((m-M+5)/5) + Av
#19
    return dist, distwithAv

#20.
distList = distance(dist)
distAvList = distance(distwithAv)


















