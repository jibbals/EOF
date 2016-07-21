# -*- coding: utf-8 -*-

import csv

def get_TS_region(filename='TS_LargerNSW.csv'):
    '''
    Read the corrected time series data produced by the OMI swaths
        (these are created in my OMI project folder.)
    '''
    with open(filename,'r') as inf:
        reader=csv.reader(inf)
        data=list(reader)
        t = [ d[0] for d in data ] # dates
        #h = [ d[1] for d in data ] # old averages
        hcor = [ d[2] for d in data ] # corrected averages
        c = [ d[3] for d in data ] # entries averaged
    return t,hcor,c