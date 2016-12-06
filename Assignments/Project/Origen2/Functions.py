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


#############################################################
######################### Variables #########################
#############################################################

N=10
Nbins=3


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

Xlabel='Time (d)'   # X label
XFontSize=18          # X label font size
XFontWeight="normal"  # "bold" or "normal"
XScale="linear"       # 'linear' or 'log'

YFontSize=18                    # Y label font size
YFontWeight="normal"            # "bold" or "normal"
YScale="linear"                 # 'linear' or 'log'




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
    plt.savefig("PLOTS/"+Element+'HIST.pdf')

def PlotHistSave2(Error,Ntimes,Element,Nbins):
    Element=Element.split('.')[0]

    if Element[1].isalpha():
        E=Element[0:2]
        I=Element[2:5]
    else:
        E=Element[0]
        I=Element[1:4]

    if len(E)>1:
        E=E[0]+E[1].lower()
    print(E,I)
    
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_xlabel(r'$^{'+I+'}$'+E,fontsize=16)
    ax.set_ylabel(r'Count out of '+str(Ntimes),fontsize=18)
    ax.hist(Error,Nbins,color='green',alpha=0.7,edgecolor='black')
    
    plt.savefig("PLOTS/"+Element+'Post_HIST.pdf')


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
                    


def plot(x,y,ax,Color,label,fig,Element):
    Element=Element.split('.')[0]

    if Element[1].isalpha():
        E=Element[0:2]
        I=Element[2:5]
    else:
        E=Element[0]
        I=Element[1:4]
    if len(E)>1:
        E=E[0]+E[1].lower()
    
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
        	 fontweight=TitleFontWeight,fontdict=font,
                 ha='center')
    #Set X and y labels
    Ylabel=r'$^{'+I+'}$'+E+" (g)"
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
