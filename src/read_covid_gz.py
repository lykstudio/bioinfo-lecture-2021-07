import gzip

file_name = "covid19.fasta.gz"

data = dict()

with gzip.open(file_name, 'rt') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in base:
                data[base] = 0

print(data)


#sys로 파일 열기

import sys

if len(sys.argv) != 2:
    print(f"usage: python {sys.argv[0] [file]")
    sys.exit()

file_name = sys.argv[1]



