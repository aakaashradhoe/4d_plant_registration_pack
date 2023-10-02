#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script provides a demo for the skeleton matching (correspondence estimation) between a pair of skeletons.
"""

import os 

import matplotlib.pyplot as plt
from plant_registration import skeleton as skel
from plant_registration import skeleton_matching as skm
from plant_registration import visualize as vis


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
vis.plot_skeleton(fh, S1_maize,'b')
vis.plot_skeleton(fh, S2_maize,'r')
vis.plot_skeleton_correspondences(fh, S1_maize, S2_maize, corres) 
plt.title("Estimated correspondences between skeletons")

plt.show()