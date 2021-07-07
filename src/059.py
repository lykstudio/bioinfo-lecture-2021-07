import gzip
import sys
from typing import Dict

if len(sys.argv) != 2 :
    print(f"#usage: python {sys.argv[0]} [file")
    sys.exit()

file_name = sys.argv[0]

data = dict()

with gzip.open(file_name, 'rt') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base in data:
                data[base] = 0
            data[base] += 1



# 강사님
data = dict()

with open("059.fasta", 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base in data:
                data[base] = 0
            data[base] += 1