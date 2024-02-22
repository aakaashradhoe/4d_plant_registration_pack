import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_pointcloud(fh, P, color='r'):
    ax = fh.add_subplot(projection='3d')
    ax.scatter(P[:,0], P[:,1], P[:,2], '.', color=color, depthshade=False)


def plot_semantic_pointcloud(fh, array_list):
    """
    :param array_list: a list of numpy arrays, each array represents a different class
    """
    ax = fh.add_subplot(projection='3d')

    for P in array_list:
        P = np.asarray(P)
        ax.scatter(P[:,0], P[:,1], P[:,2], '.')


## when using the functions from here it gives:
# AttributeError: 'Axes3D' object has no attribute 'add_subplot'
# yet in the script itself it works
def plot_skeleton(ax, S, color='blue'):
    ax.scatter(S.XYZ[:,0], S.XYZ[:,1], S.XYZ[:,2], 'o', color=color, depthshade=False)

    N = S.A.shape[0]
    for i in range(N):
        for j in range(N):
            if S.A[i,j] == 1:
                ax.plot([S.XYZ[i,0], S.XYZ[j,0]], [S.XYZ[i,1], S.XYZ[j,1]], [S.XYZ[i,2], S.XYZ[j,2]], color)
def plot_skeleton_correspondences(ax, S1, S2, corres, color='red'):
    ind_remove = np.where(corres[:,0]==-1)
    corres = np.delete(corres, ind_remove, axis=0)
    ind_remove = np.where(corres[:,1]==-1)
    corres = np.delete(corres, ind_remove, axis=0)

    N = corres.shape[0]
    for i in range(N):
        ax.plot([S1.XYZ[corres[i,0],0], S2.XYZ[corres[i,1],0]],
                [S1.XYZ[corres[i,0],1], S2.XYZ[corres[i,1],1]],
                [S1.XYZ[corres[i,0],2], S2.XYZ[corres[i,1],2]], color)
