#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script provides a demo for pointcloud deformation using the skeleton registration parameters.
"""

import numpy as np
import matplotlib.pyplot as plt
import os 
from plant_registration import skeleton as skel
from plant_registration import skeleton_matching as skm
from plant_registration import pointcloud as pcd
from plant_registration import visualize as vis

# source directory
path_file = os.path.dirname(os.path.realpath(__file__))
# %% Load data
species = 'maize'
day1 = '03-13'
day2 = '03-14'
skel_path = path_file+ '/data/{}/{}.graph.txt'
pc_path = path_file + '/data/{}/{}.xyz'
corres_path = path_file+ '/data/{}/{}-{}.corres.txt'
reg_path = path_file + '/data/{}/{}-{}.reg.npy'
S1 = skel.Skeleton.read_graph(skel_path.format(species, day1))
S2 = skel.Skeleton.read_graph(skel_path.format(species, day2))
P1 = pcd.load_pointcloud(pc_path.format(species, day1))
P2 = pcd.load_pointcloud(pc_path.format(species, day2))
corres = np.loadtxt(corres_path.format(species, day1, day2), dtype = np.int32)
T12 = np.load(reg_path.format(species, day1, day2))  

# deform complete pointcloud
P1_ds = pcd.downsample_pointcloud(P1, 3)
P2_ds = pcd.downsample_pointcloud(P2, 3)
P1_deformed = pcd.deform_pointcloud(P1_ds, T12, corres, S1, S2)

# visualize results
fh = plt.figure()
vis.plot_skeleton(fh, S1,'b')
vis.plot_skeleton(fh, S2,'r')
vis.plot_pointcloud(fh, P2,'r')
vis.plot_pointcloud(fh, P1_deformed,'b')
vis.plot_skeleton_correspondences(fh, S1, S2, corres, 'g')

plt.show()