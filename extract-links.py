# This script is placed in the public domain.  It is hosted at https://github.com/gcross/Tome4WikiIndexing.

# Needed to make the script work with both Python 2.7 and 3.2
from __future__ import print_function

import sys

try:
    input_file = open(sys.argv[1],mode='rt')
except IndexError:
    input_file = sys.stdin
input_is_terminal = input_file.isatty()

try:
    output_file = open(sys.argv[2],mode='wt')
except IndexError:
    output_file = sys.stdout
output_is_terminal = output_file.isatty()

# The following regular expression matches on links of the form [[X|Y]]
import re
index_element_matcher = re.compile("\[\[[^|]*\|[^|]*\]\]")

# Use the regular expression to match all of the links
with input_file:
    index_elements = index_element_matcher.findall(input_file.read())

# If the user is copying and pasting directly into standard input and
# expecting the output to be written to the screen, then we insert a
# banner to make it easy to see where the output begins.
if input_is_terminal and output_is_terminal:
    print()
    print('='*80)
    print(' '*32+'  BEGIN OUTPUT  '+' '*32)
    print('='*80)

# The only formatting we perform is to add a colon before each link
# so that it is indented.
with output_file:
    for index_element in index_elements:
        print(":"+index_element,file=output_file)
