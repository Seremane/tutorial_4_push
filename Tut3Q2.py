# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:56:39 2016

@author: ontibile
"""

#Question 2:
#write a class that contains masses and	x and y positions for a collection of particles
#the class should also contain a dictionary that can contain options.
#two entries in the dictionary should also be the number of particles and
#G(grativational constant).the class should also contain a method that
#calculates the potential energy of every particle,sum(Gm_1m_2/r_12)


import numpy

class Particles:
    def __init__(self,n=2000,G=1.0):
        self.x=numpy.random.randn(n)
        self.y=numpy.random.randn(n)
        self.m=numpy.ones(n)
        self.vx=numpy.zeros(n)
        self.vy=numpy.zeros(n)
        self.opts={}
        self.opts['n']=n
        self.opts['G']=G
    def get_potential(self):
        pot=numpy.zeros(self.opts['n'])
        for i in range(0,self.opts['n']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            r=numpy.sqrt(dx*dx+dy*dy)
            rinv=1.0/r
            rinv[i]=0  
            pot[i]=self.m[i]+numpy.sum(self.opts['G']*self.m[i]*self.m*rinv)
        return pot

if __name__=='__main__':
    part=Particles()
    pot=part.get_potential()
