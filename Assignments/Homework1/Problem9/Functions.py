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

def PlotSetup():
    
    fig = plt.figure()
    ax = [fig.add_subplot(111)]
    ax[0].spines['top'].set_color('none')
    ax[0].spines['bottom'].set_color('none')
    ax[0].spines['left'].set_color('none')
    ax[0].spines['right'].set_color('none')
    ax[0].tick_params(labelcolor='w', top='off', bottom='off', left='off',
                      labelleft='off',labelright='off',labeltop='off',
                      labelbottom='off',right='off')
                    
    ax = np.append(ax,fig.add_subplot(411)) #1
    ax = np.append(ax,fig.add_subplot(412)) #2
    ax = np.append(ax,fig.add_subplot(421)) #3
    ax = np.append(ax,fig.add_subplot(422)) #4
    
    ax[0].set_xlabel(r'Number of Samples',fontsize=18)
    ax[0].xaxis.labelpad=20

    ax[1].set_ylabel(r'Mean',fontsize=14)
    ax[2].set_ylabel(r'Variance',fontsize=14)
    ax[3].set_ylabel(r'Skew',fontsize=14)
    ax[4].set_ylabel(r'Kurtosis',fontsize=14)
    
    ax[1].xaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[2].xaxis.set_tick_params(labelsize=14)
    ax[2].yaxis.set_tick_params(labelsize=14)
    ax[3].xaxis.set_tick_params(labelsize=14)
    ax[3].yaxis.set_tick_params(labelsize=14)
    ax[4].xaxis.set_tick_params(labelsize=14)
    ax[4].yaxis.set_tick_params(labelsize=14)
    
    ax[1].grid(alpha=0.8,color='black',linestyle='dotted')
    ax[2].grid(alpha=0.8,color='black',linestyle='dotted')
    ax[3].grid(alpha=0.8,color='black',linestyle='dotted')
    ax[4].grid(alpha=0.8,color='black',linestyle='dotted')
    return(fig,ax)

def Plot(N,mean,variance,skew,kurtosis,ax):
        
    ax[1].plot(N,mean,'.k')
    ax[2].plot(N,variance,'.k')
    ax[3].plot(N,skew,'.k')
    ax[4].plot(N,kurtosis,'.k')

    return(ax)

