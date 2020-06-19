import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import mpl_toolkits.mplot3d.art3d as a3

#from IPython.display import clear_output,display
import time

import h5hep

#import zipfile

################################################################################
def get_collisions(infile,verbose=False,experiment='CMS'):

    print("\nBuilding a simplified interface to the events...\n")

    collisions = []

    data,event = h5hep.load(infile, verbose=verbose)

    nentries = data['nentries']

    if experiment.lower() == 'cms':
        groups = [['jets',['e','px','py','pz','btag']], 
                  ['muons',['e','px','py','pz','q']],
                  ['electrons',['e','px','py','pz','q']],
                  ['photons',['e','px','py','pz']] ]
    elif experiment.lower() == 'babar':
        groups = [['pions',['e','px','py','pz','q','beta','dedx']], 
                  ['kaons',['e','px','py','pz','q','beta','dedx']], 
                  ['protons',['e','px','py','pz','q','beta','dedx']], 
                  ['muons',['e','px','py','pz','q','beta','dedx']],
                  ['electrons',['e','px','py','pz','q','beta','dedx']],
                  ['photons',['e','px','py','pz']] ]
    elif experiment.lower() == 'cleo':
        groups =  [ ['pions',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['kaons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['muons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['electrons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['photons',['e','px','py','pz']] ]


    for i in range(0,nentries):

        #if verbose:
        if 1:
            if i%10000==0:
                print("Reading in event ",i)

        h5hep.unpack(event,data,n=i)

        collision = {}

        for group in groups:
            gname = group[0]
            gvars = group[1]
            collision[gname] = []
            key = "%s/n%s" % (gname, gname)
            ngroup = event[key]
            for j in range(ngroup):
                particle = {}
                for var in gvars:
                    event_key = '%s/%s' % (gname,var)
                    particle[var] = event[event_key][j]

                collision[gname].append(particle)

        if experiment.lower() == 'cms':
            collision['METx'] = event['METx']
            collision['METy'] = event['METy']

        collisions.append(collision)

    return collisions

################################################################################
def get_number_of_entries(alldata):

    nentries = alldata[0]['nentries'] # We assume passing in an ntuple/list of data/event

    return nentries

################################################################################
def get_all_data(infile,verbose=False):

    print("\nLoading in the data...\n")

    data,event = h5hep.load(infile, verbose=verbose)

    return [data,event]

################################################################################
################################################################################
def get_collision(alldata,entry_number=0,verbose=False,experiment='CMS'):

    data,event = alldata[0],alldata[1]

    groups = None
    if experiment.lower() == 'cms':
        groups = [['jets',['e','px','py','pz','btag']], 
                  ['muons',['e','px','py','pz','q']],
                  ['electrons',['e','px','py','pz','q']],
                  ['photons',['e','px','py','pz']] ]
    elif experiment.lower() == 'babar':
        groups = [['pions',['e','px','py','pz','q','beta','dedx']], 
                  ['kaons',['e','px','py','pz','q','beta','dedx']], 
                  ['protons',['e','px','py','pz','q','beta','dedx']], 
                  ['muons',['e','px','py','pz','q','beta','dedx']],
                  ['electrons',['e','px','py','pz','q','beta','dedx']],
                  ['photons',['e','px','py','pz']] ]
    elif experiment.lower() == 'cleo':
        groups =  [ ['pions',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['kaons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['muons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['electrons',['e','px','py','pz','q','sigpi','sigka','likpi','likka','nphopi','nphoka','depthmu','cluster_energy'] ],
                    ['photons',['e','px','py','pz']] ]
    else:
        print("\nThe experiment {0} is not recognized\n".format(experiment))
        exit()


    h5hep.unpack(event,data,n=entry_number)

    collision = {}

    for group in groups:
        gname = group[0]
        gvars = group[1]
        collision[gname] = []
        key = "%s/n%s" % (gname, gname)
        ngroup = event[key]
        for j in range(ngroup):
            particle = {}
            for var in gvars:
                event_key = '%s/%s' % (gname,var)
                particle[var] = event[event_key][j]

            collision[gname].append(particle)

    if experiment.lower() == 'cms':
        collision['METx'] = event['METx']
        collision['METy'] = event['METy']

    return collision

################################################################################
def get_icecube_event(alldata,entry_number=0,verbose=False):

    data,event = alldata[0],alldata[1]

    h5hep.unpack(event,data,n=entry_number)

    return event

