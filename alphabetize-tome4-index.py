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

alphabet_sentinel = "<!-- Alphabet goes here -->"
index_sentinel = "<!-- Index goes here -->"
skip_next_line = False

import fileinput
for line in fileinput.input(files=(input_filename,),openhook=lambda input_filename,mode: open(input_filename,mode) if input_filename is not None else sys.stdin):
    if skip_next_line:
        skip_next_line = False
        continue
    line = line.strip()
    if line == alphabet_sentinel:
        skip_next_line = True
    if index is None:
        if line == index_sentinel:
            index = {}
        else:
            prelude.append(line)
    if index is not None:
        if not line or line[0] != ':':
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

with open(output_filename,mode='w') if output_filename is not None else sys.stdout as f:
    for line in prelude:
        if line == alphabet_sentinel:
            print(alphabet_sentinel,file=f)
            print(' '.join('[[#{0:}|{0:}]]'.format(letter) for letter in sorted(letters)),file=f)
        else:
            print(line,file=f)

    print(index_sentinel,file=f)
    last_letter = None
    for key, value in sorted(index.items()):
        if key[0] != last_letter:
            last_letter = key[0]
            print("=={}==".format(key[0]))
        print(":[[{}|{}]]".format(value,key),file=f)
