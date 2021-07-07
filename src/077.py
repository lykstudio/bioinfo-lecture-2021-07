sum = 0

with open("077.bed", 'r') as handle:
    for line in handle:
        data = line.strip().split("\t")
       #num = int(data[2]) - int(data[1])
        chrom, start, end = data
        length = int(end) - int(start)
        result += length

print(result)