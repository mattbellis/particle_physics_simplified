import sys

# First dump the XML with something like....

# hddm-xml -n 10 -o this particle_gun012_001_rest.hddm

# Got this
# https://github.com/martinblech/xmltodict
# And to use it
# https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
import xmltodict

import numpy as np

import h5hep

data = h5hep.initialize()

h5hep.create_group(data,'startHit',counter='nstartHit')
h5hep.create_dataset(data,['dE','time'],group='startHit',dtype=float)
h5hep.create_dataset(data,['sector'],group='startHit',dtype=int)

h5hep.create_group(data,'chargedTrack_1',counter='nchargedTrack_1')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_1',dtype=float)
h5hep.create_group(data,'chargedTrack_2',counter='nchargedTrack_2')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_2',dtype=float)
h5hep.create_group(data,'chargedTrack_3',counter='nchargedTrack_3')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_3',dtype=float)
h5hep.create_group(data,'chargedTrack_4',counter='nchargedTrack_4')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_4',dtype=float)

event = h5hep.create_single_event(data)
print(event.keys())
print(event)

infilename = sys.argv[1]
infile = open(infilename)

xml = infile.read()

d = xmltodict.parse(xml)

a = d['HDDM'] 

events = a['reconstructedPhysicsEvent']
for hddmevent in events:

    h5hep.clear_event(event)

    print("Event keys:  ")
    print(hddmevent.keys())
    if 'chargedTrack' in hddmevent.keys():
        tracks = hddmevent['chargedTrack']
        print(len(tracks))
        for track in tracks:
            print(track.keys())
            print(track['@ptype'])

            event['chargedTrack_1/candidateId'].append(track['@candidateId'])


