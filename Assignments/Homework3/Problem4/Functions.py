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
import lhsmdu
from scipy.stats import beta
from scipy import interpolate
from scipy import integrate
from scipy.integrate import trapz

################################################################
######################### Functions ############################
################################################################

def betau(a,b):
    return(a/(a+b))

def betao(a,b):
    return((a*b)/(((a+b)**2)*(a+b+1)))

def Rosen(x,y):
    return((1-x)**2+100*(y-x**2)**2)

def Z(x,y):
    return(10-Rosen(x,y))


def X(t):
    return(2*t-1)

def Y(s):
    return(2*s-1)

def vdc(n, base=2):
    """
    Generates van der Corput sequence function
    """
    vdc, denom = 0,1
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder / denom
    return vdc

def Rstrat(N,Nstrata):
    """
    Generate a vector N long with stratified
    random variables, with Nstrata bins
    """
    RN=[]
    Nloop=int(N/Nstrata)*Nstrata
    for i in range(0,int(N/Nstrata)):
        for j in range(0,Nstrata):
            RN.append(np.random.uniform(low=j/Nstrata,
                                high=(j+1)/Nstrata,size=1))
    #If N/Nstrata doesn't divide evenly
    if Nloop<N:
        for j in range(0,N-Nloop):
            RN.append(np.random.uniform(low=j/Nstrata,
                            high=(j+1)/Nstrata,size=1))
    return(RN)

#Van Sampling
def Rvdc(N,base=2):
    """
    Will generate a vector N long of the van
    der Corput sequence with a chosen base
    """
    RN=[]
    for i in range(0,N):
        RN.append(vdc(i+1,base))
    return(RN)

def HIST(Xlabel,Samples,Nbins,filename,N):
    """
    Plot histogram
    """
    #Plot histogram
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel(Xlabel,fontsize=16)
    #For normalization of histogram
    weights=np.ones_like(Samples)/(len(Samples))
    ax.set_ylabel('Normalized counts with tot N = '+str(N),fontsize=18)
    #Get data from histogram and plot
    n,bins,patches=ax.hist(Samples,Nbins,
            weights=weights,color='green',alpha=0.7,edgecolor='black')

    #Modify some of the data from histograms
    Probability=n #Probability in a particular bin
    XValues=[]
    PDF=[]   #Probability density function (different than Prob)
    for i in range(0,len(n)):
        XValues.append((bins[i]+bins[i+1])/2)
        PDF.append(Probability[i]/(bins[i+1]-bins[i]))
        
    #Fit the data to a function
    m=(PDF[1]-PDF[0])/(XValues[1]-XValues[0]) #slope at start
    b=PDF[0]-m*XValues[0]
    #print(b,PDF[0],PDF[1])
    XValues.insert(0,0)
    PDF.insert(0,b)
    I=interpolate.interp1d(XValues,PDF,
                           fill_value=max(Probability),bounds_error=False)
    #Evaluate the function and see how well it
    #fits the data
    x=np.linspace(min(XValues),max(XValues),10000)
    x=np.linspace(min(XValues),10,10000)
    y=I(x)
    ax.plot(x,y,'r',linewidth=2.0)
    plt.savefig(filename)

    #does the pdf integrate to 1?
    print(integrate.trapz(I(x),x))
    return(I)
