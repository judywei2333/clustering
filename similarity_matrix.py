#!/usr/bin/env python

import sys, os, glob
import numpy as np

frame_names = glob.glob("frames/*.pdb")

N = len(frame_names)

# Use first 300 frames for demo
N = 300

similarity_matrix = np.zeros(shape = (N, N))

import timeit

for iframe in range(N-1):
    start_time = timeit.default_timer()
    pts = np.loadtxt(frame_names[iframe], usecols=[6, 7, 8])
    A = np.sqrt(np.sum((pts[None, :] - pts[:, None])**2, -1))
    for jframe in range(iframe+1, N):
        pts = np.loadtxt(frame_names[jframe], usecols=[6, 7, 8])
        B = np.sqrt(np.sum((pts[None, :] - pts[:, None])**2, -1))
        d = np.sqrt(np.mean((A-B)**2))
        similarity_matrix[iframe][jframe] = d
        similarity_matrix[jframe][iframe] = d

    elapsed = timeit.default_timer() - start_time
    print("Frame %s elapsed time = %d seconds" %(iframe, elapsed))

np.save("saved_simlaritymatrix.npy", similarity_matrix)
