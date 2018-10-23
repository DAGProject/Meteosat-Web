# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:51:14 2018

@author: mshem
"""

from numpy import asarray as ar
from numpy import dstack

from . import env
from . import astro
from . import stat

class Eumetsat():
    def __init__(self, verb=True):
        self.verb = verb
        self.eetc = env.etc(verb=self.verb)
        self.h5 = astro.H5(verb=self.verb)
        self.pstat = stat.Python(verb=self.verb)
        
        self.chList = {"1":"Ch1(VIS06)", "2":"Ch2(VIS08)", "3":"Ch3(VIS16)",
                       "4r":"Ch4(IR39)", "4":"Ch4(VIS39)", "5":"Ch5(WV62)",
                       "6":"Ch6(WV73)", "7":"Ch7(IR87)", "8":"Ch8(IR97)",
                       "9":"Ch9(IR108)", "10":"Ch10(IR120)",
                       "11":"Ch11(IR134)", "12":"Ch12(VISHRV)",
                       "Sinfo":"Slot_Info", "Tinfo":"TMet_Info"}
        
    def vssdfD(self, src):
        try:
            R = self.h5.data(src, self.chList["3"])
            RR = self.pstat.normalize(R, scale=255)
            
            G = self.h5.data(src, self.chList["2"])
            GG = self.pstat.normalize(G, scale=255)
            
            B = self.h5.data(src, self.chList["1"])
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 
            
    
    def ccsfD(self, src):
        try:
            R = self.h5.data(src, self.chList["2"])
            RR = self.pstat.normalize(R, scale=255)
            
            G = self.h5.data(src, self.chList["4r"])
            GG = self.pstat.normalize(G, scale=255)
            
            B = self.h5.data(src, self.chList["9"])
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 
            
    
    def sfD(self, src):
        try:
            R = self.h5.data(src, self.chList["2"])
            RR = self.pstat.normalize(R, scale=255)
            
            G = self.h5.data(src, self.chList["3"])
            GG = self.pstat.normalize(G, scale=255)
            
            B = self.h5.data(src, self.chList["4r"])
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 
            
            
    def scD(self, src):
        try:
            R1 = self.h5.data(src, self.chList["5"])
            R2 = self.h5.data(src, self.chList["6"])
            R = R1 - R2
            RR = self.pstat.normalize(R, scale=255)
            
            G1 = self.h5.data(src, self.chList["4"])
            G2 = self.h5.data(src, self.chList["9"])
            G = G1 - G2
            GG = self.pstat.normalize(G, scale=255)
            
            B1 = self.h5.data(src, self.chList["3"])
            B2 = self.h5.data(src, self.chList["1"])
            B = B1- B2
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 
            
    def cfcN(self, src):
        try:
            R1 = self.h5.data(src, self.chList["10"])
            R2 = self.h5.data(src, self.chList["9"])
            R = R1 - R2
            RR = self.pstat.normalize(R, scale=255)
            
            G1 = self.h5.data(src, self.chList["9"])
            G2 = self.h5.data(src, self.chList["4"])
            G = G1 - G2
            GG = self.pstat.normalize(G, scale=255)
            
            B = self.h5.data(src, self.chList["9"])
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 
            
            
    def dtccDN(self, src):
        try:
            R1 = self.h5.data(src, self.chList["10"])
            R2 = self.h5.data(src, self.chList["9"])
            R = R1 - R2
            RR = self.pstat.normalize(R, scale=255)
            
            G1 = self.h5.data(src, self.chList["9"])
            G2 = self.h5.data(src, self.chList["7"])
            G = G1 - G2
            GG = self.pstat.normalize(G, scale=255)
            
            B = self.h5.data(src, self.chList["9"])
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 
            
    def scjPVaDN(self, src):
        try:
            R1 = self.h5.data(src, self.chList["5"])
            R2 = self.h5.data(src, self.chList["6"])
            R = R1 - R2
            RR = self.pstat.normalize(R, scale=255)
            
            G1 = self.h5.data(src, self.chList["8"])
            G2 = self.h5.data(src, self.chList["9"])
            G = G1 - G2
            GG = self.pstat.normalize(G, scale=255)
            
            B = self.h5.data(src, self.chList["5"])
            BB = self.pstat.normalize(B, scale=255)
        
        
            td_arr = dstack(ar([RR, GG, BB], dtype=int).astype('uint8'))
            
            return td_arr
        except Exception as e:
            self.eetc.print_if(e) 

