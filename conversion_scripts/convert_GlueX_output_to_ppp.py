import sys
from collections import OrderedDict


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

h5hep.create_group(data,'vertex',counter='nvertex')
h5hep.create_dataset(data,['vx','vy','vz'],group='vertex',dtype=float)

h5hep.create_group(data,'chargedTrack_0',counter='nchargedTrack_0')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_0',dtype=float)
h5hep.create_group(data,'chargedTrack_1',counter='nchargedTrack_1')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_1',dtype=float)
h5hep.create_group(data,'chargedTrack_2',counter='nchargedTrack_2')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_2',dtype=float)
h5hep.create_group(data,'chargedTrack_3',counter='nchargedTrack_3')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_3',dtype=float)
h5hep.create_group(data,'chargedTrack_4',counter='nchargedTrack_4')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_4',dtype=float)
h5hep.create_group(data,'chargedTrack_5',counter='nchargedTrack_5')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_5',dtype=float)
h5hep.create_group(data,'chargedTrack_6',counter='nchargedTrack_6')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_6',dtype=float)
h5hep.create_group(data,'chargedTrack_7',counter='nchargedTrack_7')
h5hep.create_dataset(data,['candidateId','px','py','pz'],group='chargedTrack_7',dtype=float)

event = h5hep.create_single_event(data)
#print(event.keys())
#print(event)

infilename = sys.argv[1]
infile = open(infilename)

xml = infile.read()

d = xmltodict.parse(xml)

a = d['HDDM'] 

events = a['reconstructedPhysicsEvent']

ptypes = {"Positron":'0', "Pi+":'1', "K+":"2", "Proton":"3",
          "Electron":'4', "Pi-":'5', "K-":"6", "AntiProton":"7"}

for hddmevent in events:

    h5hep.clear_event(event)

    #print("Event keys:  ")
    #print(hddmevent.keys())

    ncharged_tracks = [[], [], [], [], [], [], [], []]

    if 'reaction' in hddmevent.keys():
        reaction = hddmevent['reaction']
        #print(reaction.keys())
        if 'vertex' in reaction.keys():
            vertex = reaction['vertex']
            if type(vertex) is not OrderedDict:
                continue
            #print(vertex)
            #print(vertex.keys())
            #print(vertex['origin'].keys())
            event['vertex/vx'].append(float(vertex['origin']['@vx']))
            event['vertex/vy'].append(float(vertex['origin']['@vy']))
            event['vertex/vz'].append(float(vertex['origin']['@vz']))

    if 'chargedTrack' in hddmevent.keys():
        tracks = hddmevent['chargedTrack']
        #print(len(tracks))
        for track in tracks:
            #print(track.keys())
            if type(track) is not OrderedDict:
                continue
            ptype = track['@ptype']
            #print(ptype)

            which_charged_track_hypothesis = f"chargedTrack_{ptypes[ptype]}"

            #print(int(track['@candidateId'])-1)
            #print(int(ptypes[ptype]))
            ncharged_tracks[int(ptypes[ptype])].append(int(track['@candidateId'])-1)

            event[which_charged_track_hypothesis+'/candidateId'].append(int(track['@candidateId']))
            event[which_charged_track_hypothesis+'/px'].append(float(track['trackFit']['@px']))
            event[which_charged_track_hypothesis+'/py'].append(float(track['trackFit']['@py']))
            event[which_charged_track_hypothesis+'/pz'].append(float(track['trackFit']['@pz']))

    for i in range(len(ncharged_tracks)):
        if len(ncharged_tracks[i])>0:
            which_charged_track_hypothesis = f"chargedTrack_{i}"
            #print(ncharged_tracks)
            event[which_charged_track_hypothesis+'/n'+which_charged_track_hypothesis] = max(ncharged_tracks[i])+1

    h5hep.pack(data,event)

h5hep.write_to_file('test.h5',data,comp_type='gzip')





