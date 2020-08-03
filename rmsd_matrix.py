#!/usr/bin/env python

import sys, os, glob
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis import align
from MDAnalysis.analysis.rms import rmsd

frame_names = glob.glob("frames/*.pdb")
#print(frame_names)

N = len(frame_names)

# Use first 300 frames for demo
N = 300

rmsd_matrix = np.zeros(shape = (N, N))
print(rmsd_matrix, rmsd_matrix.shape)

import timeit

for iframe in range(N-1):
    start_time = timeit.default_timer()

    mobile = mda.Universe(frame_names[iframe])
    A = mobile.select_atoms('name CA')
    for jframe in range(iframe+1, N):
        ref = mda.Universe(frame_names[jframe])
        B = ref.select_atoms('name CA')
        d = rmsd(A.positions, B.positions, superposition=True)
        rmsd_matrix[iframe][jframe] = d
        rmsd_matrix[jframe][iframe] = d

    elapsed = timeit.default_timer() - start_time
    print("Frame %d - *, elapsed time for align and rmsd = %d seconds" %(iframe, elapsed))

np.save("saved_rmsdmatrix.npy", rmsd_matrix)
