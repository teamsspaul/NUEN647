#!/usr/bin/env python3

############################################################
######################### Packages #########################
############################################################

import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import copy

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

Title = 'Comparison between two Gaussian distributions'
TitleFontSize = 22
TitleFontWeight = "bold"  # "bold" or "normal"

Xlabel='CPS/Volume'   # X label
XFontSize=18          # X label font size
XFontWeight="normal"  # "bold" or "normal"
XScale="linear"       # 'linear' or 'log'

Ylabel='Probability Density'    # Y label
YFontSize=18                    # Y label font size
YFontWeight="normal"            # "bold" or "normal"
YScale="linear"                 # 'linear' or 'log'

Range=4 # Range of sigmas to extend outside PDF
N=100   # Number of points in each plot

#############################################################
######################### Functions #########################
#############################################################

def CPS_Vol_Data(filename):
	"""
	This function will store in a list of list
	as a string, CPS/volume data with sigma values.
	I am sorry, that is not terribly descriptive,
	but its what I got
	"""
	
	#Open files
	with open(filename) as f:
		content=f.readlines()
	List=[]
	for i in content:
		i=i.replace("\n","")
		i=i.replace("\t"," ")
		i=i.split()
		List.append(i)
	return(List)

def find_nearest_index(array,value,number):
	"""
	This function will find the nth 'number' nearest 
	to a number from an array.
	"""
	arraycopy=copy.copy(array)
	for i in range(0,number-1):
		#arraycopy.remove(array[(np.abs(array-value)).argmin()])
		index=np.argwhere(arraycopy==arraycopy[(np.abs(arraycopy-value)).argmin()])
		arraycopy=np.delete(arraycopy,index)
	inx=(np.abs(arraycopy-value)).argmin()
	#return arraycopy[inx]
	return(inx)

def plotPDF(ax,Color,mean,sigma,label,fig):
	#Set up x and y array:
	x=np.linspace(mean-Range*sigma,mean+Range*sigma,N)
	y=mlab.normpdf(x,mean,sigma)
	#Plot X and Y
	ax.plot(x,y,
			linestyle="solid", #"solid","dashed","dash_dot","dotted","."
			marker="", # "*" "H" "h" "d" "^" ">" good ones http://matplotlib.org/1.4.1/api/markers_api.html for more options
			color=Color,
			markersize=8,
			alpha=1,
			label=label)
	#Give lines for sigma values
	Sigmas=[mean-2*sigma,mean-sigma,mean,mean+sigma,mean+2*sigma]
	for i in range(0,len(Sigmas)):
		index=find_nearest_index(x,Sigmas[i],1)
		ys=np.linspace(0,y[index],N)
		xs=np.ones([N,1])*Sigmas[i]
		ax.plot(xs,ys,linestyle="dashed",marker="",color=Color,
				markersize=8,alpha=0.1)
	
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
	
def Calc_N_Plot_MDA(ax,u_I,t1,V1,oV1,u_F,t2,V2,oV2,o_I):
	oB=(u_I/(t1*V1)+((oV1*u_I)/V1)**2)**0.5
	Err=1
	Guess=abs(u_I-u_F)
	while Err>0.001:
		oT=(Guess/(t2*V2)+((oV2*Guess)/V2)**2)**0.5
		MDA=2.33*oB+1.64*((oT**2+oB**2)**0.5)
		Err=abs(MDA-Guess)
		Guess=MDA
	CPS_MDA=u_I-MDA
	xs=np.ones([N,1])*CPS_MDA
	x=np.linspace(u_I-Range*oB,u_I+Range*oB,N)
	y=mlab.normpdf(x,u_I,oB)
	ys=np.linspace(0,max(y),N)
	ax.plot(xs,ys,linestyle='dashed',color='black',alpha=1,label="MDA")
	return(ax)
	
def Legend(ax):
	handles,labels=ax.get_legend_handles_labels()
	ax.legend(handles,labels,loc='best',
			fontsize=LegendFontSize,prop=font)
	return(ax)