# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:27:18 2018

@author: mshem
"""

from numpy import amax
from numpy import amin


from . import env


class Python():
    def __init__(self, verb=True):
        self.verb = verb
        self.eetc = env.etc(verb=self.verb)
        
    def normalize(self, in_arr, scale=1):
        try:
            minn = amin(in_arr)
            maxx = amax(in_arr)
            
            norm_ar = (in_arr - minn) / (maxx - minn)
            return norm_ar * scale
        except Exception as e:
            self.eetc.print_if(e)
