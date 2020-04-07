# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 19:55:39 2018

@author: msh
"""
from astropy.time import Time

from h5py import File as h5file

import numpy as np

from . import env

class H5():
    def __init__(self, verb=True):
        self.verb = verb
        self.eetc = env.etc(verb=self.verb)
        
    def list_of_channels(self, src):
        """
        Returns all or dataset names in H5 file
        
        @param src: Source File Path.
        @type src: str
        
        @return: list
        """
        try:
            with h5file(src,'r') as hf:
                dataset_names = list(hf.keys())
               
            return dataset_names
        
        except Exception as e:
            self.eetc.print_if(e)
            
    def data(self, src, dataset):
        the_file = h5file(src, mode="r")
        return np.asarray(the_file[dataset])

class time():
    def __init__(self, verb=True):
        self.verb = verb
        self.eetc = env.etc(verb=self.verb)
        
    def jd(self, timestamp):
        """
        Calculates JD
        
        @param timestamp: Timestamp
        @type timestamp: str
        
        @return: float
        """
        if "T" not in timestamp:
            timestamp = str(timestamp).replace(" ", "T")
        
        t_jd = Time(timestamp, format='isot', scale='utc')

        return(t_jd.jd)
        
    def mjd(self, timestamp):
        """
        Calculates JD
        
        @param timestamp: Timestamp
        @type timestamp: str
        
        @return: float
        """
        if "T" not in timestamp:
            timestamp = str(timestamp).replace(" ", "T")
        
        t_jd = Time(timestamp, format='isot', scale='utc')

        return(t_jd.mjd)
