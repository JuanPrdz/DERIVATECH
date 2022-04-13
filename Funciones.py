# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 17:52:23 2022

@author: ivana
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import scipy.stats as st



def delta_call(St,k,T,t,r,sigma):
    d1 = (np.log(St/k)+r*(T-t)+ (sigma**2*(T-t))/2)/(sigma*np.sqrt(T-t))
    delta = st.norm.cdf(d1,0,1)
    return delta

def delta_put(St,k,T,t,r,sigma):
    md1 = -((np.log(St/k)+r*(T-t)+ (sigma**2*(T-t))/2)/(sigma*np.sqrt(T-t)))
    delta = -st.norm.cdf(md1,0,1)
    return delta

def vega(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    vega = St*np.sqrt(T-t)*np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi))
    return vega


def theta_call(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    d2= (np.log(St/k)+(r -0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    theta = -(St*(np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi)))*sigma)/(2*np.sqrt(T-t)) - r*k*np.exp(-r*(T-t))*st.norm.cdf(d2,0,1)
    return theta

def theta_put(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    md2= -((np.log(St/k)+(r -0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t)))
    theta = -(St*(np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi)))*sigma)/(2*np.sqrt(T-t)) + r*k*np.exp(-r*(T-t))*st.norm.cdf(md2,0,1)
    return theta


def rho_call(St,k,T,t,r,sigma):
    d2= (np.log(St/k)+(r -0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    rho = (T-t)*k*np.exp(-r*(T-t))*st.norm.cdf(d2,0,1)
    return rho

def rho_put(St,k,T,t,r,sigma):
    md2= -((np.log(St/k)+(r -0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t)))
    rho = -((T-t)*k*np.exp(-r*(T-t))*st.norm.cdf(md2,0,1))
    return rho


def gamma(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    gamma = np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi))
    return gamma

def vanna(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    vega= St*np.sqrt(T-t)*np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi))
    vanna = (vega/St)*(1-(d1/(sigma*np.sqrt(T-t))))
    return vanna


def volga(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    d2= (np.log(St/k)+(r -0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    vega= St*np.sqrt(T-t)*np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi))
    volga = vega*((d1*d2)/sigma)
    return volga


def color(St,k,T,t,r,sigma):
    d1= (np.log(St/k)+(r +0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    d2= (np.log(St/k)+(r -0.5*sigma**2)*(T-t))/(sigma*np.sqrt(T-t))
    color= -((np.exp(-0.5*d1**2)/(np.sqrt(2*np.pi)))/(2*St*(T-t)*sigma*np.sqrt(T-t)))*(1+((2*r*(T-t)-d2*sigma*np.sqrt(T-t)*d1)/(2*(T-t)*sigma*np.sqrt(T-t))))
    return color