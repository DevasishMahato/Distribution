#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:34:33 2019

@author: devashishm
"""

from matplotlib.pyplot import plot
import numpy as np
import pandas as pd
from sys import stdout
class Plot():
    #def __init__(self):
    
    def __quantity__(self):
        limit = len(self.lengths)
        for i , length in enumerate(self.lengths):
            percentage = round(100*(i/limit))
            stdout.write(f'\r {i} / {limit} : {percentage}')
            self.stats['value'][int(length/self.batch_size)] += 1
        return
            
    def __range__(self):
        '''        The values of end[] are not to excluded while iterating        '''
        start = []
        end = []
        if (self.max_length - self.min_length) % self.batch_size == 0 :
            self.__batches__ = (self.max_length - self.min_length) / self.batch_size
        else:
            self.__batches__ = int((self.max_length - self.min_length) / self.batch_size) + 1
        start = [self.min_length + i * self.batch_size for i in range(self.__batches__)]
        end = [self.min_length + (i+1) * self.batch_size for i in range(self.__batches__)]
#        for s in range(self.min_length,self.max_length,self.batch_size):
#            e = s + self.batch_size
#            start.append(s)
#            end.append(e)
#            self.__batches__ += 1
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
        self.stats.drop(0,axis=1)
        plot(self.stats['value'])
        