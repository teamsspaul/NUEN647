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
import matplotlib.mlab as mlab
import copy
import os

#############################################################
######################### Variables #########################
#############################################################

# Basic information
FigureSize = (11, 6)              # Dimensions of the figure
TypeOfFamily='monospace'          # This sets the type of font for text
font = {'family' : TypeOfFamily}  # This sets the type of font for text
LegendFontSize = 12
Lfont = {'family' : TypeOfFamily}  # This sets up legend font
Lfont['size']=LegendFontSize

Title = ''
TitleFontSize = 22
TitleFontWeight = "bold"  # "bold" or "normal"

Xlabel='E (eV)'   # X label
XFontSize=18          # X label font size
XFontWeight="normal"  # "bold" or "normal"
XScale="log"       # 'linear' or 'log'

YFontSize=18                    # Y label font size
YFontWeight="normal"            # "bold" or "normal"
YScale="log"                 # 'linear' or 'log'

################################################################
######################### Functions ############################
################################################################

def flux(E,Emt,Eme,E0,Ef):
    """
    Feed in energy as a function of ev not MeV
    """
    #Set constants
    C1=(E0**2)/(Emt**2)*np.exp(Emt/E0)
    C2=1
    C3=(Ef/Eme)*np.exp(Eme/Ef)*1/(np.sqrt(Eme/Ef))
    #Initialize flux
    F=np.zeros(len(E))
    FdE=np.zeros(len(E)-1)
    #Loop through all values of E and calculate Flux
    for i in range(0,len(E)):       
        if E[i]<=Emt:
            F[i]=C1*(E[i]/(E0**2))*np.exp(-E[i]/E0)
        if Emt<E[i] and E[i]<=Eme:
            F[i]=C2/E[i]
        if E[i]>Eme:
            F[i]=C3*(np.sqrt(E[i]/Ef)/Ef)*np.exp(-E[i]/Ef)
    
    return(F)



def plot(x,y,ax,Color,label,fig,Ylabel):
	#Plot X and Y
    ax.plot(x,y,
            linestyle="solid", #"solid","dashed","dash_dot","dotted","."
            marker="", # "*" "H" "h" "d" "^" ">"
# good ones http://matplotlib.org/1.4.1/api/markers_api.html for more
            color=Color,
            markersize=8,
            alpha=1,
            label=label)
    	
    #Log or linear scale?
    ax.set_xscale(XScale)
    ax.set_yscale(YScale)
    #Set Title
    fig.suptitle(Title,fontsize=TitleFontSize,
		 fontweight=TitleFontWeight,fontdict=font,ha='center')
    #Set X and y labels
    ax.set_xlabel(Xlabel,
		  fontsize=XFontSize,fontweight=XFontWeight,
		  fontdict=font)
    ax.set_ylabel(Ylabel,
		  fontsize=YFontSize,
		  fontweight=YFontWeight,
		  fontdict=font)
	
    return(fig,ax)

def Legend(ax):
	handles,labels=ax.get_legend_handles_labels()
	ax.legend(handles,labels,loc='best',
			fontsize=LegendFontSize,prop=font)
	return(ax)

def GETcsvFiles(directory):
    """
    This function gathers all files
    ending with ".csv" in a certain directory
    Note...NOT ".CSV" capitalization matters!
    """
    Filelist=[]
    for file in os.listdir(directory):
        if ".csv" in file:
            Filelist.append(file)
    return(Filelist)

def LoopTAPE(Protons,Isotope):
    ZAID=Protons+Isotope+"0"
    with open('../Origen2/TAPE9_BANK.inp') as f:
        content=f.readlines()

    for i in content:
        hold=i.split()
        if len(hold)>2:
                                   #want 600 libs not 1,2 or 3
            if ZAID in hold[1] and len(hold[0])>1:
                X_Section=hold[2]
                break
    return(X_Section)

def MinIndex(List):
    Count=0
    List2=[]
    for item in List:
        List2.append(item[0])
    Min=min(List2)
    for item in List:
        if item[0]==Min:
            break
        Count=Count+1
    return(Count)

def DetermineAverages(List):
    Count=0
    Averages=np.zeros(4)
    for item in List:
        for i in range(0,4):
            Averages[i]=Averages[i]+float(item[i])
        Count=Count+1
    Averages=Averages/Count
    return(Averages)
