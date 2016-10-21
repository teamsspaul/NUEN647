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

def CalculatePearson(X1,X2):
    EX1=sum(X1)/len(X1)
    EX2=sum(X2)/len(X2)
    EX1X2=sum(X1*X2)/len(X1)
    ox1=(sum(X1**2-EX1**2)/len(X1))**0.5
    ox1NM1=(sum(X1**2-EX1**2)/(len(X1)-1))**0.5
    ox2=(sum(X2**2-EX2**2)/len(X2))**0.5
    ox2NM1=(sum(X2**2-EX2**2)/(len(X2)-1))**0.5
    rho=(EX1X2-EX1*EX2)/(ox1*ox2)
    rhoNM1=(EX1X2-EX1*EX2)/(ox1NM1*ox2NM1)
    return(rho,rhoNM1)

def Rank(X1):
    temp=X1.argsort()
    ranks=np.empty(len(X1),int)
    ranks[temp]=np.arange(len(X1))+1
    return(ranks)

def CalculateSpearman(X1,X2,X1R,X2R):
    RX1=sum(X1R)/len(X1R)
    RX2=sum(X2R)/len(X2R)
    A=sum((X1R-RX1)*(X2R-RX2))
    B=sum((X1R-RX1)**2)**0.5
    C=sum((X2R-RX2)**2)**0.5
    rhos=A/(B*C)
    return(rhos)

def CalculateTau(X1,X2):
    count=0;concordant=0;discordant=0
    for i in range(0,len(X1)):
        if not i==len(X1)-1:
            for j in range(i+1,len(X2)):
                if not i==j:
                    if X1[i]>X1[j] and X2[i]>X2[j]:
                        concordant=concordant+1
                    if X1[i]<X1[j] and X2[i]<X2[j]:
                        concordant=concordant+1
                    if X1[i]>X1[j] and X2[i]<X2[j]:
                        discordant=discordant+1
                    if X1[i]<X1[j] and X2[i]>X2[j]:
                        discordant=discordant+1
                    count=count+1
    tau=(concordant-discordant)/count
    return(tau)
