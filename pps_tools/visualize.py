import numpy as np
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import mpl_toolkits.mplot3d.art3d as a3

from IPython.display import clear_output,display
import time

import h5hep

import plotly.express as px

################################################################################
################################################################################
################################################################################
def draw_jet(origin=(0,0),angle=90,length=0.5,opening_angle=20,ntracks=5,show_tracks=False):

    lines = []
    patches = []

    # Edges of cone
    width_at_top = length*np.deg2rad(opening_angle)
    for side in [-1,1]:
        theta0 = np.deg2rad(angle+(side*opening_angle/2.0)) 
        x1 = length*np.cos(theta0)
        y1 = length*np.sin(theta0)
        #print x1,y1
        line = mlines.Line2D((origin[0],x1), (origin[1],y1), lw=2., alpha=0.4,color='red',markeredgecolor='red')
        lines.append(line)

    # End of cone
    arad = np.deg2rad(angle)
    center = (origin[0]+np.cos(arad)*length,origin[1]+np.sin(arad)*length)
    #print center
    p = mpatches.Ellipse(center, width_at_top+0.01, width_at_top/2.0,facecolor='red',alpha=0.4,edgecolor='gray',angle=abs(angle+90))
    patches.append(p)

    return patches,lines


    

################################################################################
################################################################################
def draw_jets(origins=[(0,0)],angles=[90],lengths=[0.5],opening_angles=[20],ntrackss=[5],show_trackss=[False]):

    alllines = []
    allpatches = []

    # Edges of cone
    for origin,angle,length,opening_angle,ntracks,show_tracks in zip(origins,angles,lengths,opening_angles,ntrackss,show_trackss):
        patches,lines = draw_jet(origin=origin,angle=angle,length=length,opening_angle=opening_angle,ntracks=ntracks,show_tracks=show_tracks)
        allpatches += patches
        alllines += lines


    return allpatches,alllines


    
################################################################################
################################################################################
def draw_line3D(origin=[(0,0,0)],pmom=[(1,1,1)],color='red',lw=2.0,ls='solid'):

    lines = []

    #print pmom
    for o,p in zip(origin,pmom):
        #x1 = p[0]
        #y1 = p[1]
        #z1 = p[2]
        x1 = p[2]
        y1 = p[0]
        z1 = p[1]
        #print x1,y1,z1
        line = a3.Line3D((o[0],x1),(o[1],y1),(o[0],z1), lw=lw, alpha=0.9,color=color,markeredgecolor=color, linestyle = ls)
        lines.append(line)

    return lines


################################################################################
################################################################################
def draw_beams(pmom=[(0,0,-200.0),(0,0,200.0)]):

    lines = draw_line3D(origin=[(0,0,-0.1),(0,0,0.1)],pmom=pmom,color='red',lw=1)

    return lines

################################################################################
################################################################################
def draw_jet3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='orange'):

    neworg = origin.copy()
    newmom = pmom.copy()

    offset = [[0.05,0.05,0.05],
              [0.05,0.05,-0.05],
              [0.05,-0.05,0.05],
              [0.05,-0.05,-0.05],
              [-0.05,0.05,0.05],
              [-0.05,0.05,-0.05],
              [-0.05,-0.05,0.05],
              [-0.05,-0.05,-0.05],
            ]

    offset = np.array(offset)
    offset *= 50

    for p in pmom:
        for o in offset:
            #print p.copy(),o
            pnew = p.copy() + o
            #print pnew
            newmom = np.vstack((newmom,pnew))
            neworg = np.vstack((neworg,(0,0,0)))

    lines = draw_line3D(origin=neworg,pmom=newmom,color=color,lw=1,ls=ls)
    ##lines += draw_line3D(origin=neworg,pmom=newmom,color='gray',lw=.25,ls='solid')

    return lines

################################################################################
################################################################################
def draw_pion3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='red'):
    
    lines = draw_line3D(origin=origin,pmom=pmom,color=color,lw=2,ls=ls)
    ##lines += draw_line3D(origin=origin,pmom=pmom,color='gray',lw=.25,ls='solid')

    return lines

################################################################################
################################################################################
def draw_kaon3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='red'):
    
    lines = draw_line3D(origin=origin,pmom=pmom,color=color,lw=5,ls=ls)
    ##lines += draw_line3D(origin=origin,pmom=pmom,color='gray',lw=.25,ls='solid')

    return lines

################################################################################
################################################################################
def draw_proton3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='red'):
    
    lines = draw_line3D(origin=origin,pmom=pmom,color=color,lw=9,ls=ls)
    ##lines += draw_line3D(origin=origin,pmom=pmom,color='gray',lw=.25,ls='solid')

    return lines

