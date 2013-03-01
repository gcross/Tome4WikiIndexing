# This script is placed in the public domain.  It is hosted at https://github.com/gcross/Tome4WikiIndexing.

# Needed to make the script work with both Python 2.7 and 3.2
from __future__ import print_function

import sys

try:
    input_filename = sys.argv[1]
    input_is_terminal = False
except IndexError:
    input_filename = None
    input_is_terminal = sys.stdin.isatty()

try:
    output_filename = sys.argv[2]
    output_is_terminal = False
except IndexError:
    output_filename = None
    output_is_terminal = sys.stdout.isatty()

prelude = []
index = None
letters = set()

# Read through the file adding everything that we see to the prelude until
# we see a section header which marks the beginning of the index section.
import fileinput
for line in fileinput.input(files=(input_filename,),openhook=lambda input_filename,mode: open(input_filename,mode) if input_filename is not None else sys.stdin):
    line = line.strip()
    if index is None:
        if line[:1] == "=":
            index = {}
        else:
            prelude.append(line)
    if index is not None:
        if line[:1] != ':':
            continue
        try:
            value, key = line[3:-2].split('|')
        except ValueError:
            print('Error at line {}: invalid syntax'.format(fileinput.filelineno()))
            sys.exit(-1)
        value = value.replace(' ','-')
        value = value.replace('_','-')
        if key in index:
            if index[key] != value:
                print('Error at line {}: key "{}" has multiple values -- specifically, at least "{}" and "{}".'.format(fileinput.filelineno(),key,index[key],value),file=sys.stderr)
                sys.exit(-1)
        else:
            index[key] = value
        letters.add(key[0])

# If the user is copying and pasting directly into standard input and
# expecting the output to be written to the screen, then we insert a
# banner to make it easy to see where the output begins.
if input_is_terminal and output_is_terminal:
    print()
    print('='*80)
    print(' '*32+'  BEGIN OUTPUT  '+' '*32)
    print('='*80)

# Print first the prelude and then the index with each first letter
# getting its own section.
with open(output_filename,mode='w') if output_filename is not None else sys.stdout as f:
    for line in prelude:
        print(line,file=f)

    last_letter = None
    for key, value in sorted(index.items()):
        if key[0] != last_letter:
            last_letter = key[0]
            print("=={}==".format(key[0]))
        print(":[[{}|{}]]".format(value,key),file=f)
