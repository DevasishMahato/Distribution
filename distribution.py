#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:34:33 2019

@author: devashishm
"""

from matplotlib.pyplot import plot
import numpy as np
import pandas as pd
class Plot():
    #def __init__(self):
    
    def __quantity__(self):
        for length in self.lengths:
            for i in range(self.__batches__):
                if length >= self.stats['start'][i] and length < self.stats['end'][i]:
                    self.stats['value'][i] += 1
        return
            
    def __range__(self):
        '''        The values of end[] are not to excluded while iterating        '''
        start = []
        end = []
        self.__batches__ = 0
        for s in range(self.min_length,self.max_length,self.batch_size):
            e = s + self.batch_size
            start.append(s)
            end.append(e)
            self.__batches__ += 1
        return ([np.array(start),np.array(end)])
    
    def distribute(self,lengths, batch_size = 10):
        self.lengths = lengths
        self.max_length = int(np.max(self.lengths))
        self.min_length = int(np.min(self.lengths))
        self.batch_size = batch_size
        start, end = self.__range__()
        self.stats = pd.DataFrame(np.array([]))
        self.stats['start'] = start
        self.stats['end'] = end
        self.stats['value'] = np.zeros([self.__batches__])
        self.__quantity__()
        return self.stats
    
    def plot_stat(self, lengths, batch_size = 10):
        self.distribute(lengths, batch_size)
        plot(self.stats['value'])
        