import numpy as np
import sys
sys.path.append('../pps_tools')
import h5hep 

import ROOT 
################################################################################
def sph2cart(pmag,costh,phi):
    theta = np.arccos(costh)
    x = pmag*np.sin(theta)*np.cos(phi)
    y = pmag*np.sin(theta)*np.sin(phi)
    z = pmag*costh
    return x,y,z
################################################################################


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

    f = ROOT.TFile(infilename)
    t = ROOT.Get('ntp1')

    nentries = t.GetEntries()

    #'''
    for i in range(nentries):

        t.GetEvent(i)

        '''
        event['jets/njets'] = len
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
        '''

    '''
    print("Writing the file...")
    outfilename = infilename.split('.')[0] + ".hdf5"
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    '''
################################################################################
################################################################################
@profile
def convert_babar(infilename,maxentries=None):
    data = h5hep.initialize()

    groups = [ ['pions','npions',['e','px','py','pz','q','beta','dedx'] ], 
               ['kaons','nkaons',['e','px','py','pz','q','beta','dedx'] ], 
               ['protons','nprotons',['e','px','py','pz','q','beta','dedx'] ], 
               ['muons','nmuons',['e','px','py','pz','q','beta','dedx'] ], 
               ['electrons','nelectrons',['e','px','py','pz','q','beta','dedx'] ], 
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

    f = ROOT.TFile(infilename)
    tree = f.Get('ntp1')

    nentries = tree.GetEntries()

    #'''
    for i in range(nentries):

        if maxentries is not None and i>=maxentries:
            break

        h5hep.clear_event(event)

        tree.GetEvent(i)

        if i%1000==0:
            print(i)

        #pions,kaons,protons,muons,electrons,photons = collision
        #particles = [pions,kaons,protons,muons,electrons,photons]

        event['pions/npions'] = tree.npi
        for j in range(tree.npi):
            e = tree.pienergy[j]
            p3 = tree.pip3[j]
            phi = tree.piphi[j]
            costh = tree.picosth[j]
            px,py,pz = sph2cart(p3,costh,phi)
            lund = tree.piLund[j]
            q = int(lund/np.abs(lund))
            idx = tree.piTrkIdx[j]
            dedx = tree.TRKdedxdch[idx]
            drc = tree.TRKDrcTh[idx]
            beta = 1.0/np.cos(drc)/1.474

            event['pions/e'].append(e)
            event['pions/px'].append(px)
            event['pions/py'].append(py)
            event['pions/pz'].append(pz)
            event['pions/q'].append(q)
            event['pions/beta'].append(beta)
            event['pions/dedx'].append(dedx)

        event['kaons/nkaons'] = tree.nK
        for j in range(tree.nK):
            e = tree.Kenergy[j]
            p3 = tree.Kp3[j]
            phi = tree.Kphi[j]
            costh = tree.Kcosth[j]
            px,py,pz = sph2cart(p3,costh,phi)
            lund = tree.KLund[j]
            q = int(lund/np.abs(lund))
            idx = tree.KTrkIdx[j]
            dedx = tree.TRKdedxdch[idx]
            drc = tree.TRKDrcTh[idx]
            beta = 1.0/np.cos(drc)/1.474

            event['kaons/e'].append(e)
            event['kaons/px'].append(px)
            event['kaons/py'].append(py)
            event['kaons/pz'].append(pz)
            event['kaons/q'].append(q)
            event['kaons/beta'].append(beta)
            event['kaons/dedx'].append(dedx)

        event['protons/nprotons'] = tree.np
        for j in range(tree.np):
            e = tree.penergy[j]
            p3 = tree.pp3[j]
            phi = tree.pphi[j]
            costh = tree.pcosth[j]
            px,py,pz = sph2cart(p3,costh,phi)
            lund = tree.pLund[j]
            q = int(lund/np.abs(lund))
            idx = tree.pTrkIdx[j]
            dedx = tree.TRKdedxdch[idx]
            drc = tree.TRKDrcTh[idx]
            beta = 1.0/np.cos(drc)/1.474

            event['protons/e'].append(e)
            event['protons/px'].append(px)
            event['protons/py'].append(py)
            event['protons/pz'].append(pz)
            event['protons/q'].append(q)
            event['protons/beta'].append(beta)
            event['protons/dedx'].append(dedx)

        event['muons/nmuons'] = tree.nmu
        for j in range(tree.nmu):
            e = tree.muenergy[j]
            p3 = tree.mup3[j]
            phi = tree.muphi[j]
            costh = tree.mucosth[j]
            px,py,pz = sph2cart(p3,costh,phi)
            lund = tree.muLund[j]
            q = int(lund/np.abs(lund))
            idx = tree.muTrkIdx[j]
            dedx = tree.TRKdedxdch[idx]
            drc = tree.TRKDrcTh[idx]
            beta = 1.0/np.cos(drc)/1.474

            event['muons/e'].append(e)
            event['muons/px'].append(px)
            event['muons/py'].append(py)
            event['muons/pz'].append(pz)
            event['muons/q'].append(q)
            event['muons/beta'].append(beta)
            event['muons/dedx'].append(dedx)

        event['electrons/nelectrons'] = tree.ne
        for j in range(tree.ne):
            e = tree.eenergy[j]
            p3 = tree.ep3[j]
            phi = tree.ephi[j]
            costh = tree.ecosth[j]
            px,py,pz = sph2cart(p3,costh,phi)
            lund = tree.eLund[j]
            q = int(lund/np.abs(lund))
            idx = tree.eTrkIdx[j]
            dedx = tree.TRKdedxdch[idx]
            drc = tree.TRKDrcTh[idx]
            beta = 1.0/np.cos(drc)/1.474

            event['electrons/e'].append(e)
            event['electrons/px'].append(px)
            event['electrons/py'].append(py)
            event['electrons/pz'].append(pz)
            event['electrons/q'].append(q)
            event['electrons/beta'].append(beta)
            event['electrons/dedx'].append(dedx)

        event['photons/nphotons'] = tree.ngamma
        for j in range(tree.ngamma):
            e = tree.gammaenergy[j]
            p3 = tree.gammap3[j]
            phi = tree.gammaphi[j]
            costh = tree.gammacosth[j]
            px,py,pz = sph2cart(p3,costh,phi)

            event['photons/e'].append(e)
            event['photons/px'].append(px)
            event['photons/py'].append(py)
            event['photons/pz'].append(pz)

        h5hep.pack(data,event)

    print("Writing the file...")
    outfilename = infilename.split('.')[0] + ".hdf5"
    if maxentries is not None:
        outfilename = infilename.split('.')[0] + "_" + str(maxentries) + "entries.hdf5"
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    
################################################################################
def convert_cleo(infilename):
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

    for collision in collisions:

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
    print(outfilename)
    hdfile = h5hep.write_to_file(outfilename,data,comp_type='gzip',comp_opts=9)
    
################################################################################

if __name__ == "__main__":
    exptype = sys.argv[1]
    infilename = sys.argv[2]
    maxnum = None
    if len(sys.argv)>3:
        maxnum = int(sys.argv[3])

    if exptype=='cms':
        convert_cms(infilename,maxentries=maxnum)
    elif exptype=='babar':
        convert_babar(infilename,maxentries=maxnum)
    elif exptype=='cleo':
        convert_cleo(infilename,maxentries=10)


