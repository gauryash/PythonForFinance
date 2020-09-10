# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:05:13 2020

@author: yash gaur


objective: just want write basic py programe for time value of money
"""
def future_value(pv,r,n,freq):
    """
    docstring:
        this function simply compute future value of the given corpus amount 
        
        fv= future value
        pv= present value
        r=  rate of intrest/return ( in decimal )
        n=  period of compounding
        freq= frequency of compounding in a year 
        
    formula:
        fv=pv*(1+r/freq)^(n*freq)
    """
    r=r/100
    fv=pv*(1+(r/freq))**(n*freq)
    print(fv)

def present_value(fv,r,n,freq):
    """
    docstring:
        this function simply compute present value of the given corpus amount 
        
        fv= future value
        pv= present value
        r=  rate of intrest/return ( in decimal )
        n=  period of compounding
        freq= frequency of compounding in a year 
     
    formula:
        pv=fv/((1+r/freq)^(n*freq))
        
    """
    r=r/100
    pv=fv/((1+r/freq)**(n*freq))
    print(pv)

present_value(10000,10,1,1)
future_value(10000,10,1,1)
