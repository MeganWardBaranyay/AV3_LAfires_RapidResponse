#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 04:44:49 2020

@author: sousa
"""

#%%

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pandas as pd

import rasterio
#import gdal
from rasterio.plot import show
#from osgeo import gdal
import time

import umap


#%%


test = '/Volumes/GEOG/Structure_classification/UMAP/AV3_Eaton_mosaic_ROI_masked_structures_0'

#maskValue = Xsum[0,0]
maskValue = 0

image = rasterio.open(test)

X = image.read()
X = X.astype('float32')
#X = X[:,0::1000,0::100]

#X = X[:,0::10, 0::10]
#X = X[[1,2,3,4,5,6,7,9,10],:,:]

#outfile = '/Users/dansousa/Downloads/tsne/BigMosaicx3_x10_y10_no1_no8a_int_data.tif'

sample_factor = 1


X = X[:,::sample_factor,::sample_factor]

X = X.astype('float32')

# X.tofile(test + '_sub'+str(sample_factor)+'xy_data')

#%%

Xsum = np.sum(X,axis=0)

Xsub = X[:, Xsum != maskValue]
#Xsub = X[:,Xsum > -999]

X = Xsub

plt.plot(X[:,100])

# X.tofile(test + '_sub'+str(sample_factor)+'xy_data_dense')

plt.plot(X[:,100])

X = np.transpose(X)


#%%

for i in np.arange(2,4):
    
#    for j in (50, 30, 10):
     for j in (30,):
#     for j in (15, 7, 5):        
#     for j in (5, 7, 8, 10, 15, 30, 50):        
    # for j in np.arange(150,151):
        
        X = image.read()
        
    #    sample_factor = 1
        
        X = X[:,::sample_factor,::sample_factor]
        
        X = X.astype('float32')
        
        X = np.reshape(X, [X.shape[0], X.shape[1]*X.shape[2]])
        
        Xsum = np.sum(X,axis=0)
        
        Xsub = X[:, Xsum != maskValue]
    
        #Xsub = X[:,Xsum > -999]
        
        X = Xsub
        
        plt.plot(X[:,100])
        
        X = np.transpose(X)
        
        start = time.time()
        
        neighbors = j
        dist = 0.1
        metricChoice = "euclidean"
        comps = i
        
        Y = umap.UMAP(n_neighbors= neighbors,
                      min_dist = 0.1,
                      metric=metricChoice,
                      n_components = comps,
                      verbose=True).fit_transform(X)
        
        end = time.time()
        
        #Y.tofile(test + '_sub'+str(sample_factor)+'xy_2d_p0' + str(j) + '_r0' + str(i))
       
        X = image.read()
    
    #    sample_factor = 1
        
        X = X[:,::sample_factor,::sample_factor]
        
        Xsum = np.sum(X,axis=0)
        
        X = X.astype('float32')
        
        Y_sparse = X
    
        Y_sparse = Y_sparse[np.arange(0,comps),:]
                
        Y_sparse[:, Xsum != maskValue] = Y.transpose()
        
        # Y_sparse.tofile(test + '_sub'+str(sample_factor)+'xy_2d_sparse_UMAP_n' + str(int(neighbors)) + '_d' + str(int(dist*10)) + '_M' + str(metricChoice[0:3]) + '_d' + str(int(comps)) + '_r0' + str(i))
        Y_sparse.tofile(test + '_again_UMAP_n' + str(int(neighbors)) + '_d' + str(int(comps)))
    
        print(end-start)



#%%



#%%
