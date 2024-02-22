#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script provides a demo for iterative non-rigid registration procedure between a pair of skeletons.
"""
import numpy as np
import matplotlib.pyplot as plt
from plant_registration import skeleton as skel
from plant_registration import skeleton_matching as skm
from plant_registration import non_rigid_registration as nrr
from plant_registration.iterative_registration import iterative_registration
from plant_registration import visualize as vis
import os

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

# source directory
path_file = os.path.dirname(os.path.realpath(__file__))
# %% load skeleton data
species = 'maize'
day1 = '03-13'
day2 = '03-14'
skel_path = path_file + '/data/{}/{}.graph.txt'
S1 = skel.Skeleton.read_graph(skel_path.format(species, day1))
S2 = skel.Skeleton.read_graph(skel_path.format(species, day2))

# visualize input data
fh1 = plt.figure()
ax1 = fh1.add_subplot(111, projection="3d")
plot_skeleton(ax1, S1, 'b')
plot_skeleton(ax1, S2, 'r')
plt.title("Initial skeleton")
plt.show()

# %% compute non-rigid registration params

# set matching params
match_params = {'weight_e': 0.01,
                'match_ends_to_ends': True,
                'use_labels' : False,
                'label_penalty' : 1,
                'debug': False}

# set registration params
reg_params = {'num_iter': 20,
              'w_rot' : 100,
              'w_reg' : 100,
              'w_corresp' : 1,
              'w_fix' : 1,
              'fix_idx' : [],
              'R_fix' : [np.eye(3)],
              't_fix' : [np.zeros((3,1))],
              'use_robust_kernel' : True,
              'robust_kernel_type' : 'cauchy',
              'robust_kernel_param' : 2,
              'debug' : False}

# iterative procedure params
params = {'num_iter' : 5,
          'visualize': True,
          'match_params': match_params,
          'reg_params': reg_params}

# call register function
T12, corres = iterative_registration(S1, S2, params)

# %% Apply registration params to skeleton
S2_hat = nrr.apply_registration_params_to_skeleton(S1, T12)

# %% visualize registration results
fh = plt.figure()
ax = fh.add_subplot(111, projection="3d")
plot_skeleton(ax, S1,'b')
plot_skeleton(ax, S2_hat,'k')
plot_skeleton(ax, S2,'r')
plot_skeleton_correspondences(ax, S2_hat, S2, corres)
plt.title("Skeleton registration results")

