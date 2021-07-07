from Bio import SeqIO

f = "covid19.fasta"

record = SeqIO.read(f, "fasta")

print(f"A: {record.seq.count('A')}")
print(f"C: {record.seq.count('C')}")
print(f"G: {record.seq.count('G')}")
print(f"T: {record.seq.count('T')}")


