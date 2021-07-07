# 내가 푼 방법

# num = 0

# with open("070.vcf", 'r') as handle:
#     for line in handle:
#         if line.startswith("#"):
#            continue
#         #num += 1  
#         data = line.strip().split("\t")
#         if data[6] == "PASS":
#             continue
#         num += 1


# print(num)


# # 강사님 풀이
# cnt_all = 0
# cnt_pass = 0

# with open("070.vcf", 'r') as handle:
#     for line in handle:
#         if line.startswith("#"):
#            continue
#         data = line.strip().split("\t")
#         cnt_all += 1
#         if data[6] == "PASS":
#             cnt_pass += 1

# print(cnt_pass, cnt_all, cnt_pass / cnt_all)


# filter 위치를 6으로 찾지 말고 알아서 index번호 찾아서 대입하는 방법
cnt_all = 0
cnt_pass = 0

with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
           continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            cnt_pass += 1

print(cnt_pass, cnt_all, cnt_pass / cnt_all)