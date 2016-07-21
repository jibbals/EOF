# -*- coding: utf-8 -*-

import numpy as np
import numpy.linalg as npla

class eof:
    def __init__(self, data):
        # data array, 2 dimensional with rows as time series
        # self.rawdata=data
        # normalised somehow
        self.data = data
        
        # Covariance array
        self.R=np.cov(data)
        
        # eigen-values, vectors ( already normalised )
        evals,evecs = npla.eig(self.R) 
        self.evals, self.evecs = evals,evecs
        
        # Principal Components
        self.PC=np.matmul(np.transpose(evecs),data) 
        assert (np.abs(data-np.matmul(evecs,self.PC)) < 0.001).all() , "something is bad"
        
    def plot_evectors(self):
        '''
        '''
        print("TO BE IMPLEMENTED")
    
    
# Examples
arr=np.array([[1,2,3,2,3,4],[2,3,5,1,2,4]])
a=eof(arr)
