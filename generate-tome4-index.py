from __future__ import print_function

import sys

try:
    input_file = open(sys.argv[1],mode='rt')
except IndexError:
    input_file = sys.stdin

try:
    output_file = open(sys.argv[2],mode='rt')
except IndexError:
    output_file = sys.stdout

import re
index_element_matcher = re.compile("\[\[[^|]*\|[^|]*\]\]")

with input_file:
    index_elements = index_element_matcher.findall(input_file.read())

if input_file is sys.stdin and output_file is sys.stdout:
    print()
    print('='*80)
    print(' '*32+'  BEGIN OUTPUT  '+' '*32)
    print('='*80)

with output_file:
    for index_element in index_elements:
        print(":"+index_element,file=output_file)
