import numpy as np
import sys
sys.path.append('../pps_tools')
import h5hep 

import cms_tools as cms
import babar_tools as babar
import cleo_tools as cleo

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

    groups = [ ['pions','npions',['e','px','py','pz','q','beta','dedx'] ], 
               ['kaons','nkaons',['e','px','py','pz','q','beta','dedx'] ], 
               ['protons','nprotons',['e','px','py','pz','q','beta','dedx'] ], 
               ['muons','nmuons',['e','px','py','pz','q','beta','dedx'] ], 
               ['electrons','nelectrons',['e','px','py','pz','q','beta','dedx'] ], 
               ['photons','nphotons',['e','px','py','pz','q','beta','dedx'] ], 
               ]

    for group in groups:

        h5hep.create_group(data,group[0],counter=group[1])
        h5hep.create_dataset(data,group[2],group=group[0],dtype=float)

    '''
    h5hep.create_group(data,'pions',counter='npions')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='pions',dtype=float)
    '''

    event = h5hep.create_single_event(data)

    collisions = babar.get_collisions(open(infilename))

    for collision in collisions:

        h5hep.clear_event(event)

        pions,kaons,protons,muons,electrons,photons = collision

        particles = [pions,kaons,protons,muons,electrons,photons]

        for group,particle in zip(groups, particles):
            key = "%s/%s" % (group[0],group[1])
            event[key] = len(particle)
            for p in particle:
                for j in range(len(group[2])):
                    key = '%s/%s' % (group[0],group[2][j])
                    event[key].append(p[j])

        '''
        event['pions/npions'] = len(pions)
        for pion in pions:
            event['pions/e'].append(pion[0])
            event['pions/px'].append(pion[1])
            event['pions/py'].append(pion[2])
            event['pions/pz'].append(pion[3])
            event['pions/q'].append(pion[4])
            event['pions/beta'].append(pion[5])
            event['pions/dedx'].append(pion[6])
        '''

        h5hep.pack(data,event)

    print("Writing the file...")
    outfilename = infilename.split('.')[0] + ".hdf5"
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    
################################################################################
def convert_cleo(infilename,maxentries=None):
    data = h5hep.initialize()

    groups = [ ['pions','npions',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ], 
               ['kaons','nkaons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ], 
               ['muons','nmuons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ], 
               ['electrons','nelectrons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ], 
               ['photons','nphotons',['e','px','py','pz'] ],
               ]

    for group in groups:

        h5hep.create_group(data,group[0],counter=group[1])
        h5hep.create_dataset(data,group[2],group=group[0],dtype=float)

    '''
    h5hep.create_group(data,'pions',counter='npions')
    h5hep.create_dataset(data,['e','px','py','pz','q','beta','dedx'],group='pions',dtype=float)
    '''

    event = h5hep.create_single_event(data)

    collisions = cleo.get_collisions(open(infilename))

    for count,collision in enumerate(collisions):

        if maxentries is not None and count>=maxentries:
                break

        h5hep.clear_event(event)

        pions,kaons,muons,electrons,photons = collision

        particles = [pions,kaons,muons,electrons,photons]

        for group,particle in zip(groups, particles):
            key = "%s/%s" % (group[0],group[1])
            event[key] = len(particle)
            for p in particle:
                for j in range(len(group[2])):
                    key = '%s/%s' % (group[0],group[2][j])
                    event[key].append(p[j])

        '''
        event['pions/npions'] = len(pions)
        for pion in pions:
            event['pions/e'].append(pion[0])
            event['pions/px'].append(pion[1])
            event['pions/py'].append(pion[2])
            event['pions/pz'].append(pion[3])
            event['pions/q'].append(pion[4])
            event['pions/beta'].append(pion[5])
            event['pions/dedx'].append(pion[6])
        '''

        h5hep.pack(data,event)

    print("Writing the file...")
    outfilename = infilename.split('.')[0] + ".hdf5"
    if maxentries is not None:
        outfilename = infilename.split('.')[0] + "_" + str(maxentries) + "entries.hdf5"
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    
################################################################################

if __name__ == "__main__":
    infilename = sys.argv[1]
    #convert_cms(infilename)
    #convert_babar(infilename)
    convert_cleo(infilename,maxentries=10)

