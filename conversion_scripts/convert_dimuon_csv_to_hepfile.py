import numpy as np
import matplotlib.pylab as plt

import hepfile

import sys

infilename = sys.argv[1]

outfilename = infilename.split('.')[0] + "_hepfile.h5"

data = np.loadtxt(infilename,dtype=float,unpack=True,delimiter=',')

e1 = data[0]
px1 = data[1]
pz1 = data[2]
py1 = data[3]
q1 =  data[4].astype(int)

e2 = data[5]
px2 = data[6]
pz2 = data[7]
py2 = data[8]
q2 =  data[9].astype(int)

################################################################################
data = hepfile.initialize()

hepfile.create_group(data,'muon1',counter='nmuon1')
hepfile.create_dataset(data,['e','px','py','pz'],group='muon1',dtype=float)
hepfile.create_dataset(data,['q'],group='muon1',dtype=int)

hepfile.create_group(data,'muon2',counter='nmuon2')
hepfile.create_dataset(data,['e','px','py','pz'],group='muon2',dtype=float)
hepfile.create_dataset(data,['q'],group='muon2',dtype=int)

event = hepfile.create_single_bucket(data)
################################################################################


################################################################################
nevents = len(e1)

for i in range(nevents):
    event['muon1/e'].append(e1[i])
    event['muon1/px'].append(px1[i])
    event['muon1/py'].append(py1[i])
    event['muon1/pz'].append(pz1[i])
    event['muon1/q'].append(q1[i])

    event['muon2/e'].append(e2[i])
    event['muon2/px'].append(px2[i])
    event['muon2/py'].append(py2[i])
    event['muon2/pz'].append(pz2[i])
    event['muon2/q'].append(q2[i])

    return_value = hepfile.pack(data,event,STRICT_CHECKING=True)
    if return_value != 0:
        exit()
################################################################################

print(f"Writing the file...{outfilename}")
hdfile = hepfile.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9,verbose=True)



