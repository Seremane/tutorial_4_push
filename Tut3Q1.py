# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 02:21:58 2016

@author: ontibile
"""

#Question 1:
#complete the complex definition to support -,*, and /
#(__sub__,__mul__,and __div__).	recall that a/b=a*conj(b)/(b*conj(b))
#show from a few sample cases that your functions work

class complex:
	def __init__(self,r=0,c=0):
		self.r=r
		self.i=c
	def copy(self):
		return complex(self.r,self.i)

	def __add__(self,val):
		ans=self.copy()
		if isinstance(val,complex):
			ans.r=ans.r+val.r
			ans.c=ans.i+val.i
		else:
			ans.r=ans.r+val
		return ans

	def __mul__(self,val):
		ans=self.copy()
		if isinstance(val,complex):
			ans.r=self.r*val.r-self.i*val.i
			ans.i=self.r*val.i+self.i*val.r
		else:
			ans.r=ans.r*val
			ans.i=ans.i*val
		return ans

	def __sub__(self,val):
		ans=self.copy()
		if isinstance(val,complex):
			ans.r=ans.r+val.r
			ans.c=ans.i-val.i
		else:
			ans.r=ans.r-val
		return ans

	def __div__(self,val):
		
		if isinstance(val,complex):
			val=val.copy
			val.i=-1*val.i
			ans=self*val
			myabs=val.r**2+val.i**2
			ans=ans*(1.0/myabs)
		else:
			ans=self*(1.0/val)
		return ans

	def __repr__(self):
		if (self.i<0):
			return repr(self.r)+' - '+repr(-1*self.i) +'i'
		else:
			return repr(self.r)+' + '+repr(-1*self.i) +'i'
	
if __name__=="__main__":
	
	k=complex(3.0,10)
	x=complex(2.0,5)
	
	print k+x
	print k-x
	print k*x
	print k/5


