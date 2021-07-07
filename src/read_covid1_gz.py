# ACGT의 개수와 전체 길이를 covid19.count.txt로 만드는 파이썬 스크립트 작성

import gzip
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [file]")
    sys.exit()

file_name = sys.argv[1]

data = dict()

with gzip.open(file_name, 'rt') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
        data[base] += 1

print(data)