################################################################################
################################################################################
def draw_muon3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='blue'):
    
    lines = draw_line3D(origin=origin,pmom=pmom,color=color,lw=5,ls=ls)
    ##lines += draw_line3D(origin=origin,pmom=pmom,color='gray',lw=.25,ls='solid')

    return lines

################################################################################
################################################################################
def draw_electron3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='green'):

    lines = draw_line3D(origin=origin,pmom=pmom,color=color,lw=2,ls=ls)
    ##lines += draw_line3D(origin=origin,pmom=pmom,color='gray',lw=.25,ls='solid')

    return lines


################################################################################
################################################################################
def draw_photon3D(origin=[(0,0,0)],pmom=[(1,1,1)],ls='solid',color='gray'):
    
    lines = draw_line3D(origin=origin,pmom=pmom,color=color,ls=ls,lw=4)
   ## lines += draw_line3D(origin=origin,pmom=pmom,color='gray',lw=.25,ls='solid')

    return lines

################################################################################
################################################################################
def display_collision3D(collision,fig=None,ax=None,color_blind=False,experiment='CMS'):

    if fig is None:
        fig = plt.figure(figsize=(6,4),dpi=100)

    if ax is None:
        ax = fig.add_subplot(1,1,1)
        ax = fig.gca(projection='3d')
        plt.subplots_adjust(top=0.98,bottom=0.02,right=0.98,left=0.02)

    new_objects = None
    objects = None
    if experiment.lower()=='cms':
        # Need to pull out just the momentum for each. 
        orgjets = collision['jets']
        orgmuons = collision['muons']
        orgelectrons = collision['electrons']
        orgphotons = collision['photons']
        orgMETx,orgMETy = collision['METx'],collision['METy']

        objects = [orgjets, orgmuons, orgelectrons, orgphotons]

        new_objects = {}
        new_objects['jets'] = {'colorblind_color':'gray','colorblind_ls':'solid','p':[]}
        new_objects['muons'] = {'colorblind_color':'black','colorblind_ls':'dashed','p':[]}
        new_objects['electrons'] = {'colorblind_color':'gray','colorblind_ls':'dashed','p':[]}
        new_objects['photons'] = {'colorblind_color':'black','colorblind_ls':'solid','p':[]}

    elif experiment.lower()=='babar' or experiment.lower()=='cleo':
        # Need to pull out just the momentum for each. 
        orgpions = collision['pions']
        orgkaons = collision['kaons']
        if experiment.lower()=='babar':
            orgprotons = collision['protons']
        orgmuons = collision['muons']
        orgelectrons = collision['electrons']
        orgphotons = collision['photons']

        if experiment.lower()=='babar':
            objects = [orgpions, orgkaons, orgprotons, orgmuons, orgelectrons, orgphotons]
        else:
            objects = [orgpions, orgkaons, orgmuons, orgelectrons, orgphotons]

        new_objects = {}
        new_objects['pions'] = {'colorblind_color':'gray','colorblind_ls':'dotted','p':[]}
        new_objects['kaons'] = {'colorblind_color':'black','colorblind_ls':'dotted','p':[]}
        if experiment.lower()=='babar':
            new_objects['protons'] = {'colorblind_color':'gray','colorblind_ls':'solid','p':[]}
        new_objects['muons'] = {'colorblind_color':'black','colorblind_ls':'dashed','p':[]}
        new_objects['electrons'] = {'colorblind_color':'gray','colorblind_ls':'dashed','p':[]}
        new_objects['photons'] = {'colorblind_color':'black','colorblind_ls':'solid','p':[]}

    #jets = []
    for obj,key in zip(objects, new_objects.keys()):
        for ob in obj:
            new_objects[key]['p'].append([ob['px'], ob['py'], ob['pz']])

    lines = None
    if experiment.lower()=='cms':
        lines = draw_beams()
    elif experiment.lower()=='babar':
        lines = draw_beams(pmom=[(0,0,-10.0),(0,0,10.0)])
    elif experiment.lower()=='cleo':
        lines = draw_beams(pmom=[(0,0,-2.0),(0,0,2.0)])

    for key in new_objects.keys():
        pmom = new_objects[key]['p']
        origin = np.zeros((len(new_objects[key]),3))

        if(color_blind == False):
            if key=='jets':
                lines += draw_jet3D(origin=origin,pmom=pmom)
            elif key=='pions':
                lines += draw_pion3D(origin=origin,pmom=pmom)
            elif key=='kaons':
                lines += draw_kaon3D(origin=origin,pmom=pmom)
            elif key=='protons':
                lines += draw_proton3D(origin=origin,pmom=pmom)
            elif key=='muons':
                lines += draw_muon3D(origin=origin,pmom=pmom)
            elif key=='electrons':
                lines += draw_electron3D(origin=origin,pmom=pmom)
            elif key=='photons':
                lines += draw_photon3D(origin=origin,pmom=pmom)
        else:
            ls = new_objects[key]['colorblind_ls']
            cb_color = new_objects[key]['colorblind_color']
            if key=='jets':
                lines += draw_jet3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)
            elif key=='pions':
                lines += draw_pion3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)
            elif key=='kaons':
                lines += draw_kaon3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)
            elif key=='protons':
                lines += draw_proton3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)
            elif key=='muons':
                lines += draw_muon3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)
            elif key=='electrons':
                lines += draw_electron3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)
            elif key=='photons':
                lines += draw_photon3D(origin=origin,pmom=pmom,ls=ls,color=cb_color)


    for l in lines:
        ax.add_line(l)

    if experiment.lower()=='cms':
        ax.set_xlim(-200,200)
        ax.set_ylim(-200,200)
        ax.set_zlim(-200,200)
    elif experiment.lower()=='babar':
        ax.set_xlim(-2,2)
        ax.set_ylim(-2,2)
        ax.set_zlim(-2,2)
    elif experiment.lower()=='cleo':
        ax.set_xlim(-0.2,0.2)
        ax.set_ylim(-0.2,0.2)
        ax.set_zlim(-0.2,0.2)

    #return lines,fig,ax
