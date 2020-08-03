#!/usr/bin/env python

import sys
import glob, os

for path in sys.argv[1:]:

    for fname in glob.glob("%s/*stripped*.pdb" % path):
        ca_lines = [line for line in open(fname).readlines() if line[:6] == "ATOM  " and line[12:16] == " CA "]
        saved_name, _ = os.path.basename(fname).split("-")
        saved_name = saved_name+"-ca.pdb"
        open(saved_name, "w").writelines(ca_lines)

