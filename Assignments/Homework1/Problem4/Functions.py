#!/usr/bin/env python3

"""
FractionAM converts atom fractions to mass fractions
and mass fractions to atom fractions. Input is a 
single string with MCNP style fractions.
"""

__author__     =  "Paul Mendoza"
__copyright__  =  "Copyright 2016, Planet Earth"
__credits__    = ["Sunil Chirayath",
                  "Charles Folden",
                  "Jeremy Conlin"]
__license__    =  "GPL"
__version__    =  "1.0.1"
__maintainer__ =  "Paul Mendoza"
__email__      =  "paul.m.mendoza@gmail.com"
__status__     =  "Production"

################################################################
##################### Import packages ##########################
################################################################

import time
start_time = time.time()
import scipy.special as sps
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "monospace"
import matplotlib
matplotlib.rc('text',usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
import random as rn
import Functions as fun

################################################################
######################### Functions ############################
################################################################

def GammaPDF(alpha,beta,theta):
    f_x=((theta**(alpha-1))*np.exp(-theta*beta))\
                           /\
        (sps.gamma(alpha)*beta**(-alpha))
    return(f_x)


def Plot(theta,f_x):
    
    fig = plt.figure()
    ax = [fig.add_subplot(111)]
    ax[0].spines['top'].set_color('none')
    ax[0].spines['bottom'].set_color('none')
    ax[0].spines['left'].set_color('none')
    ax[0].spines['right'].set_color('none')
    ax[0].tick_params(labelcolor='w', top='off', bottom='off', left='off',
                      labelleft='off',labelright='off',labeltop='off',
                      labelbottom='off',right='off')
                    
    ax = np.append(ax,fig.add_subplot(211))
    ax = np.append(ax,fig.add_subplot(212))
    
    ax[1].plot(theta,f_x,'r',linewidth=2.0)
    ax[2].plot(theta,f_x,'r',linewidth=2.0)
    
    ax[2].set_xlabel(r'$\boldsymbol{\theta}$',fontsize=18)
    ax[0].set_ylabel(r'\textbf{Probability}',fontsize=18)
    ax[0].yaxis.labelpad=55

    ax[1].set_ylabel(r'Square $N=10^3$',fontsize=14)
    ax[2].set_ylabel(r'Triangular $N=10^3/2$',fontsize=14)
    
    ax[1].xaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[2].xaxis.set_tick_params(labelsize=14)
    ax[2].yaxis.set_tick_params(labelsize=14)
    
    ax[1].grid(alpha=0.8,color='black',linestyle='dotted')
    ax[2].grid(alpha=0.8,color='black',linestyle='dotted')
    return(fig,ax)

def PlotaxIn(X,Y,i,ax,j):
    if i<10**3 and j==1:
        ax[j].plot(X,Y,'x',markersize=7,markeredgewidth=2.5,
                   color='gray')
    elif i<(10**3)/2 and j==2:
        ax[j].plot(X,Y,'x',markersize=7,markeredgewidth=2.5,
                   color='gray',label="Inside")
    return(ax)

def PlotaxOut(X,Y,i,ax,j):
    if i<10**3 and j==1:
        ax[j].plot(X,Y,'ko',markersize=5)
    elif i<(10**3)/2 and j==2:
        ax[j].plot(X,Y,'ko',markersize=5,label="Outside")
    return(ax)

def Plotlegend(ax,theta,f_x):
    handles,labels=ax[2].get_legend_handles_labels()
    Outside=False
    Inside=False

    for i in range(0,len(handles)):
        if Outside and Inside:
            break
        if not Outside and "Outside" in labels[i]:
            Outside=True
            OutsideIndex=i
        if not Inside and "Inside" in labels[i]:
            Inside=True
            InsideIndex=i

    Smallerhandles=[handles[OutsideIndex],handles[InsideIndex]]
    Smallerlabels=[labels[OutsideIndex],labels[InsideIndex]]
    Lfont={'family':'monospace',
             'size': 12}
    ax[2].legend(Smallerhandles,Smallerlabels,
                 loc='best',fontsize=12,prop=Lfont)

    ax[1].plot(theta,f_x,'r',linewidth=2.0)
    ax[2].plot(theta,f_x,'r',linewidth=2.0)
    return(ax)
