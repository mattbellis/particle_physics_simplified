import numpy as np
import matplotlib.pylab as plt

import sys

import hep_tools as hep

infile = sys.argv[1]

collisions = hep.get_collisions(infile,experiment='CMS',verbose=True)
print(len(collisions), " collisions")

energies = []
for entry, collision in enumerate(collisions):
    if entry%10000 == 0:
        print(entry)

    jets = collision['jets']
    
    for jet in jets:
        e = jet['e']
        #print(e)

        energies.append(e)


plt.figure()
plt.hist(energies,bins=50,range=(0,500))

plt.show()
    




