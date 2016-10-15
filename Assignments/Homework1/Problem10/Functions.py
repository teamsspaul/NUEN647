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

################################################################
######################### Functions ############################
################################################################

def Plot():
    
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
    
    ax[2].set_xlabel(r'\textbf{X or Y}',fontsize=18)
    ax[0].set_ylabel(r'\textbf{Probability}',fontsize=18)
    ax[0].yaxis.labelpad=55

    ax[1].set_ylabel(r'$f(y|X=\mu_X)$',fontsize=14)
    ax[2].set_ylabel(r'$f(x|Y=\mu_Y)$',fontsize=14)
    
    ax[1].xaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[2].xaxis.set_tick_params(labelsize=14)
    ax[2].yaxis.set_tick_params(labelsize=14)
    
    ax[1].grid(alpha=0.8,color='black',linestyle='dotted')
    ax[2].grid(alpha=0.8,color='black',linestyle='dotted')
    return(fig,ax)

def Plotax(X,Y,ax,j):
    ax[j].plot(X,Y,'-k',linewidth=3)
    return(ax)

plt.savefig('P4F1.pdf')
