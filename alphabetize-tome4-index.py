from __future__ import print_function

import sys

try:
    input_filename = sys.argv[1]
except IndexError:
    input_filename = None

try:
    output_filename = sys.argv[2]
except IndexError:
    output_filename = None

prelude = []
index = None
letters = set()

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
        if key in index:
            if index[key] != value:
                print('Error at line {}: key "{}" has multiple values -- specifically, at least "{}" and "{}".'.format(fileinput.filelineno(),key,index[key],value),file=sys.stderr)
                sys.exit(-1)
        else:
            index[key] = value
        letters.add(key[0])

if input_filename is output_filename:
    print()
    print('='*80)
    print(' '*32+'  BEGIN OUTPUT  '+' '*32)
    print('='*80)

with open(output_filename,mode='w') if output_filename is not None else sys.stdout as f:
    for line in prelude:
        print(line,file=f)

    last_letter = None
    for key, value in sorted(index.items()):
        if key[0] != last_letter:
            last_letter = key[0]
            print("=={}==".format(key[0]))
        print(":[[{}|{}]]".format(value,key),file=f)
