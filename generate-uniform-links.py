# This script is placed in the public domain.  It is hosted at https://github.com/gcross/Tome4WikiIndexing.

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
