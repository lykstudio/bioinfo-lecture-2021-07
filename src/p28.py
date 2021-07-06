seq = "ATGTTATAG"
com_seq = ""
com_data = {"A":"T", "T":"A", "G":"C", "C":"G"}
for s in seq:
    comp_seq += com_data[s]

print(seq)
print(comp_seq)


#추가로 해본 것
for i in range(len(seq)):
    s =  seq[i]
    cs = comp_seq[i]
    bond = "="
    if s == "A" or s == "T":
        bond = "="
    print(f"s{s}{bond}{cs}")

