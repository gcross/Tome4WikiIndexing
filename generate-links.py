#!/usr/bin/python

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
