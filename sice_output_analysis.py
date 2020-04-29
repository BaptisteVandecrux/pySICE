# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:35:44 2020
%matplotlib qt
@author: bav
"""
from IPython import get_ipython
ipython = get_ipython()
ipython.magic("matplotlib qt")

import numpy as np
import rasterio as rio
import bav_lib as bl
import matplotlib.pyplot as plt
import os
plt.close('all')

#%% Running sice
InputFolder = 'out/SICE_2020_py1.4/'

ipython.magic('run sice.py '+InputFolder)

#% Plotting output
ipython.magic("matplotlib inline")

try:
    os.mkdir(InputFolder+'plots')
except:
    print('folder exist')
    
fig,ax=bl.heatmap_discrete(rio.open(InputFolder+'diagnostic_retrieval.tif').read(1),
                        'diagnostic_retrieval ')
ax.set_title(InputFolder)
fig.savefig(InputFolder+'plots/diagnostic_retrieval.png',bbox_inches='tight')

var_list = ('albedo_bb_planar_sw','albedo_bb_spherical_sw','r0')
for i in range(len(var_list)):
    var_1 = rio.open(InputFolder+var_list[i]+'.tif').read(1)
    plt.figure(figsize=(10,15))
    bl.heatmap(var_1,var_list[i], col_lim=(0, 1) ,cmap_in='jet')
    plt.title(InputFolder)
    plt.savefig(InputFolder+'plots/'+var_list[i]+'.png',bbox_inches='tight')
    plt.close()
    
var_list = ('O3_SICE', 'grain_diameter', 'snow_specific_area',
            'al','conc')
for i in range(len(var_list)):
    var_1 = rio.open(InputFolder+var_list[i]+'.tif').read(1)
    plt.figure(figsize=(10,15))
    bl.heatmap(var_1,var_list[i],cmap_in='jet')
    plt.title(InputFolder)
    plt.savefig(InputFolder+'plots/'+var_list[i]+'.png',bbox_inches='tight')
    plt.close()

for i in np.arange(21):
    var_name = 'albedo_spectral_spherical_'+ str(i+1).zfill(2)
    var_1 = rio.open(InputFolder+var_name+'.tif').read(1)
    plt.figure(figsize=(10,15))
    bl.heatmap(var_1,var_name, col_lim=(0, 1) ,cmap_in='jet')
    plt.title(InputFolder)
    plt.savefig(InputFolder+'plots/'+var_name+'.png',bbox_inches='tight')
    plt.close()
    var_name = 'albedo_spectral_planar_'+ str(i+1).zfill(2)
    var_1 = rio.open(InputFolder+var_name+'.tif').read(1)
    plt.figure(figsize=(10,15))
    bl.heatmap(var_1,var_name, col_lim=(0, 1) ,cmap_in='jet')
    plt.title(InputFolder)
    plt.savefig(InputFolder+'plots/'+var_name+'.png',bbox_inches='tight')
    plt.close()
    var_name = 'rBRR_'+ str(i+1).zfill(2)
    var_1 = rio.open(InputFolder+var_name+'.tif').read(1)
    plt.figure(figsize=(10,15))
    bl.heatmap(var_1,var_name, col_lim=(0, 1) ,cmap_in='jet')
    plt.title(InputFolder)
    plt.savefig(InputFolder+'plots/'+var_name+'.png',bbox_inches='tight')
    plt.close()
ipython.magic("matplotlib qt")
#%% ========== Compare two folders ==================

plt.close('all')
plt.rcParams.update({'font.size': 18})

InputFolder_1 = 'SICE_2020_py1.4/'
InputFolder_2 = 'SICE_2020_py1.4/fortran/'

tmp=bl.heatmap_discrete(rio.open('out/'+InputFolder_1+'diagnostic_retrieval.tif').read(1),
                        'isnow_py '+InputFolder_1)
try: tmp=bl.heatmap_discrete(rio.open('out/'+InputFolder_2+'diagnostic_retrieval.tif').read(1), 
                        'isnow_py '+InputFolder_2)
except:
    print('invalid diagnostic_retrieval in '+InputFolder_2)
    
plt.figure()
tmp=bl.heatmap(rio.open('out/'+InputFolder_1+'albedo_bb_planar_sw.tif').read(1),'albedo_bb_planar_sw')

var_list = ('albedo_bb_planar_sw','albedo_bb_spherical_sw')
for i in range(len(var_list)):
    var_1 = rio.open('out/'+InputFolder_1+var_list[i]+'.tif').read(1)
    var_2 = rio.open('out/'+InputFolder_2+var_list[i]+'.tif').read(1)
    diff = var_1 - var_2
    plt.figure(figsize=(10,15))
    bl.heatmap(diff,InputFolder_1 + '  -  ' + InputFolder_2)
    plt.title(var_list[i])
    plt.savefig('Plots/'+var_list[i]+'_diff.png',bbox_inches='tight')
    
for i in np.arange(21):
    var_name = 'albedo_spectral_planar_'+ str(i+1).zfill(2)
    var_1 = rio.open('out/'+InputFolder_1+var_name+'.tif').read(1)
    var_2 = rio.open('out/'+InputFolder_2+var_name+'.tif').read(1)
    diff = var_1 - var_2
    plt.figure(figsize=(10,15))
    bl.heatmap(diff,InputFolder_1 + '  -  ' + InputFolder_2)
    plt.title(var_name)
    plt.savefig('Plots/'+var_name+'_diff.png',bbox_inches='tight')

#%% Comparing with Fortran output

# bl.heatmap(rio.open('out/'+InputFolder+'diagnostic_retrieval.tif').read(1),'isnow_py')
# bl.heatmap(rio.open('out/'+InputFolder_2+'isnow.tif').read(1)-rio.open('out/'+InputFolder_1+'isnow.tif').read(1),'isnow_f-isnow_py')