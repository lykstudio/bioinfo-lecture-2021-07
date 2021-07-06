Seq1 = "AGTTTATAG"

for i in range(len(Seq1)):
   a = list(Seq1[i:i+2])

print(a.index('TT')



# 강사님 방식
for i in range(len(seq)):
    s = seq[i:i+2]
    print(i, s, s == "TT")
    #if S == "TT":
    #    print(i)

