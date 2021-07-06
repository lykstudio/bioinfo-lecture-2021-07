l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

print(max(l))
print(min(l))



# 034

cnt = dict()
for elem in data:
    if cnt not in data:
        cnt[elem] = 0
    cnt[elem] += 1
print(cnt) 
 
