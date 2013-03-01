#!/usr/bin/python

# ============================================================================== 
# This program takes two arguments: the base name of the page to link to, and 
# the kind of thing being linked.  It then takes as standard input a list of 
# topics, one on each line.  The output is a list of generated links.
#
# That is to say, running this program with arguments X and Y, input Z on each
# line will result in an output line [[X-z|Z (Y)]], where z is Z changed to
# lowercase and with spaces changed to hyphens.
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
    print("[[{}-{}|{} ({})]]".format(link,talent.lower().replace(' ','-'),talent,kind))
