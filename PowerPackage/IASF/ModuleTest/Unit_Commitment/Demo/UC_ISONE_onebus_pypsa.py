# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:59:34 2018

@author: Yichen Zhang

This module uses the data from matpower/pypower in pypsa.
For the data format, please cross reference between matpower manual and pypsa attributes in cvs.
"""

import pypsa
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
font = {'family' : 'Times New Roman',
        'weight' : 'normal',
        'size'   : 12}
matplotlib.rc('font', **font)


"""
Get the ISO level time-series load data from csv
This data set should be generated by modules developed by BNL
"""
# read ISO level load data
LoadData=pd.read_csv('P_Load.csv')  # pandas dataframe
#LoadData1=pd.read_csv('P_Load1.csv')
PL_norm=LoadData.iloc[:,1] # normal, type: series
number_hour=len(PL_norm)  # scheduling horizon



""" 
Import the studied system data using matpower/pypower format
"""
import case_39bus as case 
ppc=case.case39() # dictionary data

# get size of bus, line and generator
number_bus=ppc['bus'].shape[0] # shape returns (row,column)
number_gen=ppc['gen'].shape[0]

# calculate base
base_mva=ppc['baseMVA']     # MVA
base_KV=ppc['baseKV']       # KV
base_KA=base_mva/base_KV    # KA
base_Ohm=base_KV/base_KA    # Ohm
base_Siemens=1/base_Ohm     # Siemens


"""
Load data distribution
The load data (active power) is distributed according the static load data of standard IEEE 39-bus.
For now we are not sure this is the way that we want to perform our attack.
"""

# get static load data from standard IEEE 39-bus system (unit: MW/Mvar)
load_p=ppc['bus'][:,2]
load_q=ppc['bus'][:,3]


# create iterator for bus, generator and horizon
iter_bus=np.arange(0,number_bus)
iter_gen=np.arange(0,number_gen)
iter_hour=np.arange(0,number_hour)


"""
Convert matrxi-based data structure of matpower/pypower format to object-based pypsa format
"""
# build network object
nu = pypsa.Network()

# scheduling horizon
nu.set_snapshots(range(number_hour))

# create buses
# add(class name, customized name,...)
nu.add("Bus","ISO_NE") # {} is to get the input of format method


# create generator
for i in range(number_gen):
    nu.add("Generator","Generator {}".format(ppc['gen'][i,0]),
           bus="ISO_NE",
           p_nom=base_mva, # MW in both PyPsa and PyPower
           p_max_pu=ppc['gen'][i,8]/base_mva,  # p.u. in PyPsa, MW in PyPower
           p_min_pu=ppc['gen'][i,9]/base_mva, 
           committable=True,
           start_up_cost=0,
           shut_down_cost=0,
           marginal_cost=ppc['gencost'][i,2] # pd.Series(ppc['gencost'][i,4:7]) # ppc['gencost'][i,4:6]
           )
print(nu.generators)

# create loads
nu.add("Load","Load {}".format(ppc['bus'][i,0]),bus="ISO_NE",p_set=PL_norm)

# solve linear optimal power flow
nu.lopf(nu.snapshots,solver_name="glpk")



"""
show results
"""
# show in console
print(nu.generators_t.status)
print(nu.generators_t.p)

# plot load
plt.figure(figsize=(12,5))
plt.xlabel('time (hour)')
plt.ylabel('power (MW)')
plt.plot(PL_norm,'b',linewidth=3,label='Normal')
plt.title('Forcasted Load')
plt.legend()
plt.show()

# plot 2D
plt.figure(figsize=(12,5))
plt.xlabel('time (hour)')
plt.ylabel('power (MW)')
for i in range(number_gen):
    plt.step(iter_hour,nu.generators_t.p.iloc[:,i],label='Gen {}'.format(i),linewidth=3)
plt.title('Generator Scheduling')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5)
plt.show()

# Plot: 3D
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(111, projection='3d')
for i in iter_gen:
    xs = iter_hour
    ys = nu.generators_t.p.iloc[:,i]
    ax.bar(xs, ys, zs=int(ppc["gen"][i,0]), zdir='y', alpha=0.7, label='Gen {}'.format(int(ppc["gen"][i,0])))
ax.set_xlabel('Hours')
ax.set_ylabel('Generator Index')
ax.set_zlabel('Power')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5)
plt.show()

#plt.figure(figsize=(11,8))
#plt.subplot(211)
##plt.xlabel('time (hour)')
#plt.ylabel('power (MW)')
#plt.step(nu.generators_t.p.iloc[:,0],'b',label='Coal',linewidth=4)
#plt.step(nu.generators_t.p.iloc[:,1],'r',label='Gas',linewidth=4,linestyle='--')
#plt.title('Unit Commitment Under Normal Condition')
#plt.legend()
#plt.show()
#plt.subplot(212)
#plt.xlabel('time (hour)')
#plt.ylabel('power (MW)')
#plt.step(nu1.generators_t.p.iloc[:,0],'b',label='Coal',linewidth=4)
#plt.step(nu1.generators_t.p.iloc[:,1],'r',label='Gas',linewidth=4,linestyle='--')
#plt.title('Unit Commitment Under Attack')
#plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
#plt.legend()
#plt.show()
