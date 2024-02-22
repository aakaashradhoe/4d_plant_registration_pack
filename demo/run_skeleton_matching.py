#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script provides a demo for the skeleton matching (correspondence estimation) between a pair of skeletons.
"""

import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from plant_registration import skeleton as skel
from plant_registration import skeleton_matching as skm
from plant_registration import visualize as vis
import numpy as np

def plot_skeleton(ax, S, color='blue'):
    # ax = fh.add_subplot(projection='3d')
    ax.scatter(S.XYZ[:,0], S.XYZ[:,1], S.XYZ[:,2], 'o', color=color, depthshade=False)

    N = S.A.shape[0]
    for i in range(N):
        for j in range(N):
            if S.A[i,j] == 1:
                ax.plot([S.XYZ[i,0], S.XYZ[j,0]], [S.XYZ[i,1], S.XYZ[j,1]], [S.XYZ[i,2], S.XYZ[j,2]], color)
def plot_skeleton_correspondences(ax, S1, S2, corres, color='red'):
    # ax = fh.add_subplot(projection='3d')
    ind_remove = np.where(corres[:,0]==-1)
    corres = np.delete(corres, ind_remove, axis=0)
    ind_remove = np.where(corres[:,1]==-1)
    corres = np.delete(corres, ind_remove, axis=0)

    N = corres.shape[0]
    for i in range(N):
        ax.plot([S1.XYZ[corres[i,0],0], S2.XYZ[corres[i,1],0]],
                [S1.XYZ[corres[i,0],1], S2.XYZ[corres[i,1],1]],
                [S1.XYZ[corres[i,0],2], S2.XYZ[corres[i,1],2]], color)

# current path of the script
path_file = os.path.dirname(os.path.realpath(__file__))
# Load data
species = 'maize'
day1 = '03-13'
day2 = '03-14'
skel_path = path_file+ '/data/{}/{}.graph.txt'
S1_maize = skel.Skeleton.read_graph(skel_path.format(species, day1))
S2_maize = skel.Skeleton.read_graph(skel_path.format(species, day2))

# Perform matching
params = {'weight_e': 0.01, 'match_ends_to_ends': True,  'use_labels' : True, 'label_penalty' : 1, 'debug': False}
corres = skm.skeleton_matching(S1_maize, S2_maize, params)
print("Estimated correspondences: \n", corres)

# visualize results
fh = plt.figure()
# ax = fh.subplots()
ax = fh.add_subplot(111, projection='3d')
plot_skeleton(ax, S1_maize, 'b')
plot_skeleton(ax, S2_maize, 'r')
plot_skeleton_correspondences(ax, S1_maize, S2_maize, corres)
plt.title("Estimated correspondences between skeletons")
plt.show()