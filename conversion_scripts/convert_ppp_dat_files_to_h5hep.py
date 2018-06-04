import numpy as np
import sys
sys.path.append('../tools')
import h5hep 

import cms_tools as cms
import babar_tools as babar

################################################################################
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
################################################################################
################################################################################
def convert_babar(infilename):
    data = h5hep.initialize()

    h5hep.create_group(data,'pions',counter='npions')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='pions',dtype=float)

    h5hep.create_group(data,'kaons',counter='nkaons')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='kaons',dtype=float)

    h5hep.create_group(data,'protons',counter='nprotons')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='protons',dtype=float)

    h5hep.create_group(data,'muons',counter='nmuons')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='muons',dtype=float)
    
    h5hep.create_group(data,'electrons',counter='nelectrons')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='electrons',dtype=float)
    
    h5hep.create_group(data,'photons',counter='nphotons')
    h5hep.create_dataset(data,['e','px','py','pz'],group='photons',dtype=float)
    
    event = h5hep.create_single_event(data)

    collisions = babar.get_collisions(open(infilename))

    #'''
    for collision in collisions:

        h5hep.clear_event(event)

        pions,kaons,protons,muons,electrons,photons = collision

        event['pions/npions'] = len(pions)
        for pion in pions:
            event['pions/e'].append(pion[0])
            event['pions/px'].append(pion[1])
            event['pions/py'].append(pion[2])
            event['pions/pz'].append(pion[3])
            event['pions/q'].append(pion[4])
            event['pions/beta'].append(pion[5])
            event['pions/dedx'].append(pion[6])

        event['kaons/nkaons'] = len(kaons)
        for kaon in kaons:
            event['kaons/e'].append(kaon[0])
            event['kaons/px'].append(kaon[1])
            event['kaons/py'].append(kaon[2])
            event['kaons/pz'].append(kaon[3])
            event['kaons/q'].append(kaon[4])
            event['kaons/beta'].append(kaon[5])
            event['kaons/dedx'].append(kaon[6])

        event['protons/nprotons'] = len(protons)
        for proton in protons:
            event['protons/e'].append(proton[0])
            event['protons/px'].append(proton[1])
            event['protons/py'].append(proton[2])
            event['protons/pz'].append(proton[3])
            event['protons/q'].append(proton[4])
            event['protons/beta'].append(proton[5])
            event['protons/dedx'].append(proton[6])

        event['muons/nmuons'] = len(muons)
        for muon in muons:
            event['muons/e'].append(muon[0])
            event['muons/px'].append(muon[1])
            event['muons/py'].append(muon[2])
            event['muons/pz'].append(muon[3])
            event['muons/q'].append(muon[4])
            event['muons/beta'].append(muon[5])
            event['muons/dedx'].append(muon[6])

        event['electrons/nelectrons'] = len(electrons)
        for electron in electrons:
            event['electrons/e'].append(electron[0])
            event['electrons/px'].append(electron[1])
            event['electrons/py'].append(electron[2])
            event['electrons/pz'].append(electron[3])
            event['electrons/q'].append(electron[4])
            event['electrons/beta'].append(electron[5])
            event['electrons/dedx'].append(electron[6])

        event['photons/nphotons'] = len(photons)
        for photon in photons:
            event['photons/e'].append(photon[0])
            event['photons/px'].append(photon[1])
            event['photons/py'].append(photon[2])
            event['photons/pz'].append(photon[3])

        h5hep.pack(data,event)

    print("Writing the file...")
    outfilename = infilename.split('.')[0] + ".hdf5"
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    #'''
################################################################################

if __name__ == "__main__":
    infilename = sys.argv[1]
    #convert_cms(infilename)
    convert_babar(infilename)

