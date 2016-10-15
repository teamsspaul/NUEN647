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

import random as rn
import copy

################################################################
######################### Functions ############################
################################################################

def Remove(Not,List):
    List2=copy.copy(List)
    List2.remove(Not)
    return(List2)

def SelectOneRandomly(list):
    sum=len(list)
    rand=rn.uniform(0,1)
    for i in range(0,len(list)):
        if(rand> i/sum and rand <= (i+1)/sum):
            Selection=list[i]
    return(Selection)
