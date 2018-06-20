import numpy as np
import matplotlib.pylab as plt

import sys

import pps_tools as hep

infile = sys.argv[1]

alldata = hep.get_all_data(infile,verbose=False)
#print(len(collisions), " collisions")

energies = []

nentries = hep.get_number_of_entries(alldata)
print('Number of entries: {0}'.format(nentries))

for entry in range(nentries):

    collision = hep.get_collision(alldata,entry_number=entry,experiment='CMS')

    if entry%10000 == 0:
        print(entry)

    jets = collision['jets']
    photons = collision['photons']
    print(len(photons))
    
    for jet in jets:
        e = jet['e']
        #print(e)

        energies.append(e)


plt.figure()
plt.hist(energies,bins=50,range=(0,500))

plt.show()
    




