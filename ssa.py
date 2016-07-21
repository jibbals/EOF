# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:22:03 2016

@author: jesse
"""

import numpy as np
from numpy import transpose as tp
from numpy import matmul as mm
import numpy.linalg as npla

class ssa:
    '''
    Read in a time series and produce things we want to run a 
        Singular Spectrum Analysis
    '''
    def __init__(self, ts, M=None):
        self.data=ts
        
        if M is None: 
            M=int(len(ts)/4.0)
        self.M = M
        N=len(ts)
        self.N = N
        
        # create M dimensional phase spaces
        X = np.zeros([M,N-M+1])
        X_norm = np.zeros([M,N-M+1])
        
        for i in range(M):
            X[i,:] = ts[i:(N-M+1+i)]
            X_norm[i,:] = X[i,:] - np.mean(X[i,:])
        self.trajectory = X
        
        # AUTO COVARIANCE MATRIX
        self.R = mm(X_norm, tp(X_norm)) / (N-M+1)
        self.cov = np.cov(X)
        
        # eigen stuff, Principal components
        self.evals, self.evecs = npla.eig(self.R)
        self.PC = mm(tp(self.evecs), X_norm)
        
        # scale this to unbias it, convolution end points are based on fewer additions
        RC=np.zeros([M,N])
        for col in range(M):
            # use convolution to get reconstructed components
            RCconv = np.convolve(self.PC[:,col],self.evecs)
            if col<M-1:
                RC[:,col]=RCconv/float(col)
            elif col<N-M+1:
                RC[:,col]=RCconv/float(M)
            elif col<N:
                RC[:,col]=RCconv/float(N-col+1)
        self.RC=RC
        assert (np.sum(np.abs(np.sum(RC,axis=0) - ts)) < 0.001).all(), "Reconstruction failed"
        
    def plot_evectors(self, N=5):
        '''
        Show N eigenvector amplitudes over time?
        '''
        assert False, "Not Implemented"

if __name__=="__main__":
    arr=np.array([1,2,2,3,4,3,1,1,4,3])
    ssa(arr)