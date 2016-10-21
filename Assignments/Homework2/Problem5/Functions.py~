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

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"]="monospace"
import matplotlib
matplotlib.rc('text',usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

################################################################
######################### Functions ############################
################################################################

def CalculateRho(X1,X2):
    EX1=sum(X1)/len(X1)
    EX2=sum(X2)/len(X2)
    EX1X2=sum(X1*X2)/len(X1)
    oX1=sum(X1**2-EX1**2)/len(X1)
    oX2=sum(X2**2-EX2**2)/len(X2)
    rho=(EX1X2-EX1*EX2)/(oX1*oX2)
    return(rho)

def PlotHistSave(Error,Ntimes):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel(r'Percent Error $100\frac{|\rho_g-\rho_a|}{\rho_a}$',fontsize=16)
    ax.set_ylabel(r'Count out of '+str(Ntimes),fontsize=18)
    ax.hist(Error,500,color='green',alpha=0.7,edgecolor='black')
    ax.set_xlim(-1000,1000)
    plt.savefig('P2.pdf')
