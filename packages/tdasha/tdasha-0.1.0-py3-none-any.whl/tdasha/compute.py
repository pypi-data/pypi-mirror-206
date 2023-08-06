# -*- coding: utf-8 -*-
"""
@author: ftong
"""
import numpy as np
import bisect #used for bisecting list of events by start time
from tdasha.window import Window

def time_window_length(t_input, time_unit='day'):
        
    t = assure_order(t_input, chrono='forward')
    
    n_events = len(t) # number of events in the catalog
    t_start = t[0] # time of first event, assumes event list sorted by time
    t_end = t[-1] # time of last event
    time_span= t_end-t_start #length of data set between first and last event
    
    if time_unit == 'day':
        time_span = time_span / 86400 #convert time span from seconds to days
    elif time_unit == 'hour':
        time_span = time_span / 3600 #convert time span from seconds to hours
    elif time_unit == 'minute':
        time_span = time_span / 60 #convert time span from seconds to minutes

    activity_rate = n_events / time_span
    
    window_length = np.ceil(80 / activity_rate) # use window length such that there are 80 events per window
    
    return window_length,activity_rate



def comp_exc_prob_CNE(M_input, Mc, rum, t_input, t_unit, t_step, t_period, win_size, M_max=None, ci = False, **kwargs):

    t, M = assure_order(t_input, chrono='backward', x=M_input)
    
    t_start = t[0]
    t_end = t[-1]
    
    # convert step size to seconds
    if t_unit == 'day':
        t_step = t_step*86400 
    elif t_unit == 'hour':
        t_step = t_step*3600 
    elif t_unit == 'minute':
        t_step = t_step*60 
    
    windows = np.arange(t_start,t_end,-t_step)
    exc_pr = [] # exceedance probability for each window
    exc_pr_ci = [] # confidence interval for exc_pr
    tc = [] # timestamp of end of each window

    # Iterate through all the windows, select desired number of events and compute exceedance probability
    nwin = len(windows)
    print("Processing window...")

    for idx, tt in enumerate(windows): # tt is the end time of each window

        print(idx+1, "of", nwin)

        j = len(t) - bisect.bisect_right(t[::-1], tt)

        # fetch the next win_size number of events after event t[j], event times and their magnitudes
        T_sel = t[j:j+win_size] # event times for window
        M_sel = M[j:j+win_size] # event magnitudes for window
        
        if len(T_sel) < win_size:
            print("Not enough events left to fill window starting at", tt)
            break

        win = Window(Mc, rum, M_sel, T_sel, t_unit, t_step, t_period, **kwargs) 
                
        exc_pr.append(win.exc_prob())
        
        if ci: # estimate confidence interval
            exc_pr_ci.append(win.exc_prob_ci(**kwargs))
            
        tc.append(tt)
        
        # print(exc_pr)
        # print(exc_pr_ci) 
        # break
        
        
    exc_pr.reverse()
    exc_pr_ci.reverse()
    tc.reverse()
    
    print("Exceedance Probability computed from", tc[0], "to", tc[-1])
    
    return exc_pr, exc_pr_ci, tc



def comp_exc_prob_CTL(M_input, Mc, rum, t_input, t_unit, t_step, t_period, win_size, M_max=None, ci = False, **kwargs):
        
    t, M = assure_order(t_input, chrono='backward', x=M_input)
    
    t_start = t[0]
    t_end = t[-1]
    
    # convert from step size and window size to seconds
    if t_unit == 'day':
        t_step = t_step*86400 
        win_size = win_size*86400 
    elif t_unit == 'hour':
        t_step = t_step*3600 
        win_size = win_size*3600 
    elif t_unit == 'minute':
        t_step = t_step*60 
        win_size = win_size*60
    
    windows = np.arange(t_start,t_end,-t_step)
    exc_pr = [] # exceedance probability for each window
    exc_pr_ci = [] # confidence interval for exc_pr
    tc = [] # timestamp of end of each window
        
    # Iterate through all the windows, select desired number of events and compute exceedance probability
    # TODO: replace with iterator?
    
    nwin = len(windows)
    print("Processing window...")
    for idx, tt in enumerate(windows): # tt is the end time of each window
        
        print(idx+1, "of", nwin)
        
        j1 = len(t) - bisect.bisect_right(t[::-1], tt)
        j2 = len(t) - bisect.bisect_right(t[::-1], tt-win_size)
        
        # fetch all events within the time window
        T_sel = t[j1:j2] # event times
        M_sel = M[j1:j2] # event magnitudes
        
        num_events = len(T_sel)

        if num_events<50:
            # print("Insufficient events at time window", tt)
            exc_pr.append(float("NaN")) # insufficient events, set to null
            exc_pr_ci.append([float("NaN"),float("NaN")]) # insufficient events, set to null
            tc.append(tt)
            continue            # move on to next window
        
        win = Window(Mc, rum, M_sel, T_sel, t_unit, t_step, t_period, **kwargs)
        
        exc_pr.append(win.exc_prob())
        
        if ci: # estimate confidence interval
            exc_pr_ci.append(win.exc_prob_ci(**kwargs))
            
        tc.append(tt)
         
        # print(exc_pr)
        # print(exc_pr_ci) 
        # break
    
    exc_pr.reverse()
    exc_pr_ci.reverse()
    tc.reverse()
    
    print("Exceedance Probability computed from", tc[0], "to", tc[-1])
    
    return exc_pr, exc_pr_ci, tc



def assure_order(t, chrono, x=[None]):
    
    # t is a list of time values, x must be a numpy array
    
    # check ordering of time based on first two events and reverses it if necessary
    if chrono=="forward" and t[1]<t[0] or chrono=="backward" and t[1]>t[0]:
        t_new = list(reversed(t))
        
        if len(x)>1: # x provided, so reverse also x then return both t and x
            x_new = np.flip(x)
            return t_new, x_new
        
        else: # x is empty, return only t
            return t_new

    
    else: # ordering is already as desired based on test
    
        if len(x)>1: # x provided, so return both t and x
            return t, x
        
        else: # x is empty, return only t
            return t

