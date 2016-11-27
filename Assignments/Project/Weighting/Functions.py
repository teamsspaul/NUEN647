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

Title = 'Flux Spectra'
TitleFontSize = 22
TitleFontWeight = "bold"  # "bold" or "normal"

Xlabel='E (MeV)'   # X label
XFontSize=18          # X label font size
XFontWeight="normal"  # "bold" or "normal"
XScale="log"       # 'linear' or 'log'

Ylabel='$\phi$(E)$\cdot$E Normalized (n/cm$^{2}$s)'    # Y label
YFontSize=18                    # Y label font size
YFontWeight="normal"            # "bold" or "normal"
YScale="log"                 # 'linear' or 'log'

################################################################
######################### Functions ############################
################################################################

def flux(E,M_th,M_epi,B_th,B_fis):
    """
    Feed in energy as a function of ev not MeV
    """
    #Set constants
    C1=1/((M_th**2)*np.exp(-M_th/B_th))
    C2=1
    C3=1/((M_epi**(3/2))*np.exp(-M_epi/B_fis))
    #Initialize flux
    F=np.zeros(len(E))
    #Loop through all values of E and calculate Flux
    for i in range(0,len(E)):       
        if E[i]<=M_th:
            F[i]=C1*E[i]*np.exp(-E[i]/B_th)
        if M_th<E[i] and E[i]<=M_epi:
            F[i]=C2/E[i]
        if E[i]>M_epi:
            F[i]=C3*(E[i]**0.5)*np.exp(-E[i]/B_fis)
    return(F)

def flux2(E,Emt,Eme,E0,Ef):
    """
    Feed in energy as a function of ev not MeV
    """
    #Set constants
    C1=(E0**2)/(Emt**2)*np.exp(Emt/E0)
    C2=1
    #C3=(Ef/Eme)*np.exp(Eme/E0)*1/(np.sqrt(Eme/Ef))
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
            #F[i]=C3*(np.sqrt(E[i]/Ef)/Ef)*np.exp(-E[i]/E0)
            F[i]=C3*(np.sqrt(E[i]/Ef)/Ef)*np.exp(-E[i]/Ef)
        if i != len(E)-1:
            FdE[i]=F[i]*(E[i+1]-E[i])
            
    return(F,FdE)



def plot(x,y,ax,Color,label,fig):
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
