# Clustering samples with distance matrix

Given thousands of MD snapshots, how do we group them into clusters and pick representative snapshots for each cluster?

The "distance" or "dissimilarity" of key residues can be measured by RMSD of key residue positions. With this distance matrix at hand, this subroutine will find clusters and the medoids.
