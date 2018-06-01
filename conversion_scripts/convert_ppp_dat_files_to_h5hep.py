import numpy as np
import sys
sys.path.append('../tools')
import h5hep 

import cms_tools as cms

def convert_cms(infilename):
    data = h5hep.initialize()

    h5hep.create_group(data,'jets',counter='njets')
    h5hep.create_dataset(data,['e','px','py','pz','btag'],group='jets',dtype=float)

    h5hep.create_group(data,'muons',counter='nmuons')
    h5hep.create_dataset(data,['e','px','py','pz','q'],group='muons',dtype=float)
    
    h5hep.create_group(data,'electrons',counter='nelectrons')
    h5hep.create_dataset(data,['e','px','py','pz','q'],group='electrons',dtype=float)
    
    h5hep.create_group(data,'photons',counter='nphotons')
    h5hep.create_dataset(data,['e','px','py','pz'],group='photons',dtype=float)
    
    h5hep.create_dataset(data,['METx','METy'],dtype=float)
    
    event = h5hep.create_single_event(data)

    collisions = cms.get_collisions_from_filename(infilename)

    #'''
    for collision in collisions:

        h5hep.clear_event(event)

        jets,muons,electrons,photons,met = collision

        event['jets/njets'] = len(jets)
        for jet in jets:
            event['jets/e'].append(jet[0])
            event['jets/px'].append(jet[1])
            event['jets/py'].append(jet[2])
            event['jets/pz'].append(jet[3])
            event['jets/btag'].append(jet[4])

        event['muons/nmuons'] = len(muons)
        for muon in muons:
            event['muons/e'].append(muon[0])
            event['muons/px'].append(muon[1])
            event['muons/py'].append(muon[2])
            event['muons/pz'].append(muon[3])
            event['muons/q'].append(muon[4])

        event['electrons/nelectrons'] = len(electrons)
        for electron in electrons:
            event['electrons/e'].append(electron[0])
            event['electrons/px'].append(electron[1])
            event['electrons/py'].append(electron[2])
            event['electrons/pz'].append(electron[3])
            event['electrons/q'].append(electron[4])

        event['photons/nphotons'] = len(photons)
        for photon in photons:
            event['photons/e'].append(photon[0])
            event['photons/px'].append(photon[1])
            event['photons/py'].append(photon[2])
            event['photons/pz'].append(photon[3])


        event['METx'] = met[0]
        event['METy'] = met[1]


        h5hep.pack(data,event)

    print("Writing the file...")
    outfilename = infilename.split('.')[0] + ".hdf5"
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    #'''

if __name__ == "__main__":
    infilename = sys.argv[1]
    convert_cms(infilename)

