#!/usr/bin/env python3

"""
My functions...to clean up the main code
"""

__author__     =  "Paul Mendoza"
__copyright__  =  "Copyright 2016, Planet Earth"
__credits__    = ["Ryan_McClarren"]
__license__    =  "GPL"
__version__    =  "1.0.1"
__maintainer__ =  "Paul Mendoza"
__email__      =  "paul.m.mendoza@gmail.com"
__status__     =  "Production"

################################################################
##################### Import packages ##########################
################################################################

import scipy.special as sps
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "monospace"
import matplotlib
matplotlib.rc('text',usetex=True)
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
import random as rn

################################################################
######################### Functions ############################
################################################################

def GammaPDF(a,b,z):
    f_x=((z**(a-1))*np.exp(-z/b))\
                     /\
        (sps.gamma(a)*b**(a))
    return(f_x)

def nth_repl(s, sub, repl, nth):
    find = s.find(sub)
    # if find is not p1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != nth:
        # find + 1 means we start at the last match start index + 1
        find = s.find(sub, find + 1)
        i += 1
        # if i  is equal to nth we found nth matches so replace
    if i == nth:
        return s[:find]+repl+s[find + len(sub):]
    return s


def PlotHistSave(Error,Ntimes,Element,Nbins):
    P=Element[0:2]
    if Element[3].isalpha():
        E=Element[2:4]
        I=Element[4:7]
    else:
        E=Element[2]
        I=Element[3:6]
    S=Element[-1]
    print(P,E,I,S)
    
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel(r'$\sigma_'+S+'\ ^{'+I+'}$'+E,fontsize=16)
    ax.set_ylabel(r'Count out of '+str(Ntimes),fontsize=18)
    ax.hist(Error,Nbins,color='green',alpha=0.7,edgecolor='black')
    #ax.set_xlim(-500,500)
    plt.savefig(Element+'HIST.pdf')


def StripNL(List):
    List2=[]
    for i in range(0,len(List)):
        hold=List[i].replace('\n','')
        hold='%.3e' % float(hold)
        hold=hold.replace('e','E')
        List2.append(hold)
    return(List2)

def Graboutput(Isotope,Pages,TYPE):

    for Page in Pages:
        if TYPE in Page and Isotope in Page:
            List=Page.split('\n')
            for item in List:
                if Isotope in item:
                    hold=item
                    hold=hold.replace(Isotope,"")
                    hold=hold.split()
                    return(hold)
                    
