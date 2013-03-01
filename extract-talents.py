# This script is placed in the public domain.  It is hosted at https://github.com/gcross/Tome4WikiIndexing.

# Needed to make the script work with both Python 2.7 and 3.2
from __future__ import print_function

import re
import sys

try:
    link = sys.argv[1]
except IndexError:
    print("This program must be given the kind of talent as the first argument.")
    sys.exit(-1)
text = sys.stdin.read()

if sys.stdout.isatty():
    print()
    print('='*80)
    print(' '*32+'  BEGIN OUTPUT  '+' '*32)
    print('='*80)
for talent in re.findall("^[\\w ]*:",text,re.MULTILINE):
    talent = talent[:-1]
    if talent in ["Welcome","Note","Search this site"]: continue
    print("[[talents-{}|{} (talent)]]".format(link,talent))