################################################################################
################################################################################

def display_collision3D_animate(collisions,fig=None):

    if fig is None:
        fig = plt.figure(figsize=(6,4),dpi=100)
    ax = fig.add_subplot(1,1,1)
    ax = fig.gca(projection='3d')
    plt.subplots_adjust(top=0.98,bottom=0.02,right=0.98,left=0.02)

    if type(collisions[0][0][0]) is not list:
        collisions = [collisions]

    for collision in collisions:
        # For animations
        #fig.clear()
        clear_output()
        ax.clear();

        jets,muons,electrons,photons,met = collision

        lines = draw_beams()

        pmom = np.array(jets).transpose()[1:4].transpose()
        origin = np.zeros((len(jets),3))
        lines += draw_jet3D(origin=origin,pmom=pmom)

        pmom = np.array(muons).transpose()[1:4].transpose()
        origin = np.zeros((len(muons),3))
        lines += draw_muon3D(origin=origin,pmom=pmom)

        pmom = np.array(electrons).transpose()[1:4].transpose()
        origin = np.zeros((len(electrons),3))
        lines += draw_electron3D(origin=origin,pmom=pmom)

        pmom = np.array(photons).transpose()[1:4].transpose()
        origin = np.zeros((len(photons),3))
        lines += draw_photon3D(origin=origin,pmom=pmom)


        for l in lines:
            ax.add_line(l)

        ax.set_xlim(-200,200)
        ax.set_ylim(-200,200)
        ax.set_zlim(-200,200)

        display(ax)
        time.sleep(0.5)

    #return lines,fig,ax

################################################################################
def display_icecube_event(event,backend='plotly',draw_wires=True,color_scale='Bluered'): 
    q,x,y,z,t = event['hits/q'],event['hits/x'],event['hits/y'],event['hits/z'],event['hits/t'] 

    if backend=='plotly':
          #############################################
        fig= px.scatter_3d(x=x,y=y,z=z,color=t,color_continuous_scale=color_scale)
        fig.update_traces(marker=dict(size=q*2,line=dict(width=0)),selector=dict(mode='markers'))
        if draw_wires:
            ############ Get which strings had hits on them
            vals = np.array([x,y]).transpose()
            string_coords = []
            for a in vals:
                IN_FLAG = False
                for p in string_coords:
                     #print(a,p)
                    if a[0] == p[0] and a[1]==p[1]:
                        IN_FLAG = True
                        break

                if not IN_FLAG:
                    string_coords.append(a)

            print("here")
            #print(string_coords)
            ################## Draw the strings ########################
            for p in string_coords:
                fig.append_trace({'x':[p[0],p[0]],'y':[p[1],p[1]],'z':[-400,1200],'type':'scatter3d','showlegend':False,'marker':{'size':1},'line':{'dash':'dash','color':'lightgray'}},1,1)
            ##############################################################

        fig.update_layout(width=800,height=400,margin=dict( \
                  l=0, \
                  r=0, \
                  b=0, \
                  t=0, \
                  pad=1 \
              ),)
        return fig 

