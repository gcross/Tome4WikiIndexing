#!/usr/bin/python

# ============================================================================== 
# This program takes two arguments: the page to link to, and the kind of thing
# being linked.  It then takes as standard input a list of topics, one on each
# line.  The output is a list of generated links.
# ============================================================================== 

# Needed to make the script work with both Python 2.7 and 3.2
from __future__ import print_function

import sys
link = sys.argv[1]
kind = sys.argv[2]
for talent in sys.stdin.read().split('\n'):
    talent = talent.strip()
    if not talent:
        continue
    print("[[{}|{} ({})]]".format(link,talent,kind))
