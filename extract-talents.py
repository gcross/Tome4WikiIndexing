#!/usr/bin/python

# ============================================================================== 
# This script takes advantage of the fact that most of the talent pages have the
# name of the talent at the beginning of the line (more precisely just after the
# bullet, but the bullet is dropped when copying and pasting the raw text)
# followed by a semicolon.  Run it with the name of the page to be linked as the
# first argument and copy and paste the page into the program after you run it
# (followed by typing Control-D once or twice).  Note that occasionally there
# will be other words with this format so you need to scan the resulting list
# for mistakes before using it.
# ============================================================================== 

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
